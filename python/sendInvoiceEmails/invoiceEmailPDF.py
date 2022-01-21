# ------------ Import ------------ # 
from pdf_mail import sendpdf 
from datetime import datetime
import datetime
import getpass
from contact_info import myContactInfo, clientList


# ------------ Build variables ------------ #
senderPass = getpass.getpass()

today = datetime.date.today()
first = today.replace(day=1)
lastMonth = (first - datetime.timedelta(days=1)).strftime("%B")


# ------------ Build sendEmail fn() w/ email information ------------ #
def sendEmail(receiverEmail, firstName, fileName): 
    alertMessage = "If you have any questions/concerns, please contact Vincent Troyer at vjt.airbnb@gmail.com or 941-725-0447. Thank you."
    starString = "*" * (len(alertMessage) * 2)

    body = (f"Hi {firstName},\n\n"
        f"Attached to this email is a copy of your invoice for the month of {lastMonth}. Thank you for choosing us for your AirBnB management needs!\n\n"
        f"{starString}\n"
        f"Please Note: This is an automated message. Please do not respond to this email and/or email address. "
        f"If you have any questions/concerns, please contact Vincent Troyer at vjt.airbnb@gmail.com or 941-725-0447. Thank you.\n"
        f"{starString}\n\n"
        f"Vincent Troyer\n"
        f"BackDoor Solutions\n"
        f"vjt.airbnb@gmail.com || 941-725-0447")

    sender = "vjt.airbnb.billing@gmail.com"
    subject = f"Vincent Troyer -- {lastMonth} Invoice"
    filePath = "C:/Users/vince/Documents/Code_Projects/Python/backdoor_solutions/sendInvoiceEmails/invoice_pdfs"


    # ------------ Build email ------------ #
    email = sendpdf(sender, receiverEmail, senderPass, subject, body, fileName, filePath)

    # ------------ Send ------------ #
    email.email_send()


# ------------ Test Send to Myself ------------ #
verify = input(f"🚨 You are about to send many emails. 🚨 Proceed? (y/n) ")

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

sendEmail("vjt.airbnb@gmail.com", clientList["firmanMiller"]["firstName"], "fMiller")
sendEmail("vjt.airbnb@gmail.com", clientList["jesseMiller"]["firstName"], "jMiller")
sendEmail("vjt.airbnb@gmail.com", clientList["lavonYoder"]["firstName"], "lYoder")
sendEmail("vjt.airbnb@gmail.com", clientList["leonTroyer"]["firstName"], "lTroyer")
sendEmail("vjt.airbnb@gmail.com", clientList["jonasHochstetler"]["firstName"], "lTroyer")

# pending accounts
# sendEmail("vjt.airbnb@gmail.com", clientList["lloydWittmer"]["firstName"], "lWittmer")
# sendEmail("vjt.airbnb@gmail.com", clientList["scottYoder"]["firstName"], "sYoder")

# ------------ Send Email List ------------ #
sendEmail(clientList["firmanMiller"]["email"], clientList["firmanMiller"]["firstName"], "fMiller")
sendEmail(clientList["jesseMiller"]["email"], clientList["jesseMiller"]["firstName"], "jMiller")
sendEmail(clientList["lavonYoder"]["email"], clientList["lavonYoder"]["firstName"], "lYoder")
sendEmail(clientList["leonTroyer"]["email"], clientList["leonTroyer"]["firstName"], "lTroyer")
sendEmail(clientList["jonasHochstetler"]["email"], clientList["jonasHochstetler"]["firstName"], "lTroyer")

# ------------ REMEMBER THAT THE MONTH IN THE EMAIL IS THE PREVIOUS MONTH RELATIVE TO THE CURRENT DATE------------ 
