from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from models.request_dtos import EmailRequest
from app.settings import get_settings


def send_email(email_request: EmailRequest):
    settings = get_settings()

    sender = "davipotamus@gmail.com"
    receivers = [email_request.to, email_request.cc]
    subject = email_request.subject
    body = email_request.body

    msg = MIMEMultipart("alternative")
    msg["From"] = f"From Person <{sender}>"
    msg["To"] = ", ".join(
        email_request.to if isinstance(email_request.to, list) else [email_request.to]
    )
    if email_request.cc:
        msg["Cc"] = ", ".join(
            email_request.cc
            if isinstance(email_request.cc, list)
            else [email_request.cc]
        )

    msg["Subject"] = subject

    html = f"""\
    <html>
    <head></head>
    <body>
        <p>Variable value: {body}</p>
    </body>
    </html>
    """

    part2 = MIMEText(html, "html")
    msg.attach(part2)

    # utilizing "aiosmtpd -n" for local dev
    smtpObj = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    smtpObj.sendmail(sender, receivers, msg.as_string())
