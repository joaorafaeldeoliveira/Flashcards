from tkinter import *
import pandas
import random
from time import sleep 


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("translation.csv")
learn = data.to_dict(orient="records")
current_card = {} 

def nextCard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text = "English",fill = "black")
    canvas.itemconfig(card_word, text = current_card['English'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text= "Portuguese", fill="white")
    canvas.itemconfig(card_word, text= current_card["Portuguese"],fill="white")
    canvas.itemconfig(card_background, image =card_back_img)

window = Tk()
window.title("Flash")
window.config(padx= 50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


#Create the Background 
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file ="card_front.png")
card_back_img = PhotoImage(file = "card_back.png")
card_background = canvas.create_image(400,263, image = card_front_img)
card_title = canvas.create_text(400,150 ,font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263, font = ("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

#Buttons 
cross_image = PhotoImage(file = "wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command = nextCard )
unknown_button.grid(row=1,column =0)

check_image = PhotoImage(file= "right.png")
check_button = Button(image = check_image,highlightthickness=0, command = nextCard)
check_button.grid(row=1,column=1)

nextCard()


window.mainloop()