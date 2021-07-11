# import libraries

from tkinter import *
from textblob import TextBlob
import os
from tkinter import filedialog
import time
from tkinter.ttk import Progressbar
from tkinter import ttk

#initial window

root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Spell Correct')


#heading
Label(root, text = 'Spelling Correction' , font='Verdana 40 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Upload the text file Text :', font ='Verdana 20 ', bg ='#c6ffc1').place(y=120,x=40)


Msg=StringVar()
Message=None
#function
def upload():
    Label(root, text=" ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=50, y=305,width=600,height=50)
    input = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
    #print(input)

    if input is not None:
        pb = Progressbar(
            root, 
            orient=HORIZONTAL, 
            length=400, 
            mode='determinate'
            )
        pb.place(x=100, y=295)
        for i in range(5):
            root.update_idletasks()
            pb['value'] += 20
            time.sleep(0.50)
        pb.destroy()
        Label(root, text='File Uploaded Successfully!',  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=50, y=305)
        global Message 
        Message=''       
        for word in input:         
            Message = Message +" " + word
        #print(Message)

def Spell_correct():
    global Message 
    if Message == None or Message == "":
        Label(root, text="Select a file first ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=305,width=600,height=50)
    else:
        res = Message.split()
        f= open("correct.txt","a+")
        f.truncate(0)
        for i in res:
            scorrect = TextBlob(i).correct()
            print(scorrect)
            f.write(str(scorrect) + " ")
        f.close()
        Label(root, text="Changed file is saved ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=305,width=600,height=50)

def Exit():
    root.destroy()

def Reset():
    if Message == None or Message == "":
        Label(root, text="Make changes first",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=20, y=305,width=600,height=50)
    else:
        Msg.set("")
        Label(root, text=" ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=50, y=305,width=600,height=50)
        os.remove('correct.txt')

#upload file
Button(root, text ='Select a .txt file', font ='Verdana 20 ', command = lambda:upload()).place(x=100, y=200, height=60,width=400)
#Button

Button(root, text = "MAKE CHANGES" , font = 'Verdana 20 bold', command = Spell_correct).place(x=120, y=400, height=60,width=340)
Button(root, text = 'RESET', font='Verdana 20 bold', command = Reset).place(x=130, y =490, height=60,width=120)

Button(root,text = 'EXIT',font = 'Verdana 20 bold' , command = Exit, bg = '#ffc478').place(x=340,y=490, height=60,width=120)


#infinite loop to run program
root.mainloop()
