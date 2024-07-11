from tkinter import *
import pandas
import random
from time import sleep 


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("translation.csv")
learn = data.to_dict(orient="records")

def nextCard():
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text = "English")
    canvas.itemconfig(card_word, text = current_card['English'])

window = Tk()
window.title("Flash")
window.config(padx= 50,pady=50,bg=BACKGROUND_COLOR)

#Create the Background 
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file ="card_front.png")
canvas.create_image(400,263, image = card_front_img)
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