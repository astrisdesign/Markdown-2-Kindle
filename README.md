# Markdown 2 Kindle

A command-line tool to convert a local Markdown file to HTML and email it to your Kindle device.

This tool is perfect for sending articles, notes, or any Markdown-formatted text to your Kindle for easy reading. It supports sending to multiple Kindle devices and gracefully handles embedded-link Markdown images by converting them to links.

## Features

-   Converts any local Markdown file to a Kindle-friendly HTML format.
-   Supports multiple Kindle devices with an interactive selection menu.
-   Uses a secure Gmail "App Password" for authentication.
-   Handles Markdown images (`![alt](url)`) by converting them to linked text to avoid formatting issues.
-   Simple command-line interface.

## Setup

Before you can use the tool, you'll need to configure your Amazon account, your Gmail account, and the local project environment.

### Step 1: Configure Your Amazon Kindle Account

Your Kindle can only receive documents from approved email addresses.

1.  Navigate to the [Amazon Content and Devices](https://www.amazon.com/hz/mycd/myx#/home/settings/payment) page and click on the **"Preferences"** tab.
2.  Scroll down and open the **"Personal Document Settings"** section.
3.  Under **"Send-to-Kindle E-Mail Settings"**, find your Kindle's email address (e.g., `your_name_123@kindle.com`). You will need this for the `.env` file.
4.  Scroll down to the **"Approved Personal Document E-mail List"** and click **"Add a new approved e-mail address"**.
5.  Enter the Gmail address you will be sending from and click **"Add Address"**.

### Step 2: Configure Your Gmail Account

This tool sends email via Google's SMTP server. For security, you must use a dedicated "App Password" instead of your regular account password.

1.  Go to your [Google Account](https://myaccount.google.com/) settings.
2.  Enable **2-Step Verification** if you haven't already. This is required to generate App Passwords.
3.  Navigate to **Security** > **2-Step Verification** > **App passwords**.
4.  When prompted, give the app a name (e.g., `markdown2kindle`) and click **"Create"**.
5.  Google will generate a 16-character password. **Copy this password immediately.** You will not be able to see it again.

### Step 3: Configure the Local Environment

The project uses a `.env` file to store your credentials and Kindle email addresses securely.

1.  Clone this repository to your local machine.
2.  In the root directory of the project, create a file named `.env`.
3.  Add your credentials and Kindle device information to the `.env` file using the following format.

```ini
# .env file

# Your Gmail account and the 16-character App Password
SENDER_EMAIL="your_gmail_address@gmail.com"
GMAIL_APP_PASSWORD="the16characterapppassword"

# --- Kindle Devices ---
# You can add one or more devices.
# The script will find all devices numbered sequentially starting from 1.

# First device
KINDLE_EMAIL_1="your_first_device@kindle.com"
KINDLE_LABEL_1="My Kindle Oasis"

# Second device (optional)
KINDLE_EMAIL_2="your_second_device@free.kindle.com"
KINDLE_LABEL_2="Phone - Kindle App"

# Add more as needed...
# KINDLE_EMAIL_3="..."
# KINDLE_LABEL_3="..."
```

**Note:** The `.env` file is included in `.gitignore` and should never be committed to source control.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```sh
# Clone the repository (if you haven't already)
git clone https://github.com/your-username/markdown2kindle.git
cd markdown2kindle

# Install dependencies using Poetry
poetry install
```

## Usage

Run the tool from within the project directory using `poetry run`. The only required argument is the path to your Markdown file.

```sh
poetry run markdown2kindle /path/to/your/file.md
```

If you have configured multiple Kindle devices in your `.env` file, you will see an interactive prompt to select a destination:

```
$ poetry run markdown2kindle docs/my-article.md
Select a Kindle device to send to:
1. My Kindle Oasis (your_first_device@kindle.com)
2. Phone - Kindle App (your_second_device@free.kindle.com)
Enter number: 2

Converting...
Sending to your_second_device@free.kindle.com...
Sent successfully.
```

The document will arrive on your Kindle shortly with a title matching the filename (e.g., `my-article`).

## License

This project is licensed under the MIT License. See the `pyproject.toml` file for details.
