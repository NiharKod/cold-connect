import os
from dotenv import load_dotenv
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText


# Load environment variables from .env file
load_dotenv("config.env")

#Setup the API key for Gemini
genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Setup email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # TLS port
SENDER_EMAIL = 'nihar.kodkani@gmail.com'
SENDER_PASSWORD = os.environ["APP_PASS"]  # Or app password if 2FA is enabled

print(SENDER_PASSWORD)

TO_EMAIL = 'niharkodkanibusiness@gmail.com'
BCC_EMAIL = 'nkodkani@purdue.edu'  # BCC recipient
SUBJECT = 'Sent using python'
BODY_TEXT = 'This is a simple text email sent from Python!'


msg = MIMEText(BODY_TEXT, 'plain')  # 'plain' for a simple text email
msg['From'] = SENDER_EMAIL
msg['To'] = TO_EMAIL
msg['Bcc'] = BCC_EMAIL
msg['Subject'] = SUBJECT

# Send the email
try:
    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Use the app password here
        server.send_message(msg)  # Send the message
        print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
    
# Access the API key
#api_key = os.getenv("GEMINI_KEY")

#response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)


