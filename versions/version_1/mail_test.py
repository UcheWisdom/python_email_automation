
import os
import smtplib
import ssl

from dotenv import load_dotenv
from email.message import EmailMessage

# Load environment variables
load_dotenv()

# Get Gmail credentials
sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_PASSWORD")

# Check credentials
if not sender_email or not app_password:
    raise ValueError("Email credentials are missing from .env")

# Get recipient details
recipient_email = input("Enter recipient email: ")

# Create email
message = EmailMessage()
message["Subject"] = "Python Automation - Test Email"
message["From"] = sender_email
message["To"] = recipient_email

message.set_content("""
Hello!

This is my first automated email using Python.

The email was sent successfully through Gmail SMTP.

Regards,
Python Email Automation System
""")

# Connect and send email
try:
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        server.login(sender_email, app_password)
        server.send_message(message)

    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your Gmail credentials.")

except smtplib.SMTPException as error:
    print(f"Email sending failed: {error}")

except OSError as error:
    print(f"Connection error: {error}")
