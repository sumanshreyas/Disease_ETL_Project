# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:52:06 2022

@author: Suman
"""

import json
from pymongo import MongoClient
# Making Connection
client = MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))
# database
db = client['test_database']

# Created or Switched to collection

collection = db['mental']

# Loading or Opening the json file
with open('mental.json') as file:
    file_data = json.load(file)
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used

if isinstance(file_data, list):
    collection.insert_many(file_data) 
else:
    collection.insert_one(file_data)

# Created or Switched to collection    
collection = db['asthma'] 
# Loading or Opening the json file   
with open('asthma.json') as file:
    file_data = json.load(file)
    
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used

if isinstance(file_data, list):
    collection.insert_many(file_data) 
else:
    collection.insert_one(file_data)

# Created or Switched to collection
    
collection = db['diabetes'] 
# Loading or Opening the json file   
with open('diabetes.json') as file:
    file_data = json.load(file)

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
    
if isinstance(file_data, list):
    collection.insert_many(file_data) 
else:
    collection.insert_one(file_data)