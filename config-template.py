# Twilio Params
twilio_account_SID = 'Your Twilio Account SID'
twilio_auth_token = 'Your Twilio Auth Token'
twilio_number = 'Your Twilio Number'
destination_number = 'Phone number to call with notification'

# Discord Params
# SEARCH PRIORITY: channel > author = keywords
token = 'Your Discord Token'
monitored_channels = ['List of channels to monitor for new messages']
# Optional - notifies only when a new message is sent by a specific user (within a monitored channel)
monitored_authors = ['List of authors to monitor for new messages']
# Optional - notifies only if a message contains a specific string (within a monitored channel)
target_keywords = ['List of keywords to monitor for in new messages']