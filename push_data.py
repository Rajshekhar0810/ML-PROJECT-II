import os
import sys
import pymongo
import json
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

uri = os.getenv("MONGO_DB_URL")
print(uri)

import certifi             #The server (like MongoDB Atlas) already has its own SSL/TLS certificate issued by a Certificate Authority (CA).
ca = certifi.where()       # certifi helps the client (python)verify if the server’s certificate is trustworthy before sending any data
                        #ca -> Certificate Authority,it retrieves a bundle of trusted CA certificates from the certifi package.


import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract():
    def __init__(self):
       try:
           pass
       except Exception as e:
           raise NetworkSecurityException(e, sys) 

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True) # we dont want to keep the old index
            records = list(json.loads(data.T.to_json()).values()) #Normally, in a DataFrame: columns = keys, rows = values.transpose “catches columns as values”
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection          # MongoClient → Database → Collection → Documents
                                                #MongoDB is document-based, not table-based
            self.mongo_client=pymongo.MongoClient(uri)   #Connects to the MongoDB server
            self.database=self.mongo_client[self.database]  #Accesses a database inside MongoDB by name
            self.collection=self.database[self.collection]  #Accesses a collection inside that database
            self.collection.insert_many(self.records)    #Inserts all documents (records) into the collection.
            return(len(self.records))    #Only after insertion does MongoDB actually create the database and collection if they don’t exist.
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    file_path = "Network_Data/phisingData.csv"
    DATABASE = "RAJAI"
    Collection = "NetworkData"
    obj = NetworkDataExtract()
    records = obj.csv_to_json_convertor(file_path)
    print(records)
    count = obj.insert_data_mongodb(records,DATABASE,Collection)
    print(f"Total {count} records inserted successfully into MongoDB")


        



# Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)