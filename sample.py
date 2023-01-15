#https://github.com/Anirudh181001/Web-Dev-With-Flask
from flask import Flask, redirect, request, render_template, url_for
import sqlite3

# creates an object of the Flask class
# __name__ -> all the files it requires are in this directory
app = Flask(__name__)
USERNAME=''

# at first, our application does not know what to do when the browser asks for a path, e.g. /
# by defining @app.route('PATH'), we tell the server what to return
@app.route('/')
def home():
    if not USERNAME:
        return redirect(url_for('login'))

    with sqlite3.connect('./dataset.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT name, description, num_in_stock, image_url FROM Stocks')
        stocks = cur.fetchall()
    return render_template('home.html', username=USERNAME, stocks=stocks)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    password = request.form['password']
    with sqlite3.connect('./dataset.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT id, username FROM Users WHERE email='{email}' AND password='{password}'")
        user_info = cur.fetchone()
        if not user_info:
            return render_template('login.html')
        global USERNAME
        USERNAME = user_info[1]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
