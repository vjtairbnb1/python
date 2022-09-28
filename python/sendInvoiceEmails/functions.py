import pdf_mail as pdf
from datetime import datetime

import smtplib as smtp
import sys

def send_email(senderEmail, senderPass, receiverEmail, firstName, fileName):
    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = (first - datetime.timedelta(days=25)).strftime("%B")

    alertMessage = "If you have any questions/concerns, please contact Vincent Troyer at vjt.airbnb@gmail.com or 941-725-0447. Thank you."

    body = (f"Hi {firstName},\n\n"
        f"Attached to this email is a copy of your invoice for the month of {lastMonth}. Thank you for choosing us for your AirBnB management needs!\n\n"
        f"Please Note: This is an automated message. Please do not respond to this email and/or email address. "
        f"{alertMessage}\n"
        f"Vincent Troyer\n"
        f"FrontDoor Solutions\n"
        f"vjt.airbnb@gmail.com || 941-725-0447")

    subject = f"Vincent Troyer -- {lastMonth} Invoice"
    filePath = "C:/Users/vince/Documents/GitHub/front-door-solutions/functions/Python/sendInvoiceEmails/invoice_pdfs"


    # ------------ Build email ------------ #
    email = pdf.sendpdf(senderEmail, senderPass, receiverEmail, subject, body, fileName, filePath)

    # ------------ Send ------------ #
    email.email_send()

def send_text(email_auth, pass_auth, recipient_number: str):
    
    carriers = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@page.nextel.com"
    }

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_auth, pass_auth)

    final_number = recipient_number + carriers["verizon"]

    server.sendmail(email_auth, final_number, "test")


