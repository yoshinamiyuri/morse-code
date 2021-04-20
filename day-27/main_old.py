from tkinter import *
# import tkinter


def button_clicked():
    # my_label.config(text=f"{user_input}")#🔥
    new_text = input.get() #⭐️
    my_label.config(text=new_text)#⭐️
    print("I got clicked")
    # print(user_input)　#🔥


window = Tk()
# window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# Label
#ToDO:  上記のように、fontは指定しなくていい(default valueがあるから)
my_label= Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label= tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="top", expand=True)
my_label.pack()

# Edit the text
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
# ToDO: 質問：⭐️の代わりに、🔥で書いたら、なんで動かないの？text input文字を入れてクリックしても、ラベル名が置き換えられない
button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()
# user_input = input.get()　#🔥


window.mainloop() # keep the screen open 基本的に一番下に書く