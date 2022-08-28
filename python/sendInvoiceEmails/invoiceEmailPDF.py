# ------------ Import ------------ # 
from pdf_mail import sendpdf 
from datetime import datetime
import datetime
import getpass
from contact_info import clientList


# ------------ Build variables ------------ #
senderPass = getpass.getpass()

today = datetime.date.today()
first = today.replace(day=1)
lastMonth = (first - datetime.timedelta(days=25)).strftime("%B")


# ------------ Build sendEmail fn() w/ email information ------------ #
def sendEmail(receiverEmail, firstName, fileName): 
    alertMessage = "If you have any questions/concerns, please contact Vincent Troyer at vjt.airbnb@gmail.com or 941-725-0447. Thank you."

    body = (f"Hi {firstName},\n\n"
        f"Attached to this email is a copy of your invoice for the month of {lastMonth}. Thank you for choosing us for your AirBnB management needs!\n\n"
        f"Please Note: This is an automated message. Please do not respond to this email and/or email address. "
        f"{alertMessage}\n"
        f"Vincent Troyer\n"
        f"FrontDoor Solutions\n"
        f"vjt.airbnb@gmail.com || 941-725-0447")

    sender = "vjt.airbnb.billing@gmail.com"
    subject = f"Vincent Troyer -- {lastMonth} Invoice"
    filePath = "C:/Users/vince/Documents/GitHub/front-door-solutions/functions/Python/sendInvoiceEmails/invoice_pdfs"


    # ------------ Build email ------------ #
    email = sendpdf(sender, receiverEmail, senderPass, subject, body, fileName, filePath)

    # ------------ Send ------------ #
    email.email_send()

# ------------ Verify Statements to Ask Permission ------------ #
verify = str(input(f"🚨 You are about to send many emails. 🚨 Proceed? (y/n) "))

if verify == "y" or verify == "Y":
    # ------------ Send email ------------ #
    pass
elif verify == "n" or verify == "N":
    print(f"🚨 Email send terminated. 🚨\n")
else:
    while verify != "y" or verify != "n":
        verify = input(f"🚨 You are about to send many emails. 🚨 Proceed? (y/n) ")
        if verify == "y":
            # ------------ Send email ------------ #
            pass
        elif verify == "n":
            print(f"🚨 Email send terminated. 🚨\n")
            break
        else:
            continue

# ------------ Test Send to Myself ------------ #
sendEmail("vjt.airbnb@gmail.com", clientList["firmanMiller"]["firstName"], "fMiller")
sendEmail("vjt.airbnb@gmail.com", clientList["darylStoltzfus"]["firstName"], "dStoltzfus")
sendEmail("vjt.airbnb@gmail.com", clientList["jesseMiller"]["firstName"], "jMiller")
# sendEmail("vjt.airbnb@gmail.com", clientList["lavonYoder"]["firstName"], "lYoder")
sendEmail("vjt.airbnb@gmail.com", clientList["scottYoder"]["firstName"], "sYoder")
sendEmail("vjt.airbnb@gmail.com", clientList["leahBontrager"]["firstName"], "lBontrager")
sendEmail("vjt.airbnb@gmail.com", clientList["kateYoder"]["firstName"], "kYoder")


# ------------ Send Email List ------------ #
# sendEmail(clientList["leahBontrager"]["email"], clientList["leahBontrager"]["firstName"], "lBontrager")
# # sendEmail(clientList["lavonYoder"]["email"], clientList["lavonYoder"]["firstName"], "lYoder")
# # sendEmail(clientList["darylStoltzfus"]["email"], clientList["darylStoltzfus"]["firstName"], "dStoltzfus")
# sendEmail(clientList["scottYoder"]["email"], clientList["scottYoder"]["firstName"], "sYoder")
# sendEmail(clientList["kateYoder"]["email"], clientList["kateYoder"]["firstName"], "kYoder")
# # sendEmail(clientList["jesseMiller"]["email"], clientList["jesseMiller"]["firstName"], "jMiller")
# sendEmail(clientList["firmanMiller"]["email"], clientList["firmanMiller"]["firstName"], "fMiller")

# ------------ REMEMBER THAT THE MONTH IN THE EMAIL IS THE PREVIOUS MONTH RELATIVE TO THE CURRENT DATE (ex: January's invoice will be sent in February) ------------