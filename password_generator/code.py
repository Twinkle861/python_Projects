from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.config(bg = '#c6ffc1')

Label(root, text = 'PASSWORD' , font='Verdana 40 bold italic' , bg ='#c6ffc1').place(x = 120,y=40)
Label(root, text = 'GENERATOR' , font='Verdana 40 bold italic' , bg ='#c6ffc1').place(x = 120,y=100)
pass_label = Label(root, text = 'PASSWORD LENGTH(>8 & <32)', font='Verdana 20 italic' , bg ='#c6ffc1').place(x=50,y=200)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 20).place(x=100,y=250,height=40)

# First loop will generate a string of length 4 which is a combination of an uppercase letter, a lowercase letter, digits, and a special symbol and that string will store in password variable.
# The second loop will generate a random string of length entered by the user – 4 and add to the password variable. Here we minus 4 to the length of the user because we already generate the string of length 4.
pass_str = StringVar()
def Generator():
    if pass_len.get()<8 or pass_len.get()>32:
        Label(root, text = 'Please specify correct length' , font='Verdana 10 italic' , bg ='#c6ffc1').place(x =300,y=250,height=20,width=300)
    else:    
        Label(root, text = '' , font='Verdana 10 italic' , bg ='#c6ffc1').place(x =300,y=250,height=20,width=300)
        password = ''
        for x in range (0,4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get()- 4):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).place(x=100,y=300)
Entry(root , textvariable = pass_str).place(x=100,y=350,height = 40)

def Copy_password():
    pyperclip.copy(pass_str.get())

def reset():
    Label(root, text = '' , font='Verdana 10 italic' , bg ='#c6ffc1').place(x =300,y=250,height=20,width=300)
    password = ''
    Entry(root , textvariable ='').place(x=100,y=350,height = 40)

def quit():
    root.destroy()

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).place(x=100,y=410)
Button(root, text = 'RESET', command = reset).place(x=110,y=460)
Button(root, text = 'QUIT', command = quit).place(x=180,y=460)
Label(root, text="This password has combination of lowercase,uppercase," ,font='Verdana 10 bold italic' , bg ='#c6ffc1').place(x =40,y=530)
Label(root, text="no. and special character" ,font='Verdana 10 bold italic' , bg ='#c6ffc1').place(x =40,y=560)
#infinite loop to run program
root.mainloop()