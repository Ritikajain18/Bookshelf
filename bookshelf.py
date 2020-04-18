class Library:
    def __init__(self, list_of_books, library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for count, books in enumerate(self.list_of_books):
            print(f"{count} {books}")

    def lend_books(self, book, author):
        if (book in self.list_of_books):
            if ((self.lend_data[book]) is None):
                self.lend_data[book] = author
            else:
                print(f"This book is lend by{self.lend_data[book]}")
        else:
            print("you have entered the wrong book ")

    def return_book(self, book, author):
        if book in self.list_of_books:
            if (self.lend_data[book]) is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_books(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_books(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

    # def main(self):


if __name__ == '__main__':
    list_of_books = ["The Merchant of Venice", "Rich Dad Poor Dad", "The Alchemist", "War and Peace", "Lolita"]
    unique_ID = 1999
    Ritika = Library(list_of_books, "Ritika")
    # print(f"Welcome to {self.library_name} Library \n press 'E' to Exit")
    print(
        "1. press 'D' to display all the books in the libaray \n 2. press 'L' to lend books from library \n 3. press 'R' to return books to the librar \n 4. press 'A' to add books to the library \n 5. press 'De' to delete books from the Library")

    Exit = False
    while (Exit is not True):
        _input = input("Select the desired option:")

        if (_input == 'E'):
            Exit = True
        elif (_input == 'D'):
            Ritika.display_books()
        elif (_input == 'L'):
            _input1 = input("Name of the book: ")
            _input2 = input("Author of the book: ")
            print("Book Lend")
            Ritika.lend_books(_input1, _input2)
        elif (_input == 'A'):
            _input1 = input("Name of the Book: ")
            Ritika.add_books(_input1)
        elif (_input == 'De'):
            unique_input = int(input("enter the Unique ID to delete the book"))
            if (unique_input == unique_ID):
                _input2 = input("Enter the book you want to delete")
                Ritika.delete_books(_input2)
            else:
                print("Sorry!!! we can't delete the book")
        elif (_input == 'R'):
            _input3 = input("Name of the book: ")
            _input4 = input("Your name: ")
            Ritika.return_book(_input3, _input4)