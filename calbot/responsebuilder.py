from . import eventmanager, room, roommanager
import requests
import json

def respond_to_query(selection, response_address):
    rooms_to_check = roommanager.get_rooms(selection)
    free_rooms = eventmanager.check_if_free(rooms_to_check)
    if len(free_rooms) == 0:
        payload = {
            "text": "Sorry, no free rooms right now. :(",
            "attachments": [
                {
                    "text": "",                
                }
            ]
        }
    else:
        payload = {
            "text": "These rooms are free for the next 30 minutes:",
            "attachments": [
                {
                    "text": "",                
                }
            ]
        }
        for item in free_rooms:
            payload['attachments'][0]['text'] = payload['attachments'][0]['text'] + item.name + '\n'
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}    
    r = requests.post(response_address, data=json.dumps(payload), headers=headers)