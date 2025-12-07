# store/db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  # change if needed
db = client["shopping_db"]
products_col = db["products"]
