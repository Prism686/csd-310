import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ec94c0b.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db["students"]

#find_one = ("student_id" : 1007)
#print(find_one)

results = collection.find_one({"Student_id" : 1007})
print(results)

update = {"Last Name" : "Oakenshield"}

#print(update)

updatevalue = {"$set" : {"Last Name" : "Chief"}}
 
#print(updatevalue)

collection.update_one(update, updatevalue)
