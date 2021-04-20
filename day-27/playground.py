def test(*args):
    print(args)
    print(type(args))
    for n in args:
        print(n)
#
# test(1,2,3)
# test("text")
# test(1,2,3,4,5)


def add(*args):
    print(args[0])
    print(type(args)) #tuple
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5)) # 引数をいくらでも受け取れる
print(add(2, 4, 5))


def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dict
    for key, value in kwargs.items():
        print(key, value)

    print("kwargs['add']", kwargs["add"])

calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kw):
#ToDO: 次の書き方は、絶対に引数を指定しないといけなくなる(makeとmodel)  ※エラー出る！
        # self.make = kw["make"]
        # self.model = kw["model"]

#ToDO: 次の書き方は、引数ない場合は、Noneにしてくれる
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make = "nissan")
# my_car = Car(make = "nissan", model="GT-R")
print(my_car.model)