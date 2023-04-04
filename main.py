import tkinter as tk
import pandas as pd
import random

# Global variables
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
F_WORD=""

# Importing data
data = pd.read_csv('./data/french_words.csv')

# Random_word function


def random_word():
    global data, card, word_label, F_WORD

    F_WORD = random.choice(data['French'])
    card.itemconfigure(card_image, image=card_front_image)
    card.itemconfigure(language_label, text=f'French', fill='black')
    card.itemconfigure(word_label, text=f'{F_WORD}', fill='black')
    window.after(3000, func=show_translation)


def show_translation():
    global card_back_image, card, data, F_WORD

    e_word = data.English[data['French'] == F_WORD].values
    card.itemconfigure(language_label, text='English', fill='white')
    card.itemconfigure(card_image, image=card_back_image)
    card.itemconfigure(word_label, text=e_word[0], fill='white')


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
                           command=random_word)
correct_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                         command=random_word)
wrong_button.grid(column=0, row=1)

random_word()



window.mainloop()
