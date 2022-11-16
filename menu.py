#===============================================================================
# Project 1 - Book Management System
# John Henry Mejia
# 11/9/2022
# Path: menu.py
#===============================================================================


import sys
import book_dao


#This python program uses colors! If you don't want colors/ doesn't work when you're testing, set this to False
useColors = True


if useColors:
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

# Menu options dictionary (used in print_menu)
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    # More options to be added
    5: 'Search Books',
    6: 'Exit',
}

#Search menu options dictionary (used in print_search_menu)
search_menu_options = {
    1: 'Search all books',
    2: 'Search by title',
    3: 'Search by ISBN',
    4: 'Search by publisher',
    5: 'Search by price range (min, max)',
    6: 'Search by year',
    7: 'Search by Title and Publisher',
    8: 'Return to main menu',
}

#===============================================================================
#Helper functions for option 5 (search)
#===============================================================================
def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")


def search_by_title():
    try:
        print('Handle option \'Search by title\'')
        title = input('Enter the full title of the book you want to search: ')
        results = book_dao.findByTitle(title)
        print("The following are the ISBNs and titles of all books with title " + title)
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    except KeyboardInterrupt:
        print('Query cancelled, returning to main menu')
        return


def search_by_isbn():
    try:
        print('Handle option \'Search by ISBN\'')
        try:
            isbn = int(input('Enter the ISBN: '))
            results = book_dao.findByISBN(isbn)
            print("The following are the ISBNs and titles of all books with ISBN " + str(isbn))
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        except ValueError:
            print('Invalid ISBN number')
            return
    except KeyboardInterrupt:
        print('Query cancelled, returning to main menu')
        return

    

def search_by_publisher():
    try:
        print('Handle option \'Search by publisher\'')
        publisher = input('Enter the publisher name: ')
        results = book_dao.findByPublisher(publisher)
        print("The following are the ISBNs and titles of all books with publisher " + publisher)
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    except KeyboardInterrupt:
        print('Query cancelled, returning to main menu')
        return

def search_by_price_range():
    print('Handle option \'Search by price range\'')
    try:
        min = float(input('Enter the minimum price: '))
        max = float(input('Enter the maximum price: '))
        results = book_dao.findByPriceRange(min, max)
        print("The following are the ISBNs and titles of all books in the price range " + str(min) + " to " + str(max))
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    except ValueError:
        print('Invalid price range')
        return
    

def search_by_year():
    print('Handle option \'Search by year\'')
    try:
        year = int(input('Enter the year: '))
    except ValueError:
        print('Invalid year')
        return
    results = book_dao.findByYear(year)
    print("The following are the ISBNs and titles of all books from the year " + str(year))
    for item in results:
        print(item[0], item[1])
    print("The end of books.")

def search_by_title_and_publisher():
    print('Handle option \'Search by title and publisher\'')
    title = input('Enter the title: ')
    publisher = input('Enter the publisher name: ')
    results = book_dao.findByTitleAndPublisher(title, publisher)
    print("The following are the ISBNs and titles of all books with title " + title + " and publisher " + publisher)
    for item in results:
        print(item[0], item[1])
    print("The end of books.")


