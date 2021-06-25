
import twilio
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# export TWILIO_ACCOUNT_SID='AC63742f61dcb3033a5d473d9b23d238cc'
# export TWILIO_AUTH_TOKEN='e52cce9ad83ed8e66efba8d1491e498a'
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hello world',
#                               from_='+12532378250',
#                               to='+60134457029'
#                           )

message = client.messages.create(
                              body="Hi AA, i'm ismail",
                              from_='+12532378250',
                              to='+60124290640'
                          )

# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         from_='+12532378250',
#                         to='+60169466484'
#                     )


print(message.sid)


