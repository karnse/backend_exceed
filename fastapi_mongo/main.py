from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
load_dotenv('.env')
username=os.getenv('username')
password=urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{username}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')

db = client["exceedtest"]
collection = db['enrrolment']

res = collection.insert_one({"person":"1"})
collection.de
# for i in collection.find():
#     print(i)

# print(collection)