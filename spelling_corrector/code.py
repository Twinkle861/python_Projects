# import libraries

from tkinter import *
from textblob import TextBlob


#window

root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Typed spell_check')


#heading
Label(root, text = 'SPELL CORRECTION' , font='Verdana 40 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Enter Text :', font ='Verdana 20 ', bg ='#c6ffc1').place(y=120,x=40)


#text variable
Msg = StringVar()


#Entry field
entry_field = Text(root,height=6,width=68, font ='Verdana 10',padx=3,pady = 3)
entry_field.place(x=15 , y=170)


#functions

def spell_correct():
    Message = entry_field.get("1.0",'end-1c')
    if Message == None or Message == "":
        Label(root, text="enter text first",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=280,width=600,height=100)
    else:
        res = Message.split()
        scorrect=""
        for i in res:
            correct = TextBlob(i).correct()
            scorrect+=str(correct)+" "
        Label(root, text=scorrect+"  ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=280,width=600,height=100)

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    entry_field.delete("1.0", END)
    Label(root, text="",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=280,width=600,height=100)

#Button
Button(root, text = 'Convert', font = 'Verdana 20 bold', command = spell_correct).place(x=100, y=400, height=60,width=150)
Button(root, text = 'RESET', font='Verdana 20 bold', command = Reset).place(x=310 , y =400, height=60,width=120)

Button(root,text = 'EXIT',font = 'Verdana 20 bold' , command = Exit, bg = '#ffc478').place(x=200,y=480, height=60,width=120)


#infinite loop to run program
root.mainloop()
