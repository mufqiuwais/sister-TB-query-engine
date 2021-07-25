def get_database():
  from pymongo import MongoClient
  import pymongo

  print("Connecting to Database....")

  # Provide the mongodb atlas url to connect python to mongodb using pymongo
  CONNECTION_STRING = "mongodb+srv://dwinanda:PviH0sYYNT7yhWx3@sister-tb-query-engine.oouxs.mongodb.net/test"

  # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  client = MongoClient(CONNECTION_STRING)
  print("Database connected")

  # Create the database for our example (we will use the same database throughout the tutorial
  return client['query-engine']