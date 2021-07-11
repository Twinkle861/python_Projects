#import library
from tkinter import *
import random

#initialize window
root=Tk()
root.geometry('600x600')
root.resizable(0,0)
root.title('Rock-Paper-Scissors Game')
root.config(bg='LightPink1')

#Name of game
Label(root, text = 'ROCK-PAPER-SCISSORS', font='calibiri 23 bold', bg='LightPink1').place(x=107,y=20)

#user choice
user_choice = StringVar()
Label(root, text = 'Enter your choice : rock or paper or scissor', font='calibiri 17 bold', bg='LightPink1').place(x=50,y=150)
Entry(root, font ='calibiri 17',textvariable=user_choice, bg = 'antiquewhite2').place(x=140,y=190)
    
#result
Label(root, text = 'Result', font='calibiri 17 bold', bg='LightPink1').place(x=235,y=350)

##function to play
Result = StringVar()

def play():
        #computer choice
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = 'rock'
    elif comp_choice ==2:
        comp_choice = 'paper'
    else:
        comp_choice = 'scissor'

    user_pick = user_choice.get()        
    if user_pick == comp_choice:
        Result.set('tie,you both selected same')
    elif user_pick == 'rock' and comp_choice == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_choice == 'scissor':
        Result.set('you win,computer select scissor')
    elif user_pick == 'paper' and comp_choice== 'scissor':
        Result.set('you loose,computer select scissor')
    elif user_pick == 'paper' and comp_choice == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissor' and comp_choice == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissor' and comp_choice == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissor')
    
        
    
# reset
def Reset():
    Result.set("") 
    user_choice.set("")
    comp_choice.set("")

#exit
def Exit():
    root.destroy()


# button
Entry(root, textvariable = Result, font='calibiri 15 bold', bg ='antiquewhite2',width = 45).place(x=40, y = 390,height=40)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=235,y=235)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=140,y=450)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=360,y=450)

root.mainloop()
