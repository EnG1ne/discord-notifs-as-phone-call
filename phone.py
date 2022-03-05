import config
from twilio.rest import Client

account_sid = config.twilio_account_SID
auth_token  = config.twilio_auth_token
client = Client(account_sid, auth_token)

call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=config.destination_number,
            from_=config.twilio_number,
        )
