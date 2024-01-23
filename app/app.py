from flask import Flask, jsonify, request
import database_manager

app = Flask(__name__)

user = "admin"
password = "password"
host = "mongo"
port = 27017


@app.route("/")
def main():
    db = database_manager.connect_db(user, password, host, port).database_test
    return jsonify({"status": database_manager.test_connection(db)})


@app.route("/notes")
def get_notes():
    db = database_manager.connect_db(user, password, host, port).database_test
    notes = {str(notes.pop("_id")): notes for notes in database_manager.get_notes(db)}
    return jsonify({"notes": notes})


@app.route("/notes", methods=["POST"])
def create_note():
    db = database_manager.connect_db(user, password, host, port).database_test
    note = request.json

    id_note = database_manager.create_note(note, db)
    return jsonify({"id": str(id_note)})


@app.route("/notes", methods=["DELETE"])
def delete_notes():
    db = database_manager.connect_db(user, password, host, port).database_test
    database_manager.delete_notes(db)
    return {"status": "success"}


@app.route("/notes/<id>", methods=["DELETE"])
def delete_note(id):
    db = database_manager.connect_db(user, password, host, port).database_test
    database_manager.delete_note(db, id)
    return {"status": "success"}


@app.route("/notes/<id>", methods=["PUT"])
def update_note(id):
    db = database_manager.connect_db(user, password, host, port).database_test
    new_note = request.json
    database_manager.update_note(db, id, new_note)
    return {"status": "success"}


@app.route("/notes/<id>", methods=["GET"])
def get_notes_by_id(id):
    db = database_manager.connect_db(user, password, host, port).database_test
    notes = database_manager.get_notes_by_id(db, id)
    return jsonify({"notes": notes})
