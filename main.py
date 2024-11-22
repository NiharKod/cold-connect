import os
from dotenv import load_dotenv
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
import pandas as pd


# Load environment variables from .env file
load_dotenv("config.env")

# Load the data
df = pd.read_csv("startups.csv")


file = open("email_body.txt", "r")
body = file.read()
file.close()

file = open("out.txt", "w")
#Setup the API key for Gemini
genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

email_list = []
for (index, row) in df.iterrows():
    email_list.append((row["Name"], row["Email"], body + model.generate_content("I am writing an email to " + row["Name"] + " about wanting to intern at the company. Please write 1 or 2 sentences which I can add in my email about why working at the following company would be interesting. Please do not provide me any options. Just go with any Ue the given description :" + row["Description"]).text + "\nThank you so much, I look forward to hearing back.\n Best, Nihar Kodkani\n"))
    email_list[index][2].replace(">", " ")
    file.write(email_list[index][2])
    
# Send the emails
    



# Setup email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # TLS port
SENDER_EMAIL = 'nihar.kodkani@gmail.com'
SENDER_PASSWORD = os.environ["APP_PASS"]  # Or app password if 2FA is enabled


TO_EMAIL = 'yolinac315@cpaurl.com'
BCC_EMAIL = 'nkodkani@purdue.edu'  # BCC recipient
SUBJECT = 'Sent using python'




msg = MIMEText(BODY_TEXT, 'plain')  # 'plain' for a simple text email
msg['From'] = SENDER_EMAIL
msg['To'] = TO_EMAIL
# msg['Bcc'] = BCC_EMAIL
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


