#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# Before-request hook to store the app path in g
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# Main route
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name

    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200  # or use 202, 204, etc. if needed
    headers = {
        'Content-Type': 'text/html'
    }

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

