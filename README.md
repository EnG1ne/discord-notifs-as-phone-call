# Discord Message Notifications as Phone Call
Small Program that calls your phone when a new message has been sent on one or more chosen Discord channels.

This was made out of desperation for the terrible notification system that Discord has in place where you're lucky if an important notification actually gets sent to your phone. Also, it was made for use on important messages in channels that potentially required immediate attention.
 
How to Use:

1) Create an account on https://www.twilio.com/ and either buy a phone number or use their free trial.

2) Fill in the **config.py** file with the following fields

   Under Twilio Params
   1) _twilio_account_SID_ and _twilio_auth_token_ will both be found under the "Account Info" tab located on the first page when logging in Twilio
   2) _twilio_number_ is your new twilio number that you selected when purchasing or when activating your free trial
   3) _destination_number_ is the actual phone number you want twilio to call. If you want it to call your phone, then put your number.
        Don't froget to add a "+" followed by your region code for both these two numbers
   
   Under Discord Params
   1) _token_ is your account access token that can be optained via [various methods](https://www.followchain.org/find-discord-token/).
   2) _monitored_channels_ids_ is a list of all the channel ids you want this tool to listen on
   3) _monitored_authors_ids_ is an OPTIONAL list for all the user's ids that you want to get a notification for (only they are monitored)
   4) _target_keywords_ is an OPTIONAL list to only get a phone call when one of the keywords in this list is mentioned

  _monitored_authors_ids_ and _target_keywords_ can be used simultaneously to provide more accuracy in selecting who can trigger your phone to ring.
  
3) Compile (yes, this is necessary). 

That's about all I can think of.

Enjoy!
