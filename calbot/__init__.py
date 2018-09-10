from flask import Flask, json, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict

def create_app():
    
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def index():
        #How to get data from the Slack form:
        #user_id = request.form['user_id'].strip()
        #user_name = request.form['user_name'].strip()
        #text = request.form['text'].strip()
        #channel_name = request.form['channel_name'].strip()
        #channel_id = request.form['channel_id'].strip()
        #response_to_send = "User {} ({}) posted '{}' on channel {} ({})".format(user_name, user_id, text, channel_name, channel_id)        
        slack_buttons = '{"text": "What can I do for you?","attachments": [{"text": "Get me a free room right now in","fallback": "Something went wrong :(","callback_id": "free_rooms","color": "#3AA3E3","attachment_type": "default","actions": [{"name": "free_rooms","text": "Dublin","type": "button","value": "dub"},{"name": "free_rooms","text": "Wexford","type": "button","value": "wex"}]}]}'
        response = app.response_class(
            response=slack_buttons,
            status=202,
            mimetype='application/json'
        )
        return response

    @app.route('/status')
    def test():
        return 'App running', 200

    return app