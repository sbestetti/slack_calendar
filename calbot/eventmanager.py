import os
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from . import room
from google.auth import app_engine
from google.oauth2 import service_account
# import googleapiclient

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(os.getcwd(), 'service.json')

def get_service():
    """
    Authenticates against Google API with the JSON credentials
    and return a service
    """
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials, cache_discovery=False)
    return service

def check_if_free(rooms):
    """
    Receives a list of rooms and check the start time
    of the next event on each. Then it returns a list
    containing only the rooms that are free for the given time
    in minutes
    """
    service = get_service()    
    minutes_to_check = 30    
    end_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes_to_check)    
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    end_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes_to_check)
    end_time_utc = end_time.isoformat() + 'Z'
    free_rooms = []
    for item in rooms:
        query_body = {"timeMin": now, "timeMax": end_time_utc, "timeZone": "Europe/Dublin", "items": [{"id": item.id}]}
        query_body['items'][0]['id'] = item.id
        response = service.freebusy().query(body=query_body).execute()
        if not response['calendars'][item.id].get('busy'):
            free_rooms.append(item)    
    return free_rooms