#8.Write a program to implement a basic library book management with the functionalities such as 
# issue the book, return the book and search the book. 
# Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features. 
# For the storage of book details, use the file handling along with the exception handling. 


# Book class to represent individual book objects
import os
class Book:
    def __init__ (self, book_id, title, author):
        self.book_id = book_id #books unique id
        self.title = title #book title
        self.author = author #author name
    
class Library:
    def __init__(self):
        self.books = [] #empty list to hold book objects
        self.book_data() #loads the book data from the file


    def book_data(self):
        try: #if file exists
            with open ("books.txt", "r") as file:#opening the books.txt in read mode
                for line in file:
                    book_id, title, author = line.strip().split(",") #removes white space and splits by comma and makes list
                    #appends the class book info in empty list
                    self.books.append(Book(book_id, title, author))#book class append
        except FileNotFoundError:
            print ("The file doesnot exist")
        except Exception as e:
            print (f"The error is {e}")


    def save_data (self): #saves the book data in the file
        with open ("books.txt", "w+") as file: #opening the books.txt in write mode
            for book in self.books:
                file.write (f"{book.book_id}, {book.title}, {book.author} \n")

    
    def display_books(self): #displays all the book
        try:
            if  self.books: #checks in books list
                print ("Books in the library")

                for book in self.books: #books available in library
                    print (f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

        except Exception:
            print ("Books are not available in the library")


    def issue_book(self, book_id):
        try:
            for book in self.books:
                if book.book_id == book_id:
                    self.books.remove(book) #if the book is issued it removes the book from books list
                    print (f"The book {book.title} {book.book_id} has been issued")
                    self.save_data() #saves the data(book issued) in save_data 
                    return
        except Exception:
            print ("Book not found")


    def return_book (self, book_id, title, author):
        self.books.append(Book(book_id, title, author))# again adds the book after being returned
        print (f"The book {title} {book_id} has been returned")
        self.save_data()#saves the data

    #to search book by title
    def search_book (self,title):
        for book in self.books:
            if book.title.lower() in book.title.lower():
                print (f"{book.title},{book.book_id} has been found")
                return 
        print ("Book not found!") #if not in books


def main():
    library = Library()  # Creating an instance of the Library class

    while True:
        print("\n--- Library Menu: --- \n")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()  # Displays all books
        elif choice == "2":
            book_id = input("Enter the Book ID to issue: ")
            library.issue_book(book_id)  # Issue a book
        elif choice == "3":
            book_id = input("Enter the Book ID to return: ")
            title = input("Enter the Title of the book: ")
            author = input("Enter the Author of the book: ")
            library.return_book(book_id, title, author)  # Return a book
        elif choice == "4":
            title = input("Enter the Title of the book to search: ")
            library.search_book(title)  # Search for a book
        elif choice == "5":
            print("Exiting the program...")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
