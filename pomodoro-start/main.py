from tkinter import *
from PIL import ImageTk, Image

# import all of the classes
# 色えらび：https://colorhunt.co/ ️
# ToDO: 黒く出るのは更新タイミングの問題

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    if timer is None:
        print("Timer is None.")
        return
    window.after_cancel(timer)
    main_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    check_marks.update()
    main_label.update()
    global reps
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    print("reps", reps)
    minute = 3
    work_sec = 1 * minute
    short_break_sec = 1 * minute
    long_break_sec = 1 * minute
    global main_label

    if reps % 8 == 0:
        count_down(long_break_sec)
        main_label.config(text="L Break", fg=RED)
        main_label.update()  # これがないと更新時に灰色になる
    elif reps % 2 == 0:
        count_down(short_break_sec)
        main_label.config(text="S Break", fg=PINK)
        main_label.update()
    else:
        # if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        main_label.config(text="Work", fg=GREEN)
        main_label.update()
        # canvas.itemconfig(main_label, text="Work", fg=GREEN)
        count_down(work_sec)
        # print("通っている")


def start_button():
    if timer is not None:
        print("Timer is None.")
        return
    start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# 1秒たったら、1秒減らす。60秒たったら、1分減らす。62秒たったら、1分と2秒減らす
# ToDO: 講師の問題点(指摘して良いレベル)：この関数を毎回呼び出すたびに、時間がかかっているので、厳密には1秒以上かかっている（window.afterをなるべく関数の定義の直後に書いたほうがいい）
# TODO: 今回は”window.after"が非同期処理なので回避されているが、もしcount_downのなかで、自身を呼ぶとstackoverflowになる


def count_down(count):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    # count_display = (f"{count_min}:{count_sec}")
    # ToDO: Pad number with zeros (left padding, width 2)
    count_min = "{:0>2d}".format(count // 60)
    count_sec = "{:0>2d}".format(count % 60)
    print(count)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count == 0:
        start_timer()
        # ToDO 2回repsが終わると、一回✅を増やす
        if reps % 2 == 0:
            check_mark = "✅"
            num = reps // 2
            check_marks.config(text=f"{check_mark}" * num)
            check_marks.update()

        # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=200, bg=YELLOW)
# count_down(5)　⭐️ここだと動かない

canvas = Canvas(window, width=220, height=224, bg=YELLOW, highlightthickness=0)  # 偶数にセット

tomato_img = PhotoImage(file="tomato.gif")  # gifだと上手くいくが、pngは上手くいかない
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

# canvas = Canvas(window, width=220, height=224) # 偶数にセット
# canvas.grid(row=2, column=3)
#
# tomato_img = PhotoImage(file="tomato1.png")
# canvas.create_image(100, 112, anchor=NW, image=tomato_img)


# Label
main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
main_label.grid(column=1, row=0)  # 場所を保存している

# Button
# highlightthicknessが効いていないみたい？
start_button = Button(text="Start", highlightthickness=0, command=start_button)
start_button.grid(column=0, row=2)

# Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label
# ToDO: check_marksの部分を、main_labelにしても、main_labelとcheck_marksの二つが維持できているが、
#  上の方のmain_labelにアクセルはできなくなる。（ただ、一回目の表示はされる）→ポインター
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
