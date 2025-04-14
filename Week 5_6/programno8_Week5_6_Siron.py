'''Write a program to implement a basic library book management with the functionalities such as issue the book, return the book 
and search the book. Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features. 
For the storage of book details, use the file handling along with the exception handling. '''

class Book:
    def _init_(self, book_id, title, issued=False):
        self.book_id = book_id       #Unique identifier for the book
        self.title = title           #Title of the book
        self.issued = issued         #Status: True if issued, False if available

    #Converts book details into a line of text for saving into a file
    def to_line(self):
        return f"{self.book_id}|{self.title}|{self.issued}"

    #Creates a Book object from a line of text from the file
    @staticmethod
    def from_line(line):
        parts = line.strip().split("|")
        return Book(parts[0], parts[1], parts[2] == "True")


#Class representing the entire library
class Library:
    def _init_(self):
        self.books = []                #List to store all books
        self.filename = "library.txt"  #File to save and load books
        self.load_books()              #Load books from file on startup

    #Load book data from the file
    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    book = Book.from_line(line)
                    self.books.append(book)
        except FileNotFoundError:
            print("No existing library file found. Starting fresh.")
        except Exception as e:
            print("Error reading file:", e)

    #Save all book data to the file
    def save_books(self):
        try:
            with open(self.filename, "w") as f:
                for book in self.books:
                    f.write(book.to_line() + "\n")
        except Exception as e:
            print("Error writing file:", e)

    #Add a new book to the library
    def add_book(self):
        book_id = input("Enter new Book ID: ")
        title = input("Enter Book Title: ")

        #Check if Book ID already exists
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.")
                return

        self.books.append(Book(book_id, title))
        print("Book added successfully.")

    #Display all books in the library
    def view_all_books(self):
        if not self.books:
            print("No books in library.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            print(f"{book.book_id} - {book.title} ({status})")

    #Mark a book as issued
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        for book in self.books:
            if book.book_id == book_id:
                if not book.issued:
                    book.issued = True
                    print("Book issued.")
                else:
                    print("Book already issued.")
                return
        print("Book not found.")

    #Mark a book as returned
    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        for book in self.books:
            if book.book_id == book_id:
                if book.issued:
                    book.issued = False
                    print("Book returned.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")

    #Search for a book by a keyword in its title
    def search_book(self):
        keyword = input("Enter keyword to search: ").lower()
        found = False
        for book in self.books:
            if keyword in book.title.lower():
                status = "Issued" if book.issued else "Available"
                print(f"{book.book_id} - {book.title} ({status})")
                found = True
        if not found:
            print("No matching book found.")


#Main function to run the menu and interact with the library
def main():
    lib = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.view_all_books()
        elif choice == "3":
            lib.issue_book()
        elif choice == "4":
            lib.return_book()
        elif choice == "5":
            lib.search_book()
        elif choice == "6":
            lib.save_books()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")



main()