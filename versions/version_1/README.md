# Version 1: Gmail Test Email Sender

## 1. Project Overview

Version 1 is the foundation of the Python Email Automation System.

The purpose of this version is to establish a working connection between Python and Gmail using Gmail's SMTP (Simple Mail Transfer Protocol) service.

The application allows a user to enter a recipient's email address and automatically sends a predefined test email.

This version introduces basic email automation and secure credential management.

## 2. Features

- Connects to Gmail using SMTP.
- Authenticates using a Gmail App Password.
- Retrieves credentials from environment variables.
- Accepts a recipient's email address.
- Creates and sends a formatted email.
- Handles common authentication and connection errors.

## 3. Technologies and Libraries

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| smtplib | Connects Python to Gmail SMTP |
| ssl | Provides secure communication |
| os | Retrieves environment variables |
| python-dotenv | Loads variables from the `.env` file |
| email.message | Creates and formats email messages |

## 4. Source Code Explanation

### A. Importing the libraries

```python
import os
import smtplib
import ssl

from dotenv import load_dotenv
from email.message import EmailMessage
```

**Line 1: `import os`**

Imports Python's built-in operating system module.

In this project, we use it to retrieve environment variables containing our Gmail credentials.

**Line 2: `import smtplib`**

Imports Python's built-in SMTP library.

SMTP stands for Simple Mail Transfer Protocol. It is the protocol used to send emails between mail servers.

We use this library to establish a connection with Gmail and send messages.

**Line 3: `import ssl`**

Imports Python's SSL module.

It provides security features for network communication.

We use it to create a secure connection when communicating with Gmail.

**Line 4: `from dotenv import load_dotenv`**

Imports the `load_dotenv()` function from the external `python-dotenv` library.

This function reads variables stored in our `.env` file and makes them available to Python.

**Line 5: `from email.message import EmailMessage`**

Imports Python's built-in `EmailMessage` class.

It allows us to construct an email with a subject, sender, recipient and message body.

### B. Loading environment variables

```python
load_dotenv()
```

This function loads the variables stored in our `.env` file.

For example:

```env
EMAIL_ADDRESS=your_gmail@gmail.com
EMAIL_PASSWORD=your_app_password
```

After loading the file, Python can retrieve these values without hardcoding them into the source code.

### C. Retrieving Gmail credentials

```python
sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_PASSWORD")
```

**Line 1: `sender_email = os.getenv("EMAIL_ADDRESS")`**

Uses `os.getenv()` to retrieve the value of the `EMAIL_ADDRESS` environment variable.

The retrieved email address is stored in the `sender_email` variable.

**Line 2: `app_password = os.getenv("EMAIL_PASSWORD")`**

Retrieves the Gmail App Password from the environment variables.

The value is stored in `app_password`.

This keeps the actual password outside the Python source code.

### D. Validating credentials

```python
if not sender_email or not app_password:
    raise ValueError("Email credentials are missing from .env")
```

**Line 1: `if not sender_email or not app_password:`**

Checks whether either of the required credentials is missing or empty.

The `or` operator means that if at least one condition is true, the code inside the `if` statement will execute.

**Line 2: `raise ValueError(...)`**

Raises a `ValueError` exception if the credentials are missing.

This prevents the application from continuing without the required Gmail credentials.

### E. Collecting recipient information

```python
recipient_email = input("Enter recipient email: ")
```

The `input()` function displays a message in the terminal and waits for the user to enter information.

The entered email address is stored in `recipient_email`.

This allows the user to choose who receives the email.

### F. Creating the email message

```python
message = EmailMessage()
```

Creates a new email message object.

The `EmailMessage` class provides methods and properties for constructing an email.

```python
message["Subject"] = "Python Automation - Test Email"
```

Sets the subject of the email.

```python
message["From"] = sender_email
```

Sets the sender's email address using the Gmail account retrieved from the environment variables.

```python
message["To"] = recipient_email
```

Sets the recipient's email address using the information entered by the user.