#===============================================================================
# Print menu options
#===============================================================================
def print_menu():
    print()
    print("--------------------------------------------Book Manager Software-------------------------------------------\n")
    if useColors:
        print(f"{bcolors.HEADER}Please Make a Selection{bcolors.ENDC}")
    else:
        print("Please Make a Selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_search_menu():
    print()
    if useColors:
        print(f"{bcolors.HEADER}Please Make a Selection{bcolors.ENDC}")
    else:
        print("Please Make a Selection")
    
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()
    print("The end of search options")
    print()

#===============================================================================
# Option handling methods
#===============================================================================

#Option 1: Add a publisher
# A publisher has a name, a phone number, and a city
def option1():
    print('\'Option 1\' (Add a Publisher)')
    #A publisher has a name a phone number and a city
    name = input('Enter the publisher name: ')
    try:
        phone = int(input('Enter the phone number: (as an integer) '))
    except ValueError:
        if useColors:
            print(f"{bcolors.FAIL}Invalid phone number{bcolors.ENDC}")
        else:
            print('Invalid phone number')
        
        return
    city = input('Enter the city: ')
    book_dao.addPublisher(name, phone, city)
    print("Publisher added successfully")


#Option 2: Add a book
#A book has an ISBN, a title, a publisher, a year, a previous edition and a price
def option2():
    print('\'Option 2\' (Add a Book)')
    try:
        isbn = int(input('Enter the ISBN: '))
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid ISBN number{bcolors.ENDC}")
        else:
            print('Invalid ISBN number')
        
        return    
    title = input('Enter the title: ')
    publisher = input('Enter the publisher\'s name: ')
    book_dao.checkPublisher(publisher)
    if book_dao.checkPublisher(publisher) == False:
        if useColors:
            print(f"{bcolors.WARNING}Publisher not found. Please add a valid publisher or add yours with \'Add a Publisher\'{bcolors.ENDC}")
        else:
            print('Publisher not found. Please add a valid publisher or add yours with \'Add a Publisher\'')
        return
    try:
        year = int(input('Enter the year: '))
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid year{bcolors.ENDC}")
        else:
            print('Invalid year')
        
        return
    try:
        previous_edition = input('Enter the previous edition\'s ISBN (\'None\' if none) :  ')
        if previous_edition != 'None':
            previous_edition = int(previous_edition)
            if book_dao.checkISBN(previous_edition) == False:
                if useColors:
                    print(f"{bcolors.WARNING}Could not find ISBN number of previous edition book. Try using \'None\' {bcolors.ENDC}")
                else:
                    print('Could not find ISBN number of previous edition book. Try using \'None\'')
                return
    except:
        if useColors:
            print(f"{bcolors.WARNING}Invalid ISBN number{bcolors.ENDC}")
        else:
            print('Invalid ISBN number')
        return
    try:
        price = float(input('Enter the price: '))
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid price{bcolors.ENDC}")
        else:
            print('Invalid price')
        return
    book_dao.addBook(isbn, title, publisher, year, previous_edition, price)
    print("Book added successfully")


#Option 3: Edit a book
#Edit a book with a given ISBN and change the title, publisher, year, previous edition, and price
def option3():
    print('\'Option 3\'(Edit a Book)')
    try:
        isbn = int(input('Enter the ISBN of the book to edit: '))
        if book_dao.checkISBN(isbn) == False:
            if useColors:

                print(f"{bcolors.FAIL}Could not find ISBN number of book to edit.  {bcolors.ENDC}")
            else:
                print('Could not find ISBN number of book to edit.')
            return
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid ISBN number{bcolors.ENDC}")
        else:
            print('Invalid ISBN number')
        
        return
    
    title = input('Enter the new title: ')
    publisher = input('Enter the new publisher: ')
    if book_dao.checkPublisher(publisher) == False:
        if useColors:
            print(f"{bcolors.WARNING}Publisher not found. Please add a valid publisher or add yours with \'Add a Publisher\'{bcolors.ENDC}")
        else:
            print('Publisher not found. Please add a valid publisher or add yours with \'Add a Publisher\'')
        
        return
    try:
        year = int(input('Enter the new year: '))
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid year{bcolors.ENDC}")
        else:
            print('Invalid year')

        return
    try:
        previous_edition = input('Enter the previous edition\'s ISBN (None if none): ')
        if previous_edition != 'None':
            previous_edition = int(previous_edition)
            if book_dao.checkISBN(previous_edition) == False:
                if useColors:
                    print(f"{bcolors.WARNING}Could not find ISBN number of previous edition book. Try using \'None\' {bcolors.ENDC}")
                else:
                    print('Could not find ISBN number of previous edition book. Try using \'None\'')
                return
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid ISBN number{bcolors.ENDC}")
        else:
            print('Invalid ISBN number')
        
        return
    try:
        price = float(input('Enter the price: '))
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid price{bcolors.ENDC}")
        else:
            print('Invalid price')
        
        
        return
    book_dao.updateBook(isbn, title, publisher, year, previous_edition, price)
    print("Book with ISBN " + str(isbn) + " has been updated with the new information.")


#Option 4: Delete a book
#Delete a book with a given ISBN
def option4():
    print('\'Option 4\' (Delete a Book)')
    try:
        isbn = int(input('Enter the ISBN of the book to delete: '))
        if book_dao.checkISBN(isbn) == False:
            if useColors:

                print(f"{bcolors.FAIL}Could not find ISBN number of book to delete.  {bcolors.ENDC}")
            else:
                print('Could not find ISBN number of book to delete.')
            return
    except:
        if useColors:
            print(f"{bcolors.FAIL}Invalid ISBN number{bcolors.ENDC}")
        else:
            print('Invalid ISBN number')
        
        
        return
    book_dao.deleteBook(isbn)
    print("Book with ISBN " + str(isbn) + " has been deleted.")


#Option 5: Search for a book
#Search for a book by ISBN, title, publisher, price range, year, or title and publisher

def option5():
    # A sub-menu shall be printed
    # and prompt user selection
    print('\'Option 5\' (Search Books)')
    print_search_menu()

    # user selection of options and actions
    while True:
        option = ' '
        try:
            option = int(input('Please select a search query, type [1 - 8] and press enter: '))
            break
        except KeyboardInterrupt:
            print('\nInterrupted by user, returning to main menu')
            return
        except:
            if useColors:
               
                print(f"{bcolors.WARNING}Wrong Input. Please enter a number....{bcolors.ENDC}")
            else:
                print('Wrong Input. Please enter a number....')
            

    if option == 1:
        search_all_books()
    elif option == 2:
        search_by_title()
    elif option == 3:
        search_by_isbn()
    elif option == 4:
        search_by_publisher()
    elif option == 5:
        search_by_price_range()
    elif option == 6:
        search_by_year()
    elif option == 7:
        search_by_title_and_publisher()
    elif option == 8:
        return
    else:
        if useColors:
            print(f"{bcolors.WARNING}Invalid option. Please enter a number between 1 and 7.{bcolors.ENDC}")
        else:
            print('Invalid option. Please enter a number between 1 and 7.')
        
        option5() #If the user enters an invalid option, the sub-menu shall be printed again
    





#===============================================================================
# Main
#===============================================================================

if __name__=='__main__':
    

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Please select an option, type [1 - 6] and press enter: '))
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
        except:
            if useColors:
                print(f"{bcolors.WARNING}Wrong Input. Please enter a number....{bcolors.ENDC}")
            else:
                print('Wrong Input. Please enter a number....')
            
            

        # Check what choice was entered and act accordingly
        if option == 1:
           option1() # Add a Publisher
        elif option == 2:
            option2() #Add a book
        elif option == 3:
            option3() #Edit an existing Book
        elif option == 4:
            option4() #Delete an existing Book
        # More options to be added
        elif option == 5: # Search a book
            option5()
        elif option == 6: # Exit
            if useColors:
                
                print(f"{bcolors.OKBLUE}Thanks you for using our database services! Bye!!{bcolors.ENDC}")
            else:
                print('Thanks you for using our database services! Bye!!')
            book_dao.closeConnection()
            exit()
        else:
            if useColors:
                print(f"{bcolors.WARNING}Invalid option. Please enter a number between 1 and 6.{bcolors.ENDC}")
            else:
                print('Invalid option. Please enter a number between 1 and 6.')
            











