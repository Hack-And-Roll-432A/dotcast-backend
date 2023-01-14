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
    response = startup.getUser(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])
    return redirect(response)

@app.route('/callback/')
def home():
    startup.getUserToken(request.args['code'])
    acc_token = startup.getAccessToken()[1]
    # print("\n ===== acc_token:")
    # print(acc_token)
    headers = {"Content-Type" : 'application/json', "Accept" : 'application/json'}
    headers.update(acc_token)
    # print("\n ===== headers:")
    # print(headers)
    post = requests.get("https://api.spotify.com/v1/me",headers=headers)
    print(post.text)
    return post.text


if __name__ == '__main__':
    app.config.from_file("auth/config.json", load=json.load)
    app.run(port=8081, debug=True)
