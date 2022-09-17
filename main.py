from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///final-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.id}'


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        entry = Book(title=title, author=author, rating=rating)
        db.session.add(entry)
        db.session.commit()

    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_rating(id):
    book = Book.query.get(id)
    if request.method == "POST":
        book.rating = request.form["rating"]
        print(book.rating)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("edit_rating.html",
                               id=book.id,
                               title=book.title,
                               rating=book.rating)


@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
