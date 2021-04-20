# 20210324(初回)　1週間後にreviewすべき。review時はできるように(by Angela YU　Sensei)
# Procedural programming (スパゲティーみたいでわかりづらいので、Object Oriented　programmingにすべき)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report of all coffee machine resources
# なんで、str(value)とstringにする必要がある？下のエラーが出力される　⭐質問️
# TypeError: can only concatenate str (not "int") to str


def report():
    for key, value in resources.items():
        print(key + ":" + str(value))
        # print(key, ":", value)
    print("money" + ":" + str(profit))


# TODO: 2. Prompt user by asking(コーヒーができ終わるたびに、聞く必要がある)
# TODO: 3. ユーザのお金が足りているか確認する、不足していれば、refundする


def coffee_maker():
    while True:
        user_menu = input("What would you like? (espresso/latte/cappuccino):")
        if user_menu == "off":
            break
        if user_menu == "report":
            report()
        # print(check_resources(user_menu))

        # 材料確認
        if (user_menu == "espresso" or user_menu == "latte" or user_menu == "cappuccino") and check_resources(user_menu):
            print("Please insert coins.")
            user_money = int(input("how many quarters?: ")) * 0.25
            user_money += int(input("how many pennies?: ")) * 0.05
            user_money += int(input("how many dimes?: ")) * 0.10
            user_money += int(input("how many nickles?: ")) * 0.01

            # user_money = user_quarters * 0.25 + user_nickles * 0.05 + user_dimes * 0.10 + user_pennies * 0.01
            change(user_money, user_menu)
            update_resources(user_menu)

        # 　⭐️️これをコメントアウトしないと、change関数の中身が2回実行される（ifの中も実行している）
        # if change(user_money, user_menu) > 0:
        #     check_resources(user_menu)
        #     cal_money(user_menu)

# TODO: 4. 選ばれたメニューの材料が足りているか確認する（材料確認）


def check_resources(user_menu):
    """Returns True when order can be made, False if ingredients are insufficient"""
    # ループにすべき⭐️
    for item in MENU[user_menu]["ingredients"].keys():
        if resources[item] < MENU[user_menu]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

    # if "water" in MENU[user_menu]["ingredients"].keys() and resources["water"] < MENU[user_menu]["ingredients"]["water"]:
    #     print("Sorry there is not enough water.")
    #     # return retry　エラー出るのなぜ？
    #     return False
    #
    # # espressoを注文した時という条件にしないで、milkがない時という条件にする（人の介入による解釈をしなくても動作するようにする）⭐️
    # if "milk" in MENU[user_menu]["ingredients"].keys() and resources["milk"] < MENU[user_menu]["ingredients"]["milk"]:
    #     print("Sorry there is not enough milk.")
    #     return False
    #
    # if "coffee" in MENU[user_menu]["ingredients"].keys() and resources["coffee"] < MENU[user_menu]["ingredients"]["coffee"]:
    #     print("Sorry there is not enough coffee.")
    #     return False


# 講師の方法
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO:5. お金が足りているか確認する（＋お釣りの計算をする）：普通だったら、2つの関数に分ける（お金確認、お金引く）
# TODO:6. お釣りの計算をする ：(材料確認、お金確認、お金ひく、材料ひく)は、区分して、順序はmainの関数で決める


def change(user_money, user_menu):
    """Returns the change if the payment is accepted, or -1 if the user's money is insufficient"""
    give_change = user_money - MENU[user_menu]["cost"]
    if give_change >= 0:
        change = round(give_change, 2)
        print(f"Here is ${change} in change.")
        cal_money(user_menu)
    else:
        print("Sorry that's not enough money. Money refunded.")
        give_change = -1
    return give_change


# TODO: 7. コーヒーメーカの収益(money)を更新する


def cal_money(user_menu):
    """ユーザの注文を引数にとり、利益を返す"""
    global profit
    profit += MENU[user_menu]["cost"]
    return profit


# ToDO:8. resourcesを更新する（材料引く）


def update_resources(user_menu):
    """ユーザの注文を引数にとり、材料をupdateする"""
    # resourcesが足りているから、使用した分を引いて、updateする
    # for item in user_menu:
    #     if item in MENU[user_menu]["ingredients"].keys():
    #         resources[item] -= MENU[user_menu]["ingredients"][item]
    if "water" in MENU[user_menu]["ingredients"].keys():
        resources["water"] -= MENU[user_menu]["ingredients"]["water"]

    if "coffee" in MENU[user_menu]["ingredients"].keys():
        resources["coffee"] -= MENU[user_menu]["ingredients"]["coffee"]

    # espressoを注文した時のエラーを回避(milkがないので)
    if "milk" in MENU[user_menu]["ingredients"].keys():
        resources["milk"] -= MENU[user_menu]["ingredients"]["milk"]

    print(f"Here is your {user_menu} ☕️. Enjoy!")
    return True


coffee_maker()





