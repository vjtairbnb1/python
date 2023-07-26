# import
from datetime import datetime
from dateutil.relativedelta import relativedelta

#define time variables
now = datetime.now()
currentMonth = format(now, '%B')
currentYear = format(now, '%Y')
prevYear = format(now - relativedelta(years=1), '%Y')

# define functions
def get_invoice_year():
    if currentMonth == 'December':
        return prevYear
    else:
        return currentYear
        

# start dictionaries
myContactInfo = {
    'vinceTroyer': {
        'firstName': 'Vincent',
        'lastName': 'Troyer',
        'email': 'vjt.airbnb@gmail.com',
        'phone': '9417250447',
        'address': '2212 Vintage St, Sarasota, FL 34240'
    }
}

clientList = {
    'darylStoltzfus': {
        'firstName': 'Daryl',
        'lastName': 'Stoltzfus',
        'email': 'daryl1969@yahoo.com',
        'phone': '7173721822',
        'billingAddress': '15072 Lurgan Rd, Orrstown, PA 17244',
        'propertyAddress': '926 Rhodes Ave, Sarasota, FL 34237',
        'filePath': f'G:/My Drive/Sent Invoices/Daryl Stoltzfus/{get_invoice_year()}'
    },
    'firmanMiller': {
        'firstName': 'Firman',
        'lastName': 'Miller',
        'email': 'cf2@emyprinter.net',
        'phone': '3306744505',
        'billingAddress': '5440 Township Rd 618, Millersburg, OH 44654',
        'propertyAddress': '1020 S Conrad Ave, Sarasota, FL 34237',
        'filePath': f'G:/My Drive/Sent Invoices/Firman Miller/{get_invoice_year()}'
    },
    'jesseMiller': {
        'firstName': 'Jesse',
        'lastName': 'Miller',
        'email': 'jesse@thinkinkllc.com',
        'phone': '3302432511',
        'billingAddress': '8057 OH-241, Millersburg, OH 44654',
        'propertyAddress': '972 Pattison Ave, Sarasota, FL 34237',
        'filePath': f'G:/My Drive/Sent Invoices/Jesse Miller/{get_invoice_year()}'
    },
    'kateYoder': {
        'firstName': 'Kate',
        'lastName': 'Yoder',
        'email': "1yodergirl@gmail.com",
        'phone': '2693394530',
        'billingAddress': '806 Ponder Ave, Sarasota, FL 34232',
        'propertyAddress': '5071 Houle Pl, Sarasota, FL 34232',
        'filePath': f'G:/My Drive/Sent Invoices/Kate Yoder/{get_invoice_year()}'
    },
    'lavonYoder': {
        'firstName': 'Lavon',
        'lastName': 'Yoder',
        'email': 'leyoder02@gmail.com',
        'phone': '5743044587',
        'billingAddress': '6035 W 600 N, Shipshewana, IN 46565',
        'propertyAddress': '229 E Cornelius Cir, Sarasota, FL 34232',
        'filePath': f'G:/My Drive/Sent Invoices/Lavon Yoder/{get_invoice_year()}'
    },
    'leahBontrager': {
        'firstName': 'Leah',
        'lastName': 'Bontrager',
        'email': 'warrenridge22@gmail.com',
        'phone': '2696255530',
        'billingAddress': '1165 Mendon Rd, Sherwood, MI 49089',
        'propertyAddress': '3727 Warren Ridge St, Sarasota, FL 34233',
        'filePath': f'G:/My Drive/Sent Invoices/Leah Bontrager/{get_invoice_year()}'
    },
    'leonTroyer': {
        'firstName': 'Leon',
        'lastName': 'Troyer',
        'email': 'leon3433@yahoo.com',
        'phone': '3304643433',
        'billingAddress': '15258 Durstine Rd, Dundee, OH 44624',
        'propertyAddress': '1201 Oak View Dr, Sarasota, FL 34232',
        'filePath': f'G:/My Drive/Sent Invoices/Leon Troyer/{get_invoice_year()}'
    },
    'scottYoder': {
        'firstName': 'Scott',
        'lastName': 'Yoder',
        'email': 'coastaltrees21@gmail.com',
        'phone': '2698326643',
        'billingAddress': '806 Ponder Ave, Sarasota, FL 34232',
        'propertyAddress': '5150 Island Date St, Sarasota, FL 34232',
        'filePath': f'G:/My Drive/Sent Invoices/Scott Yoder/{get_invoice_year()}'
    }
}