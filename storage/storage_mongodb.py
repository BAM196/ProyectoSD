# storage/mongo_storage.py

from pymongo import MongoClient

class MongoStorage:
#    def _init_(self, uri="mongodb+srv://hugomartinez2:colocolo123@cluster0.tbgfql2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", db_name="waze", collection_name="eventos"):
    def _init_(self, uri="mongodb://HM:colocolo123@localhost:27017/waze?authSource=admin",db_name="waze", collection_name="eventos"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_many_events(self, events):
        if events:
            self.collection.insert_many(events)
            print(f"Se insertaron {len(events)} eventos en MongoDB.")
        else:
            print("No hay eventos para insertar.")