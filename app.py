from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

import uuid

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "haadha ba3da ka5eer"

jwt = JWTManager(app)


@app.route('/ping')
@jwt_required()
def ping():

    return jsonify({'ping': 'pong'})


@app.route('/')
def home():

    return jsonify({'routes': ['/ping', '/login', '/create', '/read', '/update', '/delete']})


@app.route("/login", methods=["POST"])
def login():

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "altair" or password != "1234":

        return jsonify({"Error": "Incorrect "}), 401

    access_token = create_access_token(identity=username)

    return jsonify(access_token=access_token)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=9000)
