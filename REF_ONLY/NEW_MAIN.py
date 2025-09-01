import os
import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import markdown2

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def get_kindle_emails():
    devices = []
    idx = 1
    while True:
        email = os.getenv(f"KINDLE_EMAIL_{idx}")
        label = os.getenv(f"KINDLE_LABEL_{idx}", f"Device {idx}")
        if email:
            devices.append((label, email))
            idx += 1
        else:
            break
    return devices

def select_kindle_email():
    devices = get_kindle_emails()
    if not devices:
        raise RuntimeError("No KINDLE_EMAILs found in environment variables.")
    print("Select a Kindle device to send to:")
    for i, (label, email) in enumerate(devices, 1):
        print(f"{i}. {label} ({email})")
    selection = None
    while selection is None:
        try:
            choice = int(input("Enter number: ").strip())
            if 1 <= choice <= len(devices):
                selection = devices[choice-1][1]
            else:
                print("Invalid selection.")
        except Exception:
            print("Enter a valid number.")
    return selection

def convert_markdown_to_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown2.markdown(markdown_content)
    return html_content

def send_to_kindle(html_content, title, kindle_email):
    msg = MIMEMultipart()
    msg["Subject"] = title
    msg["From"] = SENDER_EMAIL
    msg["To"] = kindle_email

    part = MIMEApplication(html_content.encode('utf-8'), Name=f"{title}.html")
    part['Content-Disposition'] = f'attachment; filename="{title}.html"'
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML and send to Kindle.')
    parser.add_argument('filepath', help='The path to the Markdown file.')
    args = parser.parse_args()

    title = os.path.splitext(os.path.basename(args.filepath))[0]

    kindle_email = select_kindle_email()

    print("Converting...")
    html_content = convert_markdown_to_html(args.filepath)

    print(f"Sending to {kindle_email}...")
    send_to_kindle(html_content, title, kindle_email)

    print("Sent successfully.")

if __name__ == "__main__":
    main()
