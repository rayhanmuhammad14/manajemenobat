from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_CONN = os.getenv('MONGODB_CONN')
CLUSTER = os.getenv('DB')
COLLECTION_OBAT = os.getenv('COLLECTION_OBAT')
COLLECTION_USER = os.getenv('COLLECTION_USER')

client = MongoClient(MONGODB_CONN)
cluster = client[CLUSTER]

obatDatas = cluster[COLLECTION_OBAT]
userDatas = cluster[COLLECTION_USER]
