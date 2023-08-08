import random
from tkinter import *
import pandas
from os.path import exists

BACKGROUND_COLOR = "#B1DDC6"

if exists("data/words_to_learn.csv"):
    data = pandas.read_csv("data/words_to_learn.csv")
else:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def new_word():
    global current_card, flip_timer
    # Cleanup
    cv.delete("lang_word")
    cv.delete("lang")
    cv.itemconfig(background_card, image=background_front)

    # Get new word
    current_card = random.choice(to_learn)
    cv.itemconfig(lang, text="French", fill="black")
    cv.itemconfig(lang_word, text=current_card["French"], fill="black")
    if flip_timer:
        window.after_cancel(flip_timer)
    flip_timer = cv.after(5000, show_back)


def show_back():
    global current_card

    # Clean Up
    cv.delete("lang_word")
    cv.delete("lang")

    # Show back
    cv.itemconfig(background_card, image=background_back)
    cv.itemconfig(lang, text="English", fill="white")
    cv.itemconfig(lang_word, text=current_card["English"], fill="white")


def is_known():
    global to_learn, current_card
    to_learn.remove(current_card)
    print(len(to_learn))

    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)

    new_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

cv = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_front = PhotoImage(file="images/card_front.png")
background_back = PhotoImage(file="images/card_back.png")
center_x = 800 / 2
center_y = 525 / 2
background_card = cv.create_image(center_x, center_y, image=background_front)

lang = cv.create_text(center_x, 150, text="", font=("Arial", 40, "italic"))
lang_word = cv.create_text(center_x, 253, text="", font=("Arial", 60, "bold"))

cv.grid(row=0, column=0, columnspan=2)

img_w = PhotoImage(file="images/wrong.png")
button_w = Button(image=img_w, highlightthickness=0, command=new_word)
button_w.grid(row=1, column=0)

img_r = PhotoImage(file="images/right.png")
button_r = Button(image=img_r, highlightthickness=0, command=is_known)
button_r.grid(row=1, column=1)

flip_timer = None

new_word()

window.mainloop()
