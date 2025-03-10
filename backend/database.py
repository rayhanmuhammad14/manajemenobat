from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_CONN = os.getenv('MONGODB_CONN')
DB_OBAT = os.getenv('DB_OBAT')

db = MongoClient(MONGODB_CONN)
obat = db[DB_OBAT]