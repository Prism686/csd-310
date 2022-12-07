import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ec94c0b.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db["students"]
#print (db.list_collection_names)

#post1 = {"Student_id": 1007, "First Name": "Thorin", "Last Name": "Oakenshield"}
#post2 = {"Student_id": 1008, "First Name": "Bilbo", "Last Name": "Baggins"}
#post3 = {"Student_id": 1009, "First Name": "Frodo", "Last Name": "Baggins"}

#collection.insert_many([post1,post2,post3])

