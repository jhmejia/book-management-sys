# book-management-sys
## This is SQL that does book management system with an interactive menu

#### •	The system shall allow user to add a new publisher (name, phone and city).
#### •	The system shall allow user to add a new book (ISBN, title, year, published_by, previous edition and price).
#### •	The system shall allow user to edit an existing book.
#### •	The system shall allow user to delete a book.
#### •	The system shall allow user to search books based on criteria.
1.	All books.
2.	Based on title. Zero or more books shall be returned.
3.	Based on ISBN. One or zero book shall be returned.
4.	Based on publisher. Zero or more shall be returned.
5.	Based on price range (min and max). Zero or more shall be returned.
6.	Based on year. Zero or more shall be returned.
7.	Based on title and publisher. Zero or more shall be returned.


### The following is the schema of the database.
•	Publisher (name, phone, city), PK: name.
•	Book (ISBN, title, year, published_by, previous_edition, price), PK: ISBN, FK: published_by refs Publisher, previous_edition refs Book

