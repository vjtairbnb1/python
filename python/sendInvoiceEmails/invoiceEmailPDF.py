# ------------ Import ------------ # 
from pdf_mail import sendpdf
from datetime import datetime
# import datetime
from dateutil.relativedelta import relativedelta
import getpass
from contact_info import clientList, get_invoice_year


# ------------ Build variables ------------ #

    # date variables
now = datetime.now()
currentYear = format(now, '%Y')
prevYear = format(now - relativedelta(years=1), '%Y')
currentMonth = format(now, '%B')
prevMonth = format(now - relativedelta(months=1), '%B')

    # other
senderPass = getpass.getpass()



# ------------ Build sendEmail fn() w/ email information ------------ #
def sendEmail(receiverEmail, firstName, fileName, filePath): 
    alertMessage = "If you have any questions/concerns, please contact Vincent Troyer at vjt.airbnb@gmail.com or 941-725-0447. Thank you.\n\n"

    body = (f"Hi {firstName},\n\n"
        f"Attached to this email is a copy of your invoice for the month of {prevMonth}. Thank you for choosing us for your AirBnB management needs!\n\n"
        f"Please Note: This is an automated message. Please do not respond to this email and/or email address.\n\n"
        f"{alertMessage}\n"
        f"Vincent Troyer\n"
        f"Frontdoor Management\n"
        f"vjt.airbnb@gmail.com || 941-725-0447")

    sender = "vjt.airbnb.billing@gmail.com"
    subject = f"Vincent Troyer - {prevMonth} Invoice"


    # ------------ Build email ------------ #
    email = sendpdf(sender, receiverEmail, senderPass, subject, body, filePath, fileName)

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
# sendEmail("vjt.airbnb@gmail.com", 'Leah', clientList["leahBontrager"]['filePath'], f"Leah Bontrager {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Lavon', clientList["lavonYoder"]['filePath'], f"Lavon Yoder {prevMonth} {get_invoice_year()}")
sendEmail("vjt.airbnb@gmail.com", 'Daryl', clientList["darylStoltzfus"]['filePath'], f"Daryl Stoltzfus {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Scott', clientList["scottYoder"]['filePath'], f"Scott Yoder {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Kate', clientList["kateYoder"]['filePath'], f"Kate Yoder {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Leon', clientList["leonTroyer"]['filePath'], f"Leon Troyer {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Jesse', clientList["jesseMiller"]['filePath'], f"Jesse Miller {prevMonth} {get_invoice_year()}")
# sendEmail("vjt.airbnb@gmail.com", 'Firman', clientList["firmanMiller"]['filePath'], f"Firman Miller {prevMonth} {get_invoice_year()}")


# ------------ Send Email List ------------ #
# sendEmail(clientList['leahBontrager']['email'], 'Leah', clientList["leahBontrager"]['filePath'], f"Leah Bontrager {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['lavonYoder']['email'], 'Lavon', clientList["lavonYoder"]['filePath'], f"Lavon Yoder {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['darylStoltzfus']['email'], 'Daryl', clientList["darylStoltzfus"]['filePath'], f"dStoltzfus {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['scottYoder']['email'], 'Scott', clientList["scottYoder"]['filePath'], f"Scott Yoder {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['kateYoder']['email'], 'Kate', clientList["kateYoder"]['filePath'], f"Kate Yoder {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['leonTroyer']['email'], 'Leon', clientList["leonTroyer"]['filePath'], f"Leon Troyer {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['jesseMiller']['email'], 'Jesse', clientList["jesseMiller"]['filePath'], f"Jesse Miller {prevMonth} {get_invoice_year()}")
# sendEmail(clientList['firmanMiller']['email'], 'Firman', clientList["firmanMiller"]['filePath'], f"Firman Miller {prevMonth} {get_invoice_year()}")

# ------------ REMEMBER THAT THE MONTH IN THE EMAIL IS THE PREVIOUS MONTH RELATIVE TO THE CURRENT DATE (ex: It is the month of February. Your email will include Jan invoice ) ------------