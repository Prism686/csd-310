import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ec94c0b.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db["students"]
#print (db.list_collection_names)

docs = collection.find_one({"Student_id": 1007})

print(docs)
