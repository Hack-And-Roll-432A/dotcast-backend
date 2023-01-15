from flask import Flask, redirect, request, render_template, url_for, jsonify
import requests
from auth import startup
import json

app = Flask(__name__)

@app.route('/mrt_data')
def read_mrt_st():
    with open('data/mrt.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)
        
@app.route('/')
def index():
    return "<h1> /mrt_data, /authenticate </h1>"

@app.route('/authenticate')
def auth():
    response = startup.getUser(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])
    return redirect(response)

@app.route('/callback/')
def callback():
    startup.getUserToken(request.args['code'])
    # [ACCESS_TOKEN, AUTHENTICATION_HEADER, AUTHORIZED_SCOPES, EXPIRATION]
    acc_token = dict({"token": startup.getAccessToken()[0]}) 
    return jsonify(acc_token)


if __name__ == '__main__':
    app.config.from_file("auth/config.json", load=json.load)
    app.run(port=8081, debug=True)
