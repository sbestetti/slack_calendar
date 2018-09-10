from flask import Flask, json, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict

def create_app():
    
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def index():
        user_id = request.form['user_id'].strip()
        user_name = request.form['user_name'].strip()
        text = request.form['text'].strip()
        channel_name = request.form['channel_name'].strip()
        channel_id = request.form['channel_id'].strip()
        response_to_send = "User {} ({}) posted '{}' on channel {} ({})".format(user_name, user_id, text, channel_name, channel_id)
        return response_to_send, 202

    @app.route('/status')
    def test():
        return 'App running', 200

    return app