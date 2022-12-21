# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:15:03 2022

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
#get the asthma json file and create dataframe
def json_to_mongodb(disease_url):
    disease_data = requests.get(disease_url).json()
    db = database_connection("test_database")
    db.asthma.insert_many(disease_data)
    return 0
def extract(collection):
    db = database_connection("test_database")
    asthma = pd.DataFrame(list(db[collection].find()))
    return  asthma
try:
    json_to_mongodb("https://chronicdata.cdc.gov/resource/us8e-ubyj.json?yearstart=2020")
    mongo_asthma_df = extract("asthma")
except Exception as error:
    print(error)