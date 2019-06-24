from pymongo import MongoClient

def base(self):
    server = MongoClient('localhost', 27017)

    return server['esimples_db']
