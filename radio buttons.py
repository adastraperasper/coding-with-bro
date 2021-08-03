# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ['air',"sea","land"]

def join():
    if (x.get()==0):
        print("you joined the airforce")

    elif (x.get()==1):
        print("You joined the navy")

    elif (x.get()==2):
        print("You joined the army")

    else:
        print("you did not join")


window = Tk()

airImage=PhotoImage(file="air.png")
seaImage=PhotoImage(file="sea.png")
landImage=PhotoImage(file="land.png")

foodImages =[airImage,seaImage,landImage]

x = IntVar()
for index in range(len(food)):
     radiobutton = Radiobutton(window,
                               text=food[index], #adds text to radio buttons
                               variable=x, #groups radiobuttons
                               value= index,
                               padx =25,
                               font=("Impact",40),
                               image = foodImages[index],
                               compound = 'left',# adds image and text
                               indicatoron = 0, #width of radiobutton
                               width = 200,
                               command = join

                               )
     
     radiobutton.pack(anchor=W)

window.mainloop()
