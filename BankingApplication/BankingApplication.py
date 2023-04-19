from tkinter import *
import os
from PIL import ImageTk, Image


# Main Screen
master = Tk()
master.title('Banking App')


def finishregister():
    # Grabbing Details
    name = temp_name.get()
    age = temp_age.get()
    email = temp_email.get()
    password = temp_password.get()
    
    # Filing System
    all_accounts = os.listdir()
    print(all_accounts)

       
#Functions
def Register():
    #Variables
    global temp_name
    global temp_age
    global temp_email
    global temp_password

    temp_name = StringVar()
    temp_age = StringVar()
    temp_email = StringVar()
    temp_password = StringVar()
    #print("This is the Register screen")

    ###Register Screen... 
    #Creates a little window once the button is pressed
    registerScreen = Toplevel(master)
    registerScreen.title('Register')


#Labels
    Label(registerScreen, 
          text= 'Please enter your details below to register', 
      font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(registerScreen, text= 'Name', 
      font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(registerScreen, text= 'Age', 
      font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(registerScreen, text= 'Email', 
      font=('Calibri', 12)).grid(row=3, sticky=W,)
    Label(registerScreen, text= 'Password', 
      font=('Calibri', 12)).grid(row=4, sticky=W)

    #Entries
    Entry(registerScreen, 
          textvariable=temp_name).grid(row=1, column=0)
    Entry(registerScreen, 
          textvariable=temp_age).grid(row=2, column=0)
    Entry(registerScreen, 
          textvariable=temp_email).grid(row=3, column=0)
    Entry(registerScreen, textvariable=temp_password, 
          show = '*').grid(row=4, column=0)


    #Button error <newline> Unexpected Token
    #Button(registerScreen, text="Register", command = finishRegister, 
    #       font = ("Calibri", 12).grid(row = 5, sticky = N, pady = 10)


def login():
     print('this is the login page')


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
img = Image.open(r'C:\Users\ladar\source\repos\BankingApplication\Bank-money.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)



# Lables

Label(master, text = 'Custom Banking Beta', 
      font = ('Calibri', 14)).grid(row = 0, sticky = N, pady = 10)
Label(master, text = r'The most secure bank you have probably ever used', 
      font = ('Calibri', 12)).grid(row=1, sticky=N, pady=10)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

# Button
Button(master, text='Register', 
       font=('Calibri', 12),
       width =20 , 
       command = 'Register').grid(row=3,sticky=N)
Button(master, text='Login', 
       font=('Calibri', 12),
       width =20,
       command = 'Login').grid(row=4,sticky=N)



#Button Commands 
 
# Needed for the Gui screen to show 
master.mainloop()


