import pandas
import turtle
from turtle import Turtle

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = data.to_dict()
# print(alpha_dict)
# print(type(alpha_dict))

alpha_data_frame = pandas.DataFrame(alpha_dict)
# print(alpha_data_frame)
# print(type(alpha_data_frame))

# for (index, row) in alpha_data_frame.iterrows():
#     print(row.letter, row.code)

phonetic_dict = {row.letter: row.code for (index, row) in alpha_data_frame.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

screen = turtle.Screen()
screen.title("電話の時に、自分の名前の伝え方")

user_name = screen.textinput(title=f"Your name:",
                                prompt="What's your name? ").upper()

# user_name_list = [char for char in user_name]
output_list = [phonetic_dict[char] for char in user_name]
print(output_list)
# print(phonetic_dict["Y"])
