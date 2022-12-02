from pymongo_connector import coll
from pymongo_connector import pub

collection = coll

def findAll():
    results = collection.find({})
    return results


def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results

def findByPublisher(book_publisher):
    results = collection.find({'published_by': book_publisher})
    return results

def findByPriceRange(min_price, max_price):
    max_price = float(max_price)
    min_price = float(min_price)
    results = collection.find({'price': {'$gte': min_price, '$lte': max_price}})
    return results

def findByISBN(ISBN):
    results = collection.find({'ISBN': ISBN})
    return results

def findByTitleAndPublisher(book_title, book_publisher):
    results = collection.find({'title': book_title, 'published_by': book_publisher})
    return results

def addPublisher(name, phone, city):
    results = pub.insert_one({'name': name, 'phone': phone, 'city': city})
    return results

def addBook(isbn, title, publisher, previous_edition, price):
    if previous_edition == 'None':
        previous_edition = None
    price = float(price)
    results = collection.insert_one({'ISBN': isbn, 'title': title, 'published_by': publisher, 'previous_edition': previous_edition, 'price': price})
    return results

def editBook(isbn, title, publisher, previous_edition, price):
    if previous_edition == 'None':
        previous_edition = None
    price = float(price)
    results = collection.update_one({'ISBN': isbn}, {'$set': {'title': title, 'publisher': publisher, 'previous_edition': previous_edition, 'price': price}})

    return results



def deleteBook(ISBN):
    results = collection.delete_one({'ISBN': ISBN})
    return results

def findPublisher(publisher):

    results = pub.find({'name': publisher})
    return results