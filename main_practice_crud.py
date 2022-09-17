# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books ("
# #                "id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


#
#
# db.create_all()

# entry = Book(title="Lion", author="J. K. Rowling", rating="9")

# db.session.add(entry)
# db.session.commit()

# # Query all books
# all_books = db.session.query(Book).all()
# print(all_books)

# # Query a particular book
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# # Update A Particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()
# book.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# # Update A Record By PRIMARY KEY
# book_id = 1
# book = Book.query.get(book_id)
# book.title = "Harry Potter and the Chamber"
# db.session.commit()

# # Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book = Book.query.get(book_id)
# db.session.delete(book)
# db.session.commit()


