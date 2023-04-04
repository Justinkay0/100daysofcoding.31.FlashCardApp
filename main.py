import tkinter as tk
import pandas as pd
import random

# Global variables
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
f_word = ""

# Importing data
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')

# Random_word function


def random_word():
    global data, card, word_label, f_word

    f_word = random.choice(data['French'])
    card.itemconfigure(card_image, image=card_front_image)
    card.itemconfigure(language_label, text=f'French', fill='black', font=LANGUAGE_FONT)
    card.itemconfigure(word_label, text=f'{f_word}', fill='black', font=WORD_FONT)
    window.after(3000, func=show_translation)


# flip card function
def show_translation():
    global card_back_image, card, data, f_word

    e_word = data.English[data['French'] == f_word].values
    card.itemconfigure(language_label, text='English', fill='white')
    card.itemconfigure(card_image, image=card_back_image)
    card.itemconfigure(word_label, text=e_word[0], fill='white')


# known words functions
def known_word():
    global data
    data = data[data.French != f_word]
    data.to_csv("./data/words_to_learn.csv", index=False)
    random_word()


# Window UI
window = tk.Tk()
window.title('flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card UI
card_front_image = tk.PhotoImage(file='./images/card_front.png')
card_back_image = tk.PhotoImage(file='./images/card_back.png')
card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 268, image=card_front_image)
card.grid(column=0, row=0, columnspan=2)

# Create labels
language_label = card.create_text(400, 150, text='', font=LANGUAGE_FONT)
word_label = card.create_text(400, 263, text=f"", font=WORD_FONT)

# Buttons
correct_image = tk.PhotoImage(file='./images/right.png')
correct_button = tk.Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                           command=known_word)
correct_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                         command=random_word)
wrong_button.grid(column=0, row=1)

# Initialising game
random_word()
print(f_word)

window.mainloop()
