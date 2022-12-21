# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:16:39 2022

@author: Suman
"""

import pandas as pd
import json
import requests
from pymongo import MongoClient

# Making Connection with mongodb database
def database_connection(db_name):
   client = MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))
# database
   db = client['test_database']
   return db
#get the json file and create dataframe
def json_to_mongodb(disease_url):
    disease_data = requests.get(disease_url).json()
    db = database_connection("test_database")
    db.mental.insert_many(disease_data)
    return 0
def extract(collection):
    db = database_connection("test_database")
    mental = pd.DataFrame(list(db[collection].find()))
    return  mental
try:
    json_to_mongodb("https://chronicdata.cdc.gov/resource/ixrt-gnsg.json?yearstart=2020")
    mongo_mental_df = extract("mental")
except Exception as error:
    print(error)