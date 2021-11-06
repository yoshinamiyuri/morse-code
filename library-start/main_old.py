# 要復習！！！
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 　CREATE TABLE
class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(200), nullable=False)

    # インスタンスを作成したいときに必要。今回は不要。
    # def __init__(self, title, author, rating):
    #    self.title = title
    #    self.author = author
    #    self.rating = rating

    # 下の意図がわからない⭐️
    # Optional: this will allow each book object to be identified by its title when printed.
    # 特殊で、クラスに持たせることができる。　__repr__
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# 本のデータの読み込み(不要)
# all_books = db.session.query(Books).all()　⭐️ここですると不整合が起きる（試してみる）
# print(type(all_books))
# print(all_books[0].title)


# sqlalchemyを使用せず、sqlite3のみを使用する方法（データベースへの格納）
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# 一覧ページを見せるだけで良い。何も引数を受け取らない。（全部見せるだけ）
@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    return render_template("index.html", all_books=all_books)


#　理想的なPOSTの使用方法（登録）
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # sqlalchemyを使用しない方法（DBがないので、runするたびにデータ消去される）
        # new_books = {
        #     "name": request.form["name"],
        #     "author": request.form["author"],
        #     "rating": request.form["rating"]
        # }
        # all_books.append(new_books)

        # CREATE RECORD on SQLite
        new_book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        db.create_all()

        # addをpostした後に、親切心で、一覧ページに飛ばしている　⭐️️postの時に、redirectをよく使う。検索の時に、postを使用している場合がある。
        return redirect(url_for('home'))

    return render_template("add.html")


# 更新だけど、PUTでなく、POSTで動いている（ここのPOSTの例はイマイチ。jsonを渡したいのに、idがURLに含まれているから）
@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        book_to_update = Books.query.get(id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    print("editのid", id)
    # id = int(id)-1　#⭐️データベースのidと、リストのindexを、どちらもidをしていたから混乱する元になっていた
    # return render_template("edit.html", index=int(id)-1, all_books=all_books)
    all_books = db.session.query(Books).all() #⭐ここで実行することで、最新情報が取得できる。全部取得してくるから、無駄が発生している。


    print(all_books[int(id)-1])
    return render_template("edit.html",  book=all_books[int(id)-1])


# deleteを行う
@app.route("/delete/<id>", methods=['GET'])
def delete(id):
    print("deleteのid",id)
    #     id = int(id) - 1
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


#データベース用のメソッドを分けておくと尚良い



if __name__ == "__main__":
    app.run(debug=True)
