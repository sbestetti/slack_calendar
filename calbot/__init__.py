from flask import Flask, json, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
import sys
from roomlist import main

def create_app():
    
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def index():                
        main()
        slack_buttons = '{"text": "What can I do for you?","attachments": [{"text": "Get me a free room right now in","fallback": "Something went wrong :(","callback_id": "free_rooms","color": "#3AA3E3","attachment_type": "default","actions": [{"name": "free_rooms","text": "Dublin","type": "button","value": "dub"},{"name": "free_rooms","text": "Wexford","type": "button","value": "wex"}]}]}'
        response = app.response_class(
            response=slack_buttons,
            status=202,
            mimetype='application/json'
        )
        return response

    @app.route('/response_manager', methods=['POST'])
    def freerooms():
        form_json = json.loads(request.form['payload'])
        selection = form_json['actions'][0]['value']
        print(selection)
        response_json = '{"text": "' + selection + '"}'
        response = app.response_class(
            response=response_json,
            status=200,
            mimetype='application/json'
        )        
        return response
    
    @app.route('/status')
    def test():
        return 'App running', 200

    return app