import sqlite3

class BookDB(object):

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = self._dict_factory
        self.db = self.conn.cursor()

    def get_book(self, isbn):
        self.db.execute('SELECT * FROM books WHERE isbn = :isbn', (isbn,))
        return self.db.fetchone() 

    def add_book(self, book):

        # Get publisher ID if publisher is already in the DB,
        # otherwise add them and set the ID
        pub = self.get_publisher(book['publisher'])
        if not pub:
            pub = self.add_publisher(book['publisher'])
        book['publisher'] = pub['id']

        book_args = (book['isbn'], book['title'], book['author'], 
                book['pages'], book['publisher'], book['copies'], 
                book['year'])

        self.db.execute('INSERT INTO books(isbn, title, author, \
                pages, publisher_id, copies, year) \
                VALUES(:isbn, :title, :author, :pages, \
                :publisher, :copies, :year)', book_args)

        self.conn.commit()
        return self.get_book(book['isbn'])

    def get_books(self):
        self.db.execute('SELECT * FROM books')
        return self.db.fetchall()

    def get_publisher(self, name):
        self.db.execute('SELECT * FROM publishers WHERE name = :name', (name,))
        return self.db.fetchone()

    def add_publisher(self, name):
        self.db.execute('INSERT INTO publishers(name) VALUES(:name)', (name,))
        self.conn.commit()
        return self.get_publisher(name)

    def _dict_factory(self, cursor, row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
