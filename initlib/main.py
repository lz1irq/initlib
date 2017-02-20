import sys

import db
import gbooks

class InitLib(object):

    BOOK_FORMAT = 'ISBN: {isbn}\nTitle: {title}\nAuthor(s): {author}\nPages: {pages}\nCopies: {copies}\nYear: {year}\n'

    def __init__(self, db):
        self.db = db
        self.funcs = [
                self.list_books, self.add_book, 
                self.list_pubs, self.add_pub
                ]

    def menu(self):
        while True:
            print('\n0. List books\n1. Add book\n2. List publishers\n3. Add publisher')

            choice = input('Action: ')
            try:
                choice = int(choice)
                self.funcs[choice]()
            except Exception as e:
                print e
                print 'Invalid input, try again.'

    def list_books(self):
        books = self.db.get_books()
        for book in books:
            print(self.BOOK_FORMAT.format(
                    isbn=book['isbn'], title=book['title'], author=book['author'],
                    pages=book['pages'], copies=book['copies'], year=book['year']
                    )
                )

    def add_book(self):
        book = {}
        pass

    def list_pubs(self):
        pass

    def add_pub(self):
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
    else:
        db_path = 'books.db'
    db = db.BookDB(db_path)

    lib = InitLib(db)
    lib.menu()
