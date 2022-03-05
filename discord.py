import time, datetime, logging
import websocket, json
import threading
import config, utilities

logger = logging.getLogger()

def send_json_request(ws, request):
    ws.send(json.dumps(request))


def receive_json_response(ws):
    response = ws.recv()

    if response:
        return json.loads(response)


def heartbeat(interval, ws):
    try:        
        while ws.connected:
            time.sleep(interval)
            heartbeatJSON = {
                "op": 1,
                "d": "null"
            }
            # Aditional verification before sending heartbeat
            if ws.connected:
                send_json_request(ws, heartbeatJSON)

        utilities.print_and_log("Heartbeat Interrupted", logging.WARNING, False)

    except Exception as error:
        print(f"{datetime.datetime.now()} - Heartbeat Error has Occured: {error}")
        logger.exception("Heartbeat Error has Occured")


def initialize_gateway_connection(response_fct):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encording=json")

    event = receive_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 800
    
    # Only start new heartbeat thread if last one has stopped running
    # due to ridiculously bad timing where it sent while re-connecting
    threading.Thread(target=heartbeat, args=(heartbeat_interval, ws)).start()

    payload = {
        "op": 2,
        "d": {
            "token": config.token,
            "properties": {
                "$os": "windows",
                "$browser": "firefox",
                "$device": "pc"
            }
        }
    }

    send_json_request(ws, payload)
    
    utilities.print_and_log("Connected and Identified to the Gateway!", logging.INFO, False)

    print(f"{datetime.datetime.now()} - Listening for new messages...")
    
    while True:
        event = receive_json_response(ws)
        
        if event is not None:
            op_code = event['op']
        
            if op_code == 11:
                utilities.print_and_log("Heartbeat Received!", logging.INFO, False)
            elif op_code == 7 or op_code == 9:
                utilities.print_and_log("Session Invalidated, Re-Connection Needed", logging.WARNING, False)
                break
            elif op_code == 0:
                response_fct(event)