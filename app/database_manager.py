from pymongo import MongoClient


def connect_db(user, password, host, port=27017):
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def test_connection(database):
    try:
        database.command("serverStatus")
    except Exception:
        return "Error connecting to MongoDB"
    else:
        return "MongoDB connection successful"


def create_note(note, database):
    result = database.notes.insert_one(note)
    return result.inserted_id


def get_notes(database):
    return database.notes.find()


def delete_note(database, id):
    return database.notes.delete_one({"_id": id})


def update_note(database, id, new_note):
    return database.notes.update_one({"_id": id}, {"$set": new_note})


def get_notes_by_id(database, id):
    return database.notes.find({"_id": id})


def delete_all_notes(database):
    return database.notes.delete_many({})
