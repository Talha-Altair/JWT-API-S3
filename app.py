from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
import datetime
from connections import s3
import json
from settings import BUCKET_NAME

import uuid

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "haadha ba3da ka5eer"

jwt = JWTManager(app)

"""
{
    "uuid": "",
    "created_by": "",
    "created_time": "",
    "modified_by": "",
    "modified_time": "",
    "body": {

    }
}

"""


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


@app.route("/create", methods=["POST"])
@jwt_required()
def create():

    current_uuid = str(uuid.uuid4())

    current_user = get_jwt_identity()

    current_time = str(datetime.datetime.now())

    data = request.json

    result = {
        "uuid": current_uuid,
        "created_by": current_user,
        "created_time": current_time,
        "modified_by": current_user,
        "modified_time": current_time,
        "body": data
    }

    file_content = bytes(json.dumps(result), "utf-8")

    file_name = "file-" + current_uuid + ".json"

    s3.Bucket(BUCKET_NAME).put_object(Key=file_name, Body=file_content)

    return jsonify(result)


@app.route("/read", methods=["POST"])
@jwt_required()
def read():

    current_uuid = request.json.get("uuid", None)

    file_name = "file-" + current_uuid + ".json"

    try:

        file_content = s3.Object(BUCKET_NAME, file_name).get()["Body"].read()

    except:

        return jsonify({"Error": "File not found"}), 404

    result = json.loads(file_content)

    return jsonify(result)


@app.route("/update", methods=["POST"])
@jwt_required()
def update():

    current_uuid = request.json.get("uuid", None)

    file_name = "file-" + current_uuid + ".json"

    try:

        file_content = s3.Object(BUCKET_NAME, file_name).get()["Body"].read()

    except:

        return jsonify({"Error": "File not found"}), 404

    result = json.loads(file_content)

    created_by = result["created_by"]

    created_time = result["created_time"]

    current_user = get_jwt_identity()

    current_time = str(datetime.datetime.now())

    data = request.json.get("body", None)

    result = {
        "uuid": current_uuid,
        "created_by": created_by,
        "created_time": created_time,
        "modified_by": current_user,
        "modified_time": current_time,
        "body": data
    }

    file_content = bytes(json.dumps(result), "utf-8")

    file_name = "file-" + current_uuid + ".json"

    s3.Bucket(BUCKET_NAME).put_object(Key=file_name, Body=file_content)

    return jsonify(result)


@app.route("/delete", methods=["POST"])
@jwt_required()
def delete():

    current_uuid = request.json.get("uuid", None)

    file_name = "file-" + current_uuid + ".json"

    try:
        s3.Object(BUCKET_NAME, file_name).delete()
    except:
        return jsonify({"Error": "File not found"}), 404

    return jsonify({"msg": "deleted"})


if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=8000)
