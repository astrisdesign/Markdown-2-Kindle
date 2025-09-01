
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
KINDLE_EMAIL = os.getenv("KINDLE_EMAIL")

def test_connection():
    try:
        msg = MIMEMultipart()
        msg["Subject"] = "Ping Test"
        msg["From"] = SENDER_EMAIL
        msg["To"] = KINDLE_EMAIL

        # Attach a simple text file
        test_content = b"This is a connection test for the markdown2kindle tool."
        part = MIMEApplication(test_content, Name="test.txt")
        part['Content-Disposition'] = 'attachment; filename="test.txt"'
        msg.attach(part)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
        print("Connection test successful. Attachment sent to Kindle.")
    except Exception as e:
        print(f"Connection test failed: {e}")

if __name__ == "__main__":
    test_connection()
