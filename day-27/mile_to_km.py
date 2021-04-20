from tkinter import *


def button_clicked():
    new_miles = int(user_input.get())
    print(new_miles)
    print(new_miles * 1.609)
    km_label.config(text=str(new_miles * 1.60))#⭐️
    print("I got clicked")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Label
km_label = Label(text="0", font=("Arial", 15))
km_label.grid(column=1, row=1)

equal_label = Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 15))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Arial", 15))
km.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
user_input = Entry(width=10)
# input.pack()
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

window.mainloop()