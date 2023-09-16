import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# URL to check
url = "http://192.168.1.150:4201/"

# Email configuration
sender_email = "akram.prestacode@gmail.com"
sender_password = "quuuvrqzclbthrao"
receiver_email = "akrambensalem001@gmail.com"
email_sender_name = "PRESTACODE IT"  # Email sender name

# Twilio configuration
twilio_account_sid = 'ACd937baaedc0bec20506b377fa01130c1'
twilio_auth_token = '32fc3e0f3a031088f5b988db2e2fac2c'
twilio_phone_number = 'whatsapp:+14155238886'
recipient_whatsapp_number = 'whatsapp:+21625534432'
whatsapp_sender_name = "PRESTACODE IT"  # WhatsApp sender name


def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = f"{email_sender_name} <{sender_email}>"
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email notification sent successfully.")
    except Exception as e:
        print("Error sending email notification:", str(e))


def send_whatsapp_message(message_body):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        from_=twilio_phone_number,
        body=message_body,
        to=recipient_whatsapp_number
    )
    print(f"WhatsApp message sent with SID: {message.sid}")


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is up and running.")
        else:
            print("Website is down. Sending email notification and WhatsApp message.")
            send_email("Website Down", "The server is down.")
            send_whatsapp_message(
                f"{whatsapp_sender_name}: Website is down. Please check it.")
    except requests.ConnectionError:
        print("Website is down. Sending email notification and WhatsApp message.")
        send_email(
            "Prolegal Down", "The server of Achraf. so please call IT team (Akram ben salem) to fix it and thanx")
        send_whatsapp_message(
            f"{whatsapp_sender_name}: Prolegal Down. The server of Achraf. so please call IT team (Akram ben salem) to fix it and thanx.")


if __name__ == "__main__":
    check_website(url)
