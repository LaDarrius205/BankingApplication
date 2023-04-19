from tkinter import *
import os
from PIL import ImageTk, Image


### Main Screen
master = Tk()
master.title('Banking App')


def finishRegister():
    ## Grabbing Details
    name = temp_name.get()
    age = temp_age.get()
    email = temp_email.get()
    password = temp_password.get()
    
    ## Filing System
    all_accounts = os.listdir()
    print(all_accounts)

    # To secure registeration data from previous users
    if name == "" or age == "" or email == "" or  password == "":
        notif.config(fg="red",text="***All fields required***")
        return
    print("Registeration Successful")


    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="***Account already exists***")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(email+'\n')
            new_file.write("0")
            new_file.close()
            notif.config(fg='green', text="Account has been created")
       
### Functions
def register():
    ## Variables
    global temp_name
    global temp_age
    global temp_email
    global temp_password
    global notif

    temp_name = StringVar()
    temp_age = StringVar()
    temp_email = StringVar()
    temp_password = StringVar()
   #print("This is the Register screen")

    ###Register Screen... Error not reading
    #Creates a little window once the button is pressed
    register_Screen = Toplevel(master)
    register_Screen.title('Register')


#Labels
    Label(register_Screen, 
          text= 'Please enter your details below to register', 
      font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(register_Screen, text= 'Name', 
      font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(register_Screen, text= 'Age', 
      font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(register_Screen, text= 'Email', 
      font=('Calibri', 12)).grid(row=3, sticky=W,)
    Label(register_Screen, text= 'Password', 
      font=('Calibri', 12)).grid(row=4, sticky=W)
    notif = Label(register_Screen, font=('Calibri', 12))
    notif.grid(row=5, sticky=W)

    #Entries
    Entry(register_Screen, 
          textvariable=temp_name).grid(row=1, column=0)
    Entry(register_Screen, 
          textvariable=temp_age).grid(row=2, column=0)
    Entry(register_Screen, 
          textvariable=temp_email).grid(row=3, column=0)
    Entry(register_Screen, textvariable=temp_password, 
          show = '*').grid(row=4, column=0)


    #Button error <newline> Unexpected Token
    Button(register_Screen, text="Register", command = finishRegister, 
           font = ("Calibri", 12)).grid(row = 5, sticky = N, pady = 10)


def login_session():
    global login_name 
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
           file = open(name,"r")
           file_data = file.read()
           file_data = file_data.split('\n')
           password = file_data[1]
           #Account DashBoard
           if login_password == password:
               login_screen.destroy()
               account_dashboard = Toplevel(master)
               account_dashboard.title('Account Dashboard')

               #Labels
               Label(account_dashboard, text ="Account Dashboard", 
                     font = ("Calibri", 12)).grid(row = 0, sticky = N, pady = 10) 
               Label(account_dashboard, text ="Welcome "+ name , 
                     font = ("Calibri", 12)).grid(row = 1, sticky = N, pady = 10) 
               #Button
               Button(account_dashboard, text = "Personal Details",
                      font =('Calibri', 12), width=30, 
                      command = personal_details).grid(row = 2, sticky = N, padx = 10)
               Button(account_dashboard, text = "Deposit", 
                      font =('Calibri', 12), width=30, 
                      command = deposit).grid(row = 3, sticky = N, padx = 10)
               Button(account_dashboard, text = "Withdraw", 
                      font =('Calibri', 12), width=30, 
                      command = withdraw).grid(row = 4, sticky = N, padx = 10)
               Label(account_dashboard).grid(row = 5, sticky = N, pady = 10)
               return
           else:
                login_notif.config(fg='red', text="Password incorrect!!!")
           return
    login_notif.config(fg='red', text = "No account found ??")

def deposit():
    print( "Deposit")


def withdraw():
    print( "Withdraw")


def personal_details():
    #Variables
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[1]
    details_email = user_details[2]
    details_balance = user_details[4]
    
    # Personal Details Screen
    personal_details = Toplevel(master)
    personal_details.title("Personal Details")

    #Label
    Label(personal_details, text= "Personal Details ", 
          font =('Calibri', 12)).grid(row = 0, sticky = N, padx = 10) 
    Label(personal_details, text= "Name " + details_name, 
          font =('Calibri', 12)).grid(row = 1, sticky = W) 
    Label(personal_details, text= "Age " + details_age, 
          font =('Calibri', 12)).grid(row = 2, sticky = W) 
    Label(personal_details, text= "Email " + details_email, 
          font =('Calibri', 12)).grid(row = 3, sticky = W) 
    Label(personal_details, text= "Balance: $" + details_balance, 
          font =('Calibri', 12)).grid(row = 4, sticky = W)

    



def login():

     ## Variables
     global temp_login_name
     global temp_login_password
     global login_notif
     global login_password
     global login_screen
     
     temp_login_name = StringVar()
     temp_login_password = StringVar()

     ## Login screen
     login_screen = Toplevel(master)
     login_screen.title('Login')

     ## Label
     Label(login_screen, text="Login to your account", 
           font=('Calibri',12)).grid(row=0,sticky=N,pady=10) 
     Label(login_screen, text="Login", 
           font=('Calibri',12)).grid(row=1,sticky=W,pady=10)
     Label(login_screen, text="Password", 
           font=('Calibri',12)).grid(row=2,sticky=W,pady=10)

     ## Note 
     login_notif = Label(login_screen, font = ("Calibri",12))
     login_notif.grid(row = 4, sticky = N)

     ## Entry
     Entry(login_screen, 
           textvariable=temp_login_name).grid(row=1,column=1,padx=5)
     Entry(login_screen, 
           textvariable=temp_login_password, show = '*').grid(row=2,column=1,padx=5)
     Button(login_screen, text="Login", 
            command = login_session, width=15, font =("Calibri", 12)).grid(row=3,sticky=W,padx=5)


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
       command = register).grid(row=3,sticky=N)
Button(master, text='login', 
       font=('Calibri', 12),
       width =20,
       command = login).grid(row=4,sticky=N)



#Button Commands 
 
# Needed for the Gui screen to show 
master.mainloop()


