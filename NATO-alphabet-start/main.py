import pandas
import turtle
from turtle import Turtle

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = data.to_dict()
alpha_data_frame = pandas.DataFrame(alpha_dict)
phonetic_dict = {row.letter: row.code for (index, row) in alpha_data_frame.iterrows()}
# print(phonetic_dict)

screen = turtle.Screen()
screen.title("電話の時に、自分の名前の伝え方")


def name(al_dict):
    # again = True
    # while again:
    while True:
        user_name = screen.textinput(title=f"Your name:",
                                     prompt="What's your name? ").upper()
        try:
            output_list = [al_dict[char] for char in user_name]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(output_list)
            # again = False
            return #whileぶん抜けている　ここで終われるはずなのに、27行目を書いていたら、17行目で終わることになる

name(phonetic_dict)



