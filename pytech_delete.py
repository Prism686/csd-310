import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ec94c0b.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db["students"]

results=collection.find_one({"Student_id" : 1008})
print(results)
value = {"Student_id" : 1008}
collection.delete_one(value)