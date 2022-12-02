# pip install pymongo
# pip install dnspython


import pymongo

dbname = "bookmanager"
collection = "Book"
collection2 = "Publisher"

myclient = pymongo.MongoClient("mongodb://root:password@127.0.0.1:27017/")

coll = myclient[dbname][collection]

pub = myclient[dbname][collection2]


#Display all documents in the collection
# for x in coll.find():
#     print(x)
    


