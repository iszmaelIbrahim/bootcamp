
import twilio
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# account_sid = os.environ['AC0e734015c6d217cbde2f7cb3b749a670']
# auth_token = os.environ['312beff834e6dfb101e11758c6812b88']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+18454201095',
                              to='+60134457029'
                          )

print(message.sid)


