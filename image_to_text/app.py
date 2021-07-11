
from tkinter import *
import os
from tkinter import filedialog
import time
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import messagebox
import pytesseract

import PIL
#initial window
root = Tk()
root.geometry('600x800')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Image to text')

#heading
Label(root, text = 'Image to text' , font='Verdana 30 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Upload the image :', font ='Verdana 18 ', bg ='#c6ffc1').place(y=120,x=70)

input = None
name = None
#function
def upload():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global input
    global name
    input = filedialog.askopenfile(mode='r', filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg")])
    input = input.name
    if input is not None:
        pb = Progressbar(
            root, 
            orient=HORIZONTAL, 
            length=450, 
            mode='determinate'
            )
        pb.place(x=90, y=270)
        for i in range(5):
            root.update_idletasks()
            pb['value'] += 20
            time.sleep(0.40)
        pb.destroy()
    Label(root, text='Image Uploaded Successfully!',  font='Verdana 15 bold italic' , bg ='#c6ffc1').place(x=140, y=250)


text_data = None
def convert():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global input
    if input==None:
        messagebox.showerror("Error", "First upload an image.")
    img = PIL.Image.open(input) 
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    global text_data
    text_data = pytesseract.image_to_string(img.convert('RGB'), lang='eng')
    messagebox.showinfo("Success", "Image successfully converted to text.")

def Exit():
    root.destroy()

def show():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global text_data
    if text_data == None:
        messagebox.showerror("Error", "First convert to text.")
    messagebox.showinfo("Text", text_data)
    

def x(nme):
    global text_data,name
    if text_data == None:
        messagebox.showerror("Error", "First convert to text.")
    name =nme
    # print(name)
    # print(type(name))
    if name == '':
        name = '1'
    name = name + '.txt'
    file1=open(name,"a")
    file1.writelines(text_data)
    file1.close()
    messagebox.showinfo("Success", "Text file successfully saved with given name else saved with 1.txt.") 

def save():
    Label(root, text='Enter name and whole path(if diff folder) of ',  font='Verdana 15' , bg ='#c6ffc1').place(x=20, y=470)
    Label(root, text='sketch you want image to be saved as',  font='Verdana 15' , bg ='#c6ffc1').place(x=20, y=510)
    Label(root, text='(without extension) and press enter:',  font='Verdana 15' , bg ='#c6ffc1').place(x=20, y=550)
    inputtxt1 = Text(root,height=0.3,width=40, font ='Verdana 13',padx=10,pady=10)
    inputtxt1.place(x=50,y=595)
    global name
    inputtxt1.bind("<Return>", (lambda event: x(inputtxt1.get('1.0', 'end-1c'))))
    # name = inputtxt1.get('1.0', 'end-1c')
    # x(name)

def delete():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global name
    if name == None:
        messagebox.showerror("Error", "First save text file.")
    else:
     os.remove(name)
    messagebox.showinfo("Success", "Deleted File successfully.")

def reset():
    Label(root, text=' ',  font='Verdana 25 bold italic' , bg ='#c6ffc1',width=200).place(x=120, y=240)
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global input,name,text_data
    input = None
    name = None
    text_data = None

# #upload file
Button(root, text ='Select an Image', font ='Verdana 18 ', command = lambda:upload()).place(x=120, y=180, height=50,width=400)
# #Button
Button(root, text = "SAVE FILE" , font = 'Verdana 15 bold', command = save,bg = '#ffc478').place(x=340, y=400, height=40,width=230)
Button(root, text = "CONVERT IMAGE" , font = 'Verdana 15 bold', command = convert,bg = '#ffc478').place(x=200, y=325, height=40,width=210)
Button(root, text = "SHOW TEXT" , font = 'Verdana 15 bold', command = show,bg = '#ffc478').place(x=40, y=400, height=40,width=230)
Button(root, text = "DELETE TEXT" , font = 'Verdana 15 bold', command = delete,bg = '#ffc478').place(x=190, y=670, height=40,width=230)
Button(root, text = "RESET" , font = 'Verdana 15 bold', command = reset,bg = '#ffc478').place(x=20, y=670, height=40,width=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = '#ffc478').place(x=450,y=670, height=40,width=130)


#infinite loop to run program
root.mainloop()