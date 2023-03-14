from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient

load_dotenv()

def get_collection():
    client = MongoClient(getenv('DATABASE_CONNECTION'))
    db = client['COMP67450001']
    return db['flight-satisfaction']

def get_review():
    collection = get_collection()
    return collection.find_one({'name':'history'})

def add_review(result:bool):
    collection = get_collection()
    history = get_review()
    if result: 
        collection.update_one({'_id':history.get('_id')}, {'$inc':{'yes':1}})
    else:
        collection.update_one({'_id':history.get('_id')}, {'$inc':{'no':1}})
    
