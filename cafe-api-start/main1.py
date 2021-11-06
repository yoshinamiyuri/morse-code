from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random, json

app = Flask(__name__)


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Object(self)から辞書に変換
        # e.g. <Cafe 20> → {'id': 20, 'name': 'The Bike Shed'}

        dictionary = {column.key: getattr(self, column.name) for column in Cafe.__table__.columns}
        # ⭐️　self.__table__.columnsでなく、Cafe.__table__.columnsの方がいい。
        # selfはオブジェクト(<Cafe 20>)。　　Cafe.はクラスの〜。設計書Cafe(クラス)のテーブルカラムだから、Cafe.の方がいい

        return dictionary

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


@app.route("/")
def home():
    return render_template("index.html")


# ランダムなカフェを表示
@app.route("/random")
## HTTP GET - Read Record
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    print(random_cafe)  #オブジェクト型　 <Cafe 20>
    print(random_cafe.to_dict()) #辞書型 {'id': 20, 'name': 'The Bike Shed'}

    # print(jsonify(cafe=random_cafe.to_dict()))
    # 辞書からJSONに変換　#⭐️cafe=にしている理由 クライアントによる物である。
    return jsonify(random_cafe.to_dict())


@app.route("/all")
## HTTP GET - Read Record
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    # print(all_cafes)
    # print([cafe.to_dict() for cafe in all_cafes])
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

    # cafes = []
    # for cafe in all_cafes:
    #     print(cafe)
    #     print(cafe.to_dict())
    #     # cafes[Cafe.__table__.columns] = cafe.to_dict()  #cafes[<Cafe1>] ={"can_take_calls": false, }  エラー出る
    #     cafes.append(cafe.to_dict())
    # print(cafes)
    #
    # # 辞書からJSONに変換
    # return jsonify(cafe=cafes)


# ユーザの入力した場所(loc)から、同じ場所にあるカフェを検索
@app.route("/search/")
def search():
    location = request.args.get('loc')
    all_cafes = db.session.query(Cafe).all()

    target_city_cafes_object = [cafe for cafe in all_cafes if cafe.to_dict()["location"] == location]
    print(target_city_cafes_object) # [<Cafe 1>, <Cafe 9>]

    # ヒットしたカフェがある時
    if len(target_city_cafes_object) != 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in target_city_cafes_object])
        # return target_city_cafes_object #[<Cafe 1>, <Cafe 9>] であるが、TypeError: 'list' object is not callableのエラー出る
    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."},
        )


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD

        new_cafe = Cafe(
            name=request.args.get('name'),
            # name=request.form.get('name'), #これだと、Noneが返ってくるけど、先生の記載がこれ。。。
            img_url=request.args.get("img_url"),
            map_url=request.args.get("map_url"),
            location=request.args.get("location"),
            seats=request.args.get("seats"),
            has_toilet=str2bool(request.args.get("has_toilet")), # 文字列から、booleanに変換しないといけない
            has_wifi=str2bool(request.args.get("has_wifi")),
            has_sockets=str2bool(request.args.get("has_sockets")),
            can_take_calls=str2bool(request.args.get("can_take_calls")),
            coffee_price=request.args.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(
            response={"success": "Successfully added the new cafe"},
        )


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    print(new_price)

    # id==<cafe_id> のデータを更新 ⭐️
    cafe = db.session.query(Cafe).filter(Cafe.id==cafe_id).first()
    # cafe = db.session.query(Cafe).get(cafe_id)
    print(cafe)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe_record(cafe_id):
    api_key = request.args.get("api-key")
    print(api_key)

    # if分の多重構造になってるけど、問題ない？　⭐️
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        # 404 = Resource not found
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key"}), 403

if __name__ == '__main__':
    app.run(debug=True)
