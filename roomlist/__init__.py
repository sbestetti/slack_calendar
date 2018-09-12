from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():    
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    now = datetime.datetime.utcnow().isoformat() + 'Z'    
    events_result = service.events().list(calendarId='distilled.ie_3735313434313434393930@resource.calendar.google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    for event in events:
        print(event['summary'])
    return events