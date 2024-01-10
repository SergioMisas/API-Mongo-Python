import pymongo

with pymongo.MongoClient("mongodb://admin:password@mongo:27017/") as client:
    database = client.database_test

    try:
        database.command("serverStatus")
    except:
        print("Error connecting to MongoDB")
    else:
        print("MongoDB connection successful")

