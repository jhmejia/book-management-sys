import sys
import book_dao

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search all books',
    2: 'Search by title',
    3: 'Search by publisher',
    4: 'Search by price range (min, max)',
    5: 'Search by title and publisher',
    6: 'Return to main menu',
}

def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()


    # for x in results:
    #     print(x)
    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item)
        
    print("The end of books.")
    

def search_by_title():
    title = input("What is the exact book title that you are looking for?\n")
    results = list(book_dao.findByTitle(title))
    # Display results
    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("The title you wanted does not exist in our database.")
    print("The end.")

def search_by_publisher():
    publisher = input("What is the name of the publisher you are looking for?\n")
    #Check to see if publisher exists
    results = list(book_dao.findPublisher(publisher))
    if len(results) == 0:
        print("The publisher you are looking for does not exist in our database. Please try again.")
        return


    results = list(book_dao.findByPublisher(publisher))
    # Display results
    if len(results) != 0:
        print("We found the following matching books for you.")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("There are no books written by the publisher you are looking for .")
    print("The end.")

def search_by_price_range():
    min_price = input("Please enter the min price of the book you want to search.\n")
    max_price = input("Please enter the max price of the book you want to search.\n")
    # Check if the price is a number
    try:
        float(min_price)
        float(max_price)
    except ValueError:
        print("The price you entered is not a number. Please try again.")
        return
    results = book_dao.findByPriceRange(min_price, max_price)
    # Display results
    #print(results)
   
    print("We found the following books matching prices for you.")
    for item in results:
        print(item['ISBN'], item['title'])
  
    
    print("The end.")

def search_by_title_and_publisher():
    title = input("What is the exact book title that you are looking for?\n")
    publisher = input("What is the name of the publisher you are looking for?\n")
    results = list(book_dao.findByTitleAndPublisher(title, publisher))
    # Display results
    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("The title and publisher you wanted does not exist in our database.")
    print("The end.")

def print_menu():
    print("------------------------")
    print()
    print("Please make a selection- What do you want to do?")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_search_menu():
    print()
    print("Please make a selection for search")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()    


def option1():
    print('Handle option \'Option 1\': Add a Publisher')
    # Add a publisher
    # 1. Prompt user for publisher name
    publisher = input("Please enter the name of the publisher you want to add.\n")
    # 2. Check if the publisher already exists
    results = list(book_dao.findPublisher(publisher))
    if len(results) != 0:
        print("The publisher you want to add already exists in our database. Please try again.")
        return
    # 3. Prompt user for publisher phone number
    phone = input("Please enter the phone number of the publisher you want to add.\n")
    # 4. Prompt user for publisher city
    city = input("Please enter the city of the publisher you want to add.\n")
    # 5. Call DAO to add the publisher
    book_dao.addPublisher(publisher, phone, city)
    # 6. Display the result
    print("The publisher", publisher, "has been added.")

# Option 2: Add a book
def option2():
    print('Handle option \'Option 2\': Add a Book')
    # Add a book
    # 1. Prompt user for ISBN, title, year, publisher, price
    isbn = input("Please enter the ISBN of the book you want to add.\n")
    # 2. Check if the book already exists
    results = list(book_dao.findByISBN(isbn))
    if len(results) != 0:
        print("The book you want to add already exists in our database. Please edit it instead.")
        return
    
    title = input("Please enter the title of the book you want to add.\n")
    year = input("Please enter the year of the book you want to add.\n")
    #Check if the year is valid
    if not year.isdigit():
        print("The year you entered is not valid. Please try again.")
        return
    publisher = input("Please enter the publisher of the book you want to add.\n")
    # 3. Check if the publisher exists
    results = list(book_dao.findPublisher(publisher))
    if len(results) == 0:
        print("The publisher you entered does not exist in our database. Please add it first.")
        return
    
    previous_edition = input("Please enter the previous edition's ISBN of the book you want to add. (\"None\" if none)\n")
    # 4. Check if the previous edition exists
    if previous_edition != "None":
        results = list(book_dao.findByISBN(previous_edition))
        if len(results) == 0:
            print("The previous edition you entered does not exist in our database. Please add it first.")
            return

    price = input("Please enter the price of the book you want to add.\n")
    # Check if the price is a number
    try:
        float(price)
    except ValueError:
        print("The price you entered is not a number. Please try again.")
        return
    # 5.  Call DAO to add the book
    book_dao.addBook(isbn, title, publisher, previous_edition, price)
    # 6. Display the result
    print("The book with ISBN", isbn, "has been added.")



def option3():
    print('Handle option \'Option 3\': Edit a Book')
    # Edit a book
    # 1. Prompt user for ISBN
    isbn = input("Please enter the ISBN of the book you want to edit.\n")
    # 2. Check if the book exists
    results = list(book_dao.findByISBN(isbn))
    if len(results) == 0:
        print("The book you want to edit does not exist in our database. Please add it first.")
        return
    # 3. Prompt user for new title, year, publisher, previous edition, price
    title = input("Please enter the new title of the book you want to edit.\n")
    year = input("Please enter the new year of the book you want to edit.\n")
    #Check if the year is valid
    if not year.isdigit():
        print("The year you entered is not valid. Please try again.")
        return
    publisher = input("Please enter the new publisher of the book you want to edit.\n")
    # 4. Check if the publisher exists
    results = list(book_dao.findPublisher(publisher))
    if len(results) == 0:
        print("The publisher you entered does not exist in our database. Please add it first.")
        return

    previous_edition = input("Please enter the new previous edition's ISBN of the book you want to edit. (\"None\" if none)\n")
    # 5. Check if the previous edition exists
    if previous_edition != "None":
        results = list(book_dao.findByISBN(previous_edition))
        if len(results) == 0:
            print("The previous edition you entered does not exist in our database. Please add it first.")
            return

    price = input("Please enter the new price of the book you want to edit.\n")
    # Check if the price is a number
    try:
        float(price)
    except ValueError:
        print("The price you entered is not a number. Please try again.")
        return
    # 6.  Call DAO to edit the book
    book_dao.editBook(isbn, title, year, publisher, previous_edition, price)

# Option 4: Delete a book
def option4():
    print('Handle option \'Option 4\': Delete a Book')
    # Delete a book
    # 1. Prompt user for ISBN
    isbn = input("Please enter the ISBN of the book you want to delete.\n")
    # 2. Check if the book exists
    results = list(book_dao.findByISBN(isbn))
    if len(results) == 0:
        print("The book you want to delete does not exist in our database. Please try again.")
        return
    # 3. Call DAO to delete the book
    book_dao.deleteBook(isbn)
    # 4. Display the result
    print("The book with ISBN", isbn, "has been deleted.")



def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    while(True):
        print_search_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           search_all_books()
           return
        elif option == 2:
            search_by_title()
            return
        elif option == 3:
            search_by_publisher()
            return
        elif option == 4:
            search_by_price_range()
            return
        elif option == 5:
            search_by_title_and_publisher()
            return
        elif option == 6:
            return
        else:
            print('Invalid option. Please enter a number between 1 and 6.')



if __name__=='__main__':
    print(f"{bcolors.HEADER}Welcome to the Book Management System{bcolors.ENDC}")
    while(True):
        
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        # More options to be added
        elif option == 5:
            option5()
        elif option == 6:
            
            print(f"{bcolors.HEADER}Thank you for using our database services! Bye{bcolors.ENDC}")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











