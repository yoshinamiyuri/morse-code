# 2021-0418-0419
from tkinter import *  # import all the classes
from tkinter import messagebox  # another module of the code(上の*のなかに入っていない)
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty!")
    else:
        # ToDO: 自分の回答が下記(講師の回答と、比較して確認する⭐️2021-4-20)
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data : Deserialize
                data = json.load(data_file)
                # Updating old data with new data(Add into the dictionary)
                data.update(new_data)

                # print(type(data)) #辞書型
                # print(data)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                data = new_data

        with open("data.json", mode="w") as data_file:
            # Saving updated data: Serialize(write)
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #

def find_password():
    # ユーザのwebsiteが、data.jsonに、既に登録されているか確認する
    try:
        with open("data.json", mode="r") as data_file:
            # Reading old data : Deserialize
            data = json.load(data_file)
            website = website_entry.get()
            if website in data:
                print("既に登録されているwebsiteです")
                messagebox.showinfo(title=f"{website}",
                                    message=f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
            else:
                print("検索されたサイトは、まだ登録されていないです")
                messagebox.showinfo(title=f"{website}",
                                    message=" No details for the website")

    except FileNotFoundError as error_message:
        print("そもそも、ファイルがありません。一度も登録せずに、検索しましたね")
        messagebox.showinfo(title="Error",
                            message=f"No data file found{error_message}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(window, width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
website_label.grid(column=0, row=1)  # 場所を保存している

email_label = Label(text="Email/Username:", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
email_label.grid(column=0, row=2)  # 場所を保存している

pw_label = Label(text="Password:", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
pw_label.grid(column=0, row=3)  # 場所を保存している

# Button
search_button = Button(text="Search", highlightthickness=0, command=find_password, width=14)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate, width=14)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "default@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


