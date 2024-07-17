import pymongo
import os
import dns.resolver
from config import DB_NAME

# MongoDB connection string
DB_URI = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"

# Set custom DNS resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google's DNS servers

try:
    print("Attempting to connect to MongoDB")
    dbclient = pymongo.MongoClient(DB_URI)
    print("Connection successful")
except pymongo.errors.ConfigurationError as e:
    print(f"ConfigurationError: {e}")
except Exception as e:
    print(f"Other error: {e}")

database = dbclient[DB_NAME]
user_data = database['users']

async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return