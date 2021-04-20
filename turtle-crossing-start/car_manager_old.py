from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# ⭐️Turtleからの継承をしなくても良い理由（class CarManager(Turtle):と記載しない理由は？


class CarManager():
    def __init__(self):
        super(CarManager, self).__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        # ToDO: 上下スクリーンの50pxは空けておく（見づらいので） (-15, 15) * 20にしない。20はカメのサイズ。
        random_x = random.randint(-12, 12) * 20 # ⭐ * 20で良いか質問する️
        random_y = random.randint(-12, 12) * 20 # ⭐ * 20で良いか質問する️
        self.goto(random_x, random_y)

    def create_car(self):
        cars = []
        for _ in range(20):
            car = CarManager()
            cars.append(car)
        # car.move()

    def move(self):
        self.penup()
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)
        print("moveしている")

    def move_faster(self):
        self.move()
        self.speed()












