from flask import Flask, json, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
import sys
from . import roommanager, eventmanager, room

def create_app():
    
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def index():
        """Responds to the initial query creating the form on Slack"""
        slack_buttons = '{"text": "What can I do for you?","attachments": [{"text": "Get me a free room right now in","fallback": "Something went wrong :(","callback_id": "free_rooms","color": "#3AA3E3","attachment_type": "default","actions": [{"name": "free_rooms","text": "Dublin","type": "button","value": "dub"},{"name": "free_rooms","text": "Wexford","type": "button","value": "wex"}]}]}'
        response = app.response_class(
            response=slack_buttons,
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route('/response_manager', methods=['POST'])
    def freerooms():
        """Receives and manages the response from the form"""
        form_json = json.loads(request.form['payload'])
        selection = form_json['actions'][0]['value']        
        rooms_to_check = roommanager.get_rooms(selection)
        free_rooms = eventmanager.check_if_free(rooms_to_check)
        print('These rooms are free for the next 15 minutes: ')
        for item in free_rooms:
            print(item)                        
        response_json = '{"text": "' + selection + '"}'
        response = app.response_class(
            response=response_json,
            status=200,
            mimetype='application/json'
        )        
        return response    

    @app.route('/update_rooms', methods=['POST'])
    def update_rooms():
        """Receives a JSON payload with the list of available rooms"""
        payload = request.get_json()
        roommanager.update_list(payload)
        message = 'Update succesfull! Room list now contains {} rooms'.format(str(len(roommanager.list_of_rooms)))
        response = app.response_class(
            response=message,
            status=201
        )        
        return response

    return app