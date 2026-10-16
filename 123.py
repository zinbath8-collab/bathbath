import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(sender_email, sender_password, receiver_email, subject, body, smtp_server='smtp.gmail.com', port=587):
    # Create the email
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Attach the body as HTML (allows for links)
    html_content = f"""
    <html>1
    <body>
        <p>Dear User,</p>
        <p>Your account has been flagged for suspicious activity. Click below to verify immediately:</p>
        <p><a href="http://fake-login-portal.com/verify.php">Click Here to Verify</a></p>
        <p>Failure to act will result in account suspension.</p>
        <p>Regards,<br>Security Team</p>
    </body>
    </html>
    """
    
    part = MIMEText(html_content, "html")
    message.attach(part)

    # Create secure connection and send
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Phishing email sent successfully.")

# Usage Example
if __name__ == "__main__":
    send_phishing_email(
        sender_email="your_email@gmail.com",
        sender_password="your_app_password",
        receiver_email="target@example.com",
        subject="URGENT: Account Verification Required",
        body="Verify now to avoid suspension."
    )