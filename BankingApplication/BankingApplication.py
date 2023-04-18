
import pandas 
import numpy 
import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk, Image


# Main Screen
master = Tk()
master.title("Banking App")


## Check Path using os
#path = r"C:\Users\ladar\source\repos\BankingApplication"
#l = os.listdir(path)
#print(l)
#for e in l:   
#    print(e)
#    # Comma Seperated to see file names
#    print(e.split('.'))
#    # To print the extension seperate
#    print (f"File name {e} and the extension is {e.split('.')}")
#    # Splitext Seprate 
#    print (f"File name {e} and the extension is {os.path.splitext(e)}")



# Image import
img = Image.open(r"C:\Users\ladar\source\repos\BankingApplication\Bank-money.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)



# Lables

Label(master, text = "Custom Banking Beta", 
      font = ("Calibri", 14)).grid(row = 0, sticky = N, pady = 10)
Label(master, text = " the most secure bank you've probably ever used", 
      font = ("Calibri", 12)).grid(row=1, sticky=N, pady=10)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

# Button
Button(master, text="Register", 
       font=('Calibri',12),
       width =20).grid(row=3,sticky=N)
Button(master, text="Login", 
       font=('Calibri',12),
       width =20).grid(row=4,sticky=N)



master.mainloop()

