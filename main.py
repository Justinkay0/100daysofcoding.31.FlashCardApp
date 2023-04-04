import tkinter as tk

# Global variables
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

# Window UI
window = tk.Tk()
window.title('flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card UI
card_front_image = tk.PhotoImage(file='./images/card_front.png')
card_front = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front.create_image(400, 268, image=card_front_image)
card_front.grid(column=0, row=0, columnspan=2)

# Labels
language_label = tk.Label(text='French', font=LANGUAGE_FONT, fg='black', bg='white')
language_label.place(x=325, y=150)

word_label = tk.Label(text='word', font=WORD_FONT, fg='black', bg='white')
word_label.place(x=325, y=263)

# Buttons
correct_image = tk.PhotoImage(file='./images/right.png')
correct_button = tk.Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
correct_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
