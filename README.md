# G Suite calendar management app for Slack

Python/Flask app to do various tasks on G Suite calendar from Slack

- Implemented:
  - Find rooms that are free for the next 30 minutes
  
- Coming:
  - Find rooms that are free for a aount of time specified by the user
  - Book free rooms right from Slack
  - Check who has a room on a specific time
  
Check project page for tech work

Sample for list of rooms:
```
{
  "rooms": [
    {
      "name": "Room's display name",
      "address": "resource email address",
      "capacity": 3,
      "location": "Descriptive location",
      "office": "dub"
    },
  ]
}
```