### G. Setting the email body

```python
message.set_content("""
Hello!

This is my first automated email using Python.

The email was sent successfully through Gmail SMTP.

Regards,
Python Email Automation System
""")
```

The `set_content()` method defines the main body of the email.

The triple quotation marks (`"""`) allow us to write a multiline string.

This makes it possible to format the email body across multiple lines.

### H. Establishing a secure connection

```python
try:
    context = ssl.create_default_context()
```

**Line 1: `try:`**

Begins a `try` block.

Python uses exception handling to detect and manage errors that might occur while executing the code.

**Line 2: `context = ssl.create_default_context()`**

Creates a default SSL security context.

This context provides the security configuration needed when establishing an encrypted connection.

### I. Connecting to Gmail SMTP

```python
with smtplib.SMTP("smtp.gmail.com", 587) as server:
```

Establishes a connection with Gmail's SMTP server.

- `smtplib.SMTP()` creates the SMTP connection.
- `smtp.gmail.com` is Gmail's SMTP server address.
- `587` is the port used for SMTP with STARTTLS.

The `with` statement manages the connection and automatically closes it when the block finishes.

The connection object is stored in the `server` variable.

```python
server.ehlo()
```

Introduces our application to the SMTP server and identifies the available SMTP capabilities.

```python
server.starttls(context=context)
```

Requests an upgrade from the initial SMTP connection to an encrypted TLS connection.

This helps protect information transmitted between Python and Gmail.

```python
server.ehlo()
```

Introduces the application to the SMTP server again after TLS has been established.

This allows the client to identify the capabilities available over the secured connection.

### J. Authenticating with Gmail

```python
server.login(sender_email, app_password)
```

Authenticates our application with Gmail.

It uses:

- `sender_email`: The Gmail account.
- `app_password`: The Gmail App Password.

Gmail verifies these credentials before allowing the application to send email.

### K. Sending the email

```python
server.send_message(message)
```

Sends the email message created earlier.

The SMTP server processes the message and attempts to deliver it to the specified recipient.

### L. Confirming successful delivery submission

```python
print("Email sent successfully!")
```

Displays a success message in the terminal after the SMTP server accepts the message for sending.

Note that this confirms submission to the SMTP server, not necessarily final delivery to the recipient's inbox.

### M. Handling errors

```python
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your Gmail credentials.")
```

Catches authentication errors.

This can happen when Gmail rejects the account credentials or App Password.

```python
except smtplib.SMTPException as error:
    print(f"Email sending failed: {error}")
```

Catches other SMTP-related errors.

The `error` variable stores information about the exception.

The `f` before the string allows Python to insert the error message into the output.

```python
except OSError as error:
    print(f"Connection error: {error}")
```

Catches operating-system-related errors, including many network and connection failures.

This helps the application report connection problems instead of terminating without a useful explanation.

## 5. Application Execution

To execute the application, open the terminal inside the `version-1` directory and run:

```bash
python mail_test.py
```

The application requests the recipient's email address.

After the user enters the address, Python creates the email, connects to Gmail, authenticates and sends the message.

## 6. Security Considerations

The Gmail App Password must never be hardcoded into the Python source code.

Credentials should be stored in the `.env` file.

The `.env` file must be included in `.gitignore` to prevent Git from uploading sensitive information to GitHub.

Never publish the App Password in project documentation, screenshots or source code.

## 7. Current Limitations

Version 1 is intentionally simple.

It does not yet support:

- Automatic scheduling.
- Google Sheets integration.
- Multiple predefined recipients.
- User registration and authentication.
- Custom email templates.
- Company logos and branding.
- PDF report generation.
- Automatic report attachments.

These features will be introduced in subsequent versions.

## 8. Version Summary

Version 1 successfully establishes the foundation for the Python Email Automation System.

It demonstrates how Python can communicate with Gmail through SMTP, authenticate securely, construct an email and send it to a recipient.

**Status: Completed and tested.**
