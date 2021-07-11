# 7)first read it ,conevrt into grayscale->np.dot
# create blurred img->gaussian filter,sigma tell intensity of blurness
# dodge convert to sketch,save using imwrite

import numpy as np
import imageio
import scipy.ndimage
import cv2
from tkinter import *
import os
from tkinter import filedialog
import time
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import messagebox
#initial window
root = Tk()
root.geometry('600x800')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Image to sketch')

#heading
Label(root, text = 'Image to sketch' , font='Verdana 30 bold italic' , bg ='#c6ffc1').pack(pady=20)


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


def grayscale(rgb):
    	return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
	result=front*255/(255-back)
	result[result>255]=255
	result[back==255]=255
	return result.astype('uint8')

r = []
def convert():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global input
    if input==None:
        messagebox.showerror("Error", "First upload an image.")
    s=imageio.imread(input)
    g=grayscale(s)
    i=255-g
    b=scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    global r
    r=dodge(b,g)
    messagebox.showinfo("Success", "Image successfully converted to sketch.")

def Exit():
    root.destroy()

def show():
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global r
    if len(r)==0:
        messagebox.showerror("Error", "First convert to sketch.")
    cv2.imshow("sketch",r)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

def x(nme):
    global r,name
    if len(r)==0:
        messagebox.showerror("Error", "First convert to sketch.")
    name =nme
    # print(name)
    # print(type(name))
    if name == '':
        name = '1'
    name = name + '.png'
    cv2.imwrite(name,r)
    messagebox.showinfo("Success", "Image successfully saved with given name else saved with 1.png.") 

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
        messagebox.showerror("Error", "First save image.")
    else:
     os.remove(name)
    messagebox.showinfo("Success", "Deleted File successfully.")

def reset():
    Label(root, text=' ',  font='Verdana 25 bold italic' , bg ='#c6ffc1',width=200).place(x=120, y=240)
    Label(root, text=' ',  font='Verdana 27 bold italic' , bg ='#c6ffc1',width=600,height =4).place(x=20, y=470)
    global input,name,r
    input = None
    name = None
    r = []

# #upload file
Button(root, text ='Select an Image', font ='Verdana 18 ', command = lambda:upload()).place(x=120, y=180, height=50,width=400)
# #Button
Button(root, text = "SAVE IMAGE" , font = 'Verdana 15 bold', command = save,bg = '#ffc478').place(x=340, y=400, height=40,width=230)
Button(root, text = "CONVERT IMAGE" , font = 'Verdana 15 bold', command = convert,bg = '#ffc478').place(x=200, y=325, height=40,width=210)
Button(root, text = "SHOW IMAGE" , font = 'Verdana 15 bold', command = show,bg = '#ffc478').place(x=40, y=400, height=40,width=230)
Button(root, text = "DELETE IMAGE" , font = 'Verdana 15 bold', command = delete,bg = '#ffc478').place(x=190, y=670, height=40,width=230)
Button(root, text = "RESET" , font = 'Verdana 15 bold', command = reset,bg = '#ffc478').place(x=20, y=670, height=40,width=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = '#ffc478').place(x=450,y=670, height=40,width=130)


#infinite loop to run program
root.mainloop()