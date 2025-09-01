### Project: markdown2kindle

**Objective:** Create a command-line tool that converts a Markdown file to HTML and emails it to a user's Kindle address.

**Project Directory:** `C:\GitHub\MarkdownToKindle`

---

#### Phase 1: Prerequisites & Environment Setup

1.  **Gmail Account Setup (Manual)**
    *   Enable 2-Step Verification for the sending Gmail account.
    *   Create a 16-character "App Password" for this tool.
    *   Store this password securely.

2.  **Amazon Kindle Setup (Manual)**
    *   Navigate to "Manage Your Content and Devices" > "Preferences" > "Personal Document Settings" on your Amazon account.
    *   Note your Kindle's email address (e.g., `your_name@kindle.com`).
    *   Add your sending Gmail address to the "Approved Personal Document E-mail List".

3.  **Local Project Initialization**
    *   Navigate to `C:\GitHub\MarkdownToKindle`.
    *   Initialize a Poetry project: `poetry init`.
        *   Name: `markdown2kindle`
        *   Version: `0.1.0`
        *   Description: A tool to convert and send Markdown files to a Kindle device.
        *   Author: [Your Name]
        *   License: [Your License]
        *   Compatible Python versions: `^3.10`
        *   Define main dependencies interactively: No.
        *   Define development dependencies interactively: No.
    *   This creates `pyproject.toml`.

4.  **Create `.gitignore`**
    *   Create a file named `.gitignore` in the root directory with the following content:
        ```gitignore
        # Python
        __pycache__/
        *.pyc
        *.pyo
        *.pyd
        
        # Virtualenv
        .venv/
        venv/
        env/
        
        # Environment
        .env
        
        # IDEs
        .vscode/
        .idea/
        ```

5.  **Create `.env`**
    *   Create a file named `.env` in the root directory. This file will not be committed to source control.
    *   Add the following key-value pairs, replacing the placeholder values:
        ```ini
        SENDER_EMAIL="your_gmail_address@gmail.com"
        GMAIL_APP_PASSWORD="your_16_character_app_password"
        KINDLE_EMAIL="your_kindle_address@kindle.com"
        ```

6.  **Create `README.md`**
    *   Create `README.md` in the root directory with initial content:
        ````markdown
        # markdown2kindle
        
        A command-line tool to convert a local Markdown file to HTML and email it to your Kindle device.
        
        ## Prerequisites
        
        1.  **Gmail Account**: You need a Gmail account to send the email.
            - Enable 2-Step Verification.
            - Create a 16-character "App Password". See Google's documentation for instructions.
        
        2.  **Kindle Device**:
            - Find your Send-to-Kindle email address under "Manage Your Content and Devices" > "Preferences" > "Personal Document Settings" on your Amazon account.
            - Add your sending Gmail address to the "Approved Personal Document E-mail List" on that same page.
        ````

#### Phase 2: Connection Test

1.  **Install Dependencies**
    *   Install the library needed to read the `.env` file:
        `poetry add python-dotenv`

2.  **Create Ping/Ack Test Script**
    *   Create a new file: `test_connection.py`.
    *   Write a script that loads environment variables from `.env`, connects to Google's SMTP server, and sends a plain text email to the Kindle address.
    *   **Subject:** `Ping Test`
    *   **Body:** `This is a connection test for the markdown2kindle tool.`
    *   The script must provide clear success or failure output to the console.

3.  **Execute and Verify**
    *   Run the script: `poetry run python test_connection.py`.
    *   Confirm the document `Ping Test` appears on the target Kindle device.
    *   Debug any authentication or configuration issues. After successful verification, this script can be deleted.

#### Phase 3: Core Tool Development

1.  **Install Core Dependency**
    *   Install a Markdown conversion library:
        `poetry add markdown2`

2.  **Create Application Structure**
    *   Create a package directory: `mkdir markdown2kindle`
    *   Create the main script file: `touch markdown2kindle/main.py`
    *   Create an init file: `touch markdown2kindle/__init__.py`

3.  **Implement Core Logic in `markdown2kindle/main.py`**
    *   Define **Function 1: `convert_markdown_to_html(filepath)`**
        *   Accepts a file path string.
        *   Reads the content of the Markdown file.
        *   Uses the `markdown2` library to convert the content to an HTML string.
        *   Returns the HTML string.
    *   Define **Function 2: `send_to_kindle(html_content, title)`**
        *   Accepts an HTML string and a title string.
        *   Loads credentials from `.env`.
        *   Constructs an email using `email.mime` multipart message.
        *   Sets the `To`, `From`, and `Subject` headers. The subject will be the `title`.
        *   Attaches the `html_content` as an HTML attachment with the filename `document.html`.
        *   Uses `smtplib` to connect to `smtp.gmail.com:587` and send the email.

4.  **Implement CLI Logic in `markdown2kindle/main.py`**
    *   Define a function named `main()`. This function will serve as the application's entry point.
    *   Inside `main()`, use the built-in `argparse` module to:
        *   Define one positional argument: `filepath`.
        *   Parse the command-line arguments.
        *   Extract a document title from the base filename of the provided `filepath`.
        *   Call `convert_markdown_to_html()` with the `filepath`.
        *   Call `send_to_kindle()` with the resulting HTML and title.
        *   Print status messages to the console (e.g., "Converting...", "Sending...", "Sent successfully.").
    *   At the end of the file, add a main execution block to allow direct execution for testing: `if __name__ == "__main__": main()`

5.  **Expose as a Console Script**
    *   In `pyproject.toml`, add the following section to define the console script entry point. This links the command `markdown2kindle` to the `main` function.
        ```toml
        [tool.poetry.scripts]
        markdown2kindle = "markdown2kindle.main:main"
        ```

#### Phase 4: Finalization

1.  **Testing**
    *   Create a sample file, `test.md`.
    *   Run the tool from the command line:
        `poetry run markdown2kindle test.md`
    *   Verify the document arrives on the Kindle and is formatted correctly.
    *   Test with a file path that does not exist to observe the error handling.

2.  **Update `README.md`**
    *   Add `Installation` and `Usage` sections.
    *   Provide the `poetry install` command for installation.
    *   Provide the `poetry run markdown2kindle /path/to/your/file.md` command for usage.