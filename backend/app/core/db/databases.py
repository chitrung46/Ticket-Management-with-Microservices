from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://luongchitrung53:pass4db@ticket-management.bcadb.mongodb.net/?retryWrites=true&w=majority&appName=Ticket-Management"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.bus_db
collection_name = db['bus']