from flask import Flask, json, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
import sys
from . import roommanager, eventmanager, room, responsebuilder
import threading

def create_app():
    
    app = Flask(__name__)
    roommanager.update_list()

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
        response_address = form_json['response_url']        
        responseThread = threading.Thread(target=responsebuilder.respond_to_query, args=[selection, response_address])
        responseThread.start()        
        return 'Checking...', 200
        
    return app