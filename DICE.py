import random
import tkinter as tk

from PIL import ImageTk, Image
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
root=tk.Tk()
root.title("DICE ROLLING")
root.geometry('250x300')
root.resizable(height=False,width=False)

dices=["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
def dice_Rolling():
    dice=Image.open(random.choice(dices))
    dice=dice.resize((250,250),Image.ANTIALIAS)
    number=ImageTk.PhotoImage(dice)
# ++++++++++++++++++++LABEL++++++++++++++++++++++
    lbl1=tk.Label(root,image=number)
    lbl1.image=number
    lbl1.grid(row=0)
# +++++++++BUTTON++++++++++++++++++++
btn=tk.Button(root,text="ROLL THE DICE",bg='grey',command=dice_Rolling,border=3)
btn.grid(row=3,padx=25,pady=6,ipady=5)

root.mainloop()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
