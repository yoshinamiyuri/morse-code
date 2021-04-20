from tkinter import *


def button_clicked():
    # my_label.config(text=f"{user_input}")#🔥
    new_text = input.get() #⭐️
    my_label.config(text=new_text)#⭐️
    print("I got clicked")
    # print(user_input)　#🔥


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label= Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
#ToDO: pack,place,gridのどれかを使う（同時には使えない）。gridが一番楽。
# my_label.pack()
# my_label.place(x=150, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack() # 記載しなければ、非表示になる
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click You", command=button_clicked)
# button.pack() # 記載しなければ、非表示になる
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=20)
# input.pack()
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)

window.mainloop()