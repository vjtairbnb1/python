import os
from twilio.rest import Client
import data as d


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ[d.twilio_auth['user']]
auth_token = os.environ[d.twilio_auth['pass']]
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=d.messaging_data['twilio_phone'],
                     to='+19417250447'
                 )

print(message.sid)