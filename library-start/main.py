from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 　CREATE TABLE
class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(200), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# 本のデータの読み込み(不要)
# all_books = db.session.query(Books).all()　⭐️ここですると不整合が起きる（試してみる）
# print(type(all_books))
# print(all_books[0].title)

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
        new_book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        db.create_all()
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

    print(get_selected_data(id))
    return render_template("edit.html",  book=get_selected_data(id))


#　コントローラの役割だけ
@app.route("/delete/<id>", methods=['GET'])
def delete(id):
    delete_data(id)
    return redirect(url_for('home'))


# データベース用のメソッドだけ
def get_all_data():
    return db.session.query(Books).all()


def get_selected_data(book_id):
    book_to_update = Books.query.get(book_id)
    return book_to_update


def delete_data(book_id):
    book_to_delete = get_selected_data(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()




if __name__ == "__main__":
    app.run(debug=True)
