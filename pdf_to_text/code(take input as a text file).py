#import libraries
import PyPDF2
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from tkinter import filedialog
import time
from tkinter.ttk import Progressbar
from tkinter import ttk

#initial window

root = Tk()
root.geometry('850x900')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('pdf to text')


#heading
Label(root, text = 'pdf file to text' , font='Verdana 40 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Upload the pdf file :', font ='Verdana 20 ', bg ='#c6ffc1').place(y=150,x=100)



input = None
#function
def upload():
    global input
    global num
    global name
    input = filedialog.askopenfile(mode='r', filetypes=[('pdf Files', '*pdf')])
    Label(root, text=' ',  font='Verdana 25 bold italic' , bg ='#c6ffc1',width=200).place(x=150, y=310)
    input = input.name
    if input is not None:
        pb = Progressbar(
            root, 
            orient=HORIZONTAL, 
            length=500, 
            mode='determinate'
            )
        pb.place(x=160, y=320)
        for i in range(5):
            root.update_idletasks()
            pb['value'] += 20
            time.sleep(0.50)
        pb.destroy()
        Label(root, text='File Uploaded Successfully!',  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=150, y=310)

Label(root, text='Enter number of lines you want to read(enter all if want all)',  font='Verdana 20 ' , bg ='#c6ffc1').place(x=20, y=380)
inputtxt = Text(root,height=1,width=50, font ='Verdana 15',padx=10,pady=10)
inputtxt.place(x=80,y=425)
Label(root, text='Enter name and whole path(if diff folder) of text file you',  font='Verdana 20' , bg ='#c6ffc1').place(x=20, y=480)
Label(root, text='want pdf to be saved as',  font='Verdana 20' , bg ='#c6ffc1').place(x=20, y=525)
inputtxt1 = Text(root,height=1,width=50, font ='Verdana 15',padx=10,pady=10)
inputtxt1.place(x=80,y=580)
        

def pdf_to_text():
    global input
    if input==None:
        Label(root, text='Please upload pdf file first',  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=150, y=310)
    num = inputtxt.get('1.0', 'end-1c')
    name = inputtxt1.get('1.0', 'end-1c') 
    input = str(input)
    pdf=open(input,'rb')
    reader=PyPDF2.PdfFileReader(pdf)
    x = reader.numPages
    if(num == 'all' or num ==''):
        num = x
        num = int(num)
    elif int(num) > x:
        num = x
        num = int(num)
    else:
        num = int(num) 
    pageobj=reader.getPage(num-1)
    text=pageobj.extractText()
    if name == '':
        name = 'text'
    p1 = name + '.txt'
    file1=open(p1,"a")
    file1.writelines(text)
    file1.close()
    Label(root, text='Done and saved file with given name',  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=100, y=310)

def Exit():
    root.destroy()


# #upload file
Button(root, text ='Select a .pdf file', font ='Verdana 20 ', command = lambda:upload()).place(x=200, y=230, height=60,width=400)
# #Button

Button(root, text = "CONVERT AND SAVE TEXT FILE" , font = 'Verdana 20 bold', command = pdf_to_text).place(x=40, y=650, height=60,width=550)

Button(root,text = 'EXIT',font = 'Verdana 20 bold' , command = Exit, bg = '#ffc478').place(x=640,y=650, height=60,width=120)


#infinite loop to run program
root.mainloop()
