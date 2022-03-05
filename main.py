import discord
import time, datetime
import config, logging
import utilities
from twilio.rest import Client

def process_gateway_dispatch(event):
    try:
        if "channel_id" in event["d"]:
            if event['d']['channel_id'] in config.monitored_channels_ids and \
                "author" in event['d'] and "content" in event["d"]:

                    valid_notification = False

                    # Case for when authors and keywords given
                    if len(config.monitored_authors_ids) > 0 and len(config.target_keywords) > 0:
                        valid_notification = event['d']['author']['id'] in config.monitored_authors_ids and any(keyword in event['d']['content'] for keyword in config.target_keywords)

                    # Case for when only authors are given
                    elif len(config.monitored_authors_ids) > 0:                        
                        valid_notification = event['d']['author']['id'] in config.monitored_authors_ids
                    
                    # Case for when only keywords are given
                    elif len(config.target_keywords) > 0:
                        valid_notification = any(keyword in event['d']['content'] for keyword in config.target_keywords)

                    # Case for when no keywords or authors are given
                    else:
                        valid_notification = True

                    if valid_notification:
                        utilities.print_and_log(f"{datetime.datetime.now()} - {event['d']['author']['username']}: {event['d']['content']}", logging.INFO, True)
                        # Initiate phone call (default message left as not meant to be answered)
                        client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to=config.destination_number,
                            from_=config.twilio_number,
                        )
                        utilities.print_and_log(f"{datetime.datetime.now()} - Initiated phone call to {config.destination_number}", logging.INFO, True)

    except Exception as error:
        print(f"{datetime.datetime.now()} - Gateway Error: {error}")
        logging.exception("Gateway Error")
        pass

# Set-up Logger
log_file = f"logs/{datetime.date.today()}.log"
logging.basicConfig(level=logging.INFO, filename=log_file, encoding="UTF-8", force=True,
    datefmt="%Y-%m-%d %H:%M:%S", format="%(asctime)s - %(levelname)s in %(name)s: %(message)s")
logging.info("PROGRAM RESTARTED")

account_sid = config.twilio_account_SID
auth_token  = config.twilio_auth_token
client = Client(account_sid, auth_token)

# Start gateway socket as long as it shut downs (handle disconnects)
while True:
    try:
        discord.initialize_gateway_connection(process_gateway_dispatch)
    except:
        utilities.print_and_log("Socket Connection Lost, Re-Attempting in 1 Second.",
            logging.WARNING, False)
    finally:
        time.sleep(1)