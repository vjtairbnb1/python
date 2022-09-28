# ------------ Import ------------ # 
from datetime import datetime
import datetime
import getpass
import contact_info as c
import functions as f


# ------------ Build variables ------------ #
sender_email = c.myContactInfo['vinceTroyer']['billingEmail']
sender_pass = getpass.getpass()
# ----------------------------------------- #

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
f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["leahBontrager"]["firstName"], "lBontrager")
# f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["lavonYoder"]["firstName"], "lYoder")
# f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["darylStoltzfus"]["firstName"], "dStoltzfus")
f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["scottYoder"]["firstName"], "sYoder")
f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["kateYoder"]["firstName"], "kYoder")
# f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["jesseMiller"]["firstName"], "jMiller")
f.send_email(sender_email, sender_pass, "vjt.airbnb@gmail.com", c.clientList["firmanMiller"]["firstName"], "fMiller")


# ------------ Send Email List ------------ #
# f.send_email(sender_email, sender_pass, c.clientList["leahBontrager"]["email"], c.clientList["leahBontrager"]["firstName"], "lBontrager")
# f.send_email(sender_email, sender_pass, c.clientList["lavonYoder"]["email"], c.clientList["lavonYoder"]["firstName"], "lYoder")
# f.send_email(sender_email, sender_pass, c.clientList["darylStoltzfus"]["email"], c.clientList["darylStoltzfus"]["firstName"], "dStoltzfus")
# f.send_email(sender_email, sender_pass, c.clientList["scottYoder"]["email"], c.clientList["scottYoder"]["firstName"], "sYoder")
# f.send_email(sender_email, sender_pass, c.clientList["kateYoder"]["email"], c.clientList["kateYoder"]["firstName"], "kYoder")
# f.send_email(sender_email, sender_pass, c.clientList["jesseMiller"]["email"], c.clientList["jesseMiller"]["firstName"], "jMiller")
# f.send_email(sender_email, sender_pass, c.clientList["firmanMiller"]["email"], c.clientList["firmanMiller"]["firstName"], "fMiller")

# ------------ REMEMBER THAT THE MONTH IN THE EMAIL IS THE PREVIOUS MONTH RELATIVE TO THE CURRENT DATE (ex: January's invoice will be sent in February) ------------