from flask import Flask, jsonify
import uuid

app = Flask(__name__)


@app.route('/ping')
def ping():

    return jsonify({'ping': 'pong'})


@app.route('/')
def home():

    return jsonify({'routes': ['/ping', '/create', '/read', '/update', '/delete']})


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=9000)
