from mysql_connector import connection

# This function finds all the books in the database
def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

# This function checks if a publisher exists in the database
def checkPublisher(publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Publisher where name = %s" 
    cursor.execute(query, (publisher,))
    results = cursor.fetchall()
    if len(results) == 0:
        return False
    else:
        return True

#This function checks if an isbn exists in the database
def checkISBN(isbn):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where isbn = %s"
    cursor.execute(query, (isbn,))
    results = cursor.fetchall()
    if len(results) == 0:
        return False
    else:
        return True

#This functions finds all the books with the given title
def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s"
    cursor.execute(query, (title,))
    results = cursor.fetchall()
    #connection.close()
    return results

#This function finds all the books with the given isbn
def findByISBN(isbn):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where isbn = %s"
    cursor.execute(query, (isbn,))
    results = cursor.fetchall()
    connection.close()
    return results

#This function finds all the books with the given publisher
def findByPublisher(publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where publisher = %s"
    cursor.execute(query, (publisher,))
    results = cursor.fetchall()
    #connection.close()
    return results

# This function finds all the books within the given price range
def findByPriceRange(min, max):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price between %s and %s"
    cursor.execute(query, (min, max))
    results = cursor.fetchall()
    #connection.close()
    return results

#This function finds all the books with the given year of publication
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year = %s"
    cursor.execute(query, (year,))
    results = cursor.fetchall()
    #connection.close()
    return results

#This function finds all the books with the given Title AND publisher
def findByTitleAndPublisher(title, publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s and publisher = %s"
    cursor.execute(query, (title, publisher))
    results = cursor.fetchall()
    #connection.close()
    return results

#This function updates a book. Given the isbn, it will update the title, publisher, year, previous_edition, and price
def updateBook(title, isbn, publisher, year, previous_edition, price):
    cursor = connection.cursor()

    if previous_edition == "None":
        query = "update bookmanager.Book set title = %s, publisher = %s, year = %s, previous_edition = %s, price = %s where isbn = %s"
        cursor.execute(query, (title, publisher, year, None, price, isbn))
    else:
        query = "update bookmanager.Book set title = %s, publisher = %s, year = %s, previous_edition = %s, price = %s where isbn = %s"
        cursor.execute(query, (title, publisher, year, previous_edition, price, isbn))

    connection.commit()
    

#This function deletes a book from the database with the given isbn. It will also set all the previous_edition fields that referenced the isbn to None
def deleteBook(isbn):
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where isbn = %s"
    cursor.execute(query, (isbn,))
    connection.commit()
    

#This function adds a publisher to the database
def addPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "insert into bookmanager.Publisher values (%s, %s, %s)"
    cursor.execute(query, (name, phone, city))
    connection.commit()
    #connection.close()

#This function adds a book to the database
def addBook(isbn, title, publisher, year, previous_edition, price):
    cursor = connection.cursor()
    query = "insert into bookmanager.Book values (%s, %s, %s, %s, %s, %s)"
    if previous_edition == "None":
        cursor.execute(query, (isbn, title, year, publisher, None, price))
    else:
        cursor.execute(query, (isbn, title, year, publisher, previous_edition, price))

    connection.commit()
    

def closeConnection():
    connection.close()

