from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- VOCAB WORDS ------------------------------- #
new_choice = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


def new_word():
    global new_choice, flip_timer, word_dict
    window.after_cancel(flip_timer)
    new_choice = choice(word_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_choice["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_choice["English"], fill="white")

# ---------------------------- KNOWN WORD ------------------------------- #


def known_word():
    global word_dict
    word_dict.remove(new_choice)
    new_df = pandas.DataFrame(word_dict)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    new_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="word", font=("Arial", 60, "italic"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

new_word()

window.mainloop()
