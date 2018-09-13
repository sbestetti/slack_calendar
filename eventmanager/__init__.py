import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import room

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def get_service():
    """
    Authenticates against Google API with the JSON credentials
    and return a service
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service

def check_if_free(rooms):
    """
    Receives a list of rooms and check the start time
    of the next event on each. Then it returns a list
    containing only the rooms that are free for the given time
    in minutes
    """
    service = get_service()    
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    time_to_check = 15 # Change this to a variable later
    free_rooms = []
    for item in rooms:
        events_result = service.events().list(
            calendarId=item.id,
            timeMin=now,
            maxResults=1,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        event = events[0]        
        year = int(event['start'].get('dateTime')[:4])
        month = int(event['start'].get('dateTime')[5:7])
        day = int(event['start'].get('dateTime')[8:10])
        hour = int(event['start'].get('dateTime')[11:13])
        minute = int(event['start'].get('dateTime')[14:16])
        event_time = datetime.datetime(year, month, day, hour, minute)
        time_delta = event_time - datetime.datetime.now()        
        if time_delta > datetime.timedelta(minutes=time_to_check):
            free_rooms.append(item)    
    
    return free_rooms