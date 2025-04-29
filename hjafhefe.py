import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from PIL import Image, ImageTk
import datetime
from tkinter import font
from tkinter import Toplevel, Frame, ttk
from tkinter import filedialog
import os
import pymysql

root = tk.Tk()
root.title("Mall Management System")
root.geometry("1920x1080")
root.configure(bg="#fff")
root.resizable(False, False)
button_font = font.Font(family="Microsoft Yahei UI Light", size=18,weight="bold")
user = None
Model=None
no=None
passi = None
box=None
s=None
satch=0
satch1=None
sh=None
sh1=None
k=None
delete1=None
#For Parking
parkingtotal=700
parkingtaken=0
ticket=None
parkingavailable=None
age=None

def connectivity(q):
    try:
        db1 = pymysql.connect(host = "localhost", user = "root", password = "Jashan50788", db = "mall_system")
        print("Successfully Connected!")
    except:
        print("Database connection error!")

    cur = db1.cursor()
    cur.execute(q)
    db1.commit()
    print(cur.fetchall())


def signin2():
    

    
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
    image8 = Image.open("admin.jpg")
    resized_image8 = image8.resize((200, 200))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img8, bg="black", fg="white", border=0, command=admin1).place(x=50, y=600)
 

    image1 = Image.open("user.jpg")
    resized_image1 = image1.resize((200, 200))  # Adjust the width and height as needed
    img1 = ImageTk.PhotoImage(resized_image1)# int this add a white frame then black background %%%%%%%%
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img1 , bg="white", fg="white", border=0, command=user1).place(x=420, y=600)

    image2 = Image.open("shopkeeper.jpg")
    resized_image2 = image2.resize((200, 200))  # Adjust the width and height as needed
    img2 = ImageTk.PhotoImage(resized_image2)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img2 , bg="black", fg="white", border=0, command=shopkeeper1).place(x=800, y=600)

    image3 = Image.open("arcade.jpg")
    resized_image3 = image3.resize((200, 200))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image3)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img3 , bg="black", fg="white", border=0, command=arcade1).place(x=1120, y=600)


    image4 = Image.open("parking.jpg")
    resized_image4 = image4.resize((200, 200))  # Adjust the width and height as needed
    img4 = ImageTk.PhotoImage(resized_image4)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img4 , bg="black", fg="white", border=0, command=parking1).place(x=1420, y=600)

    image5 = Image.open("event.jpg")
    resized_image5 = image5.resize((200, 200))  # Adjust the width and height as needed
    img5 = ImageTk.PhotoImage(resized_image5)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img5 , bg="black", fg="white", border=0, command=event1).place(x=1700, y=600)

    label2 = tk.Label(screen, text="ADMIN", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=80, y=850)

    label3 = tk.Label(screen, text="USER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label3.place(x=480, y=850)


    label4 = tk.Label(screen, text="SHOPKEEPER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label4.place(x=810, y=850)


    label5 = tk.Label(screen, text="ARCADE", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label5.place(x=1160, y=850)

    label6 = tk.Label(screen, text="PARKING", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label6.place(x=1450, y=850)


    label7 = tk.Label(screen, text="EVENTS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label7.place(x=1740, y=850)



    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)



    screen.mainloop()
def signin4():
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mallll.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
    image8 = Image.open("admin.jpg")
    resized_image8 = image8.resize((200, 200))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img8, bg="black", fg="white", border=0, command=admin1).place(x=50, y=600)
 

    image1 = Image.open("user.jpg")
    resized_image1 = image1.resize((200, 200))  # Adjust the width and height as needed
    img1 = ImageTk.PhotoImage(resized_image1)# int this add a white frame then black background %%%%%%%%
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img1 , bg="white", fg="white", border=0, command=user1).place(x=420, y=600)

    image2 = Image.open("shopkeeper.jpg")
    resized_image2 = image2.resize((200, 200))  # Adjust the width and height as needed
    img2 = ImageTk.PhotoImage(resized_image2)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img2 , bg="black", fg="white", border=0, command=shopkeeper1).place(x=800, y=600)

    image3 = Image.open("arcade.jpg")
    resized_image3 = image3.resize((200, 200))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image3)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img3 , bg="black", fg="white", border=0, command=arcade1).place(x=1120, y=600)


    image4 = Image.open("parking.jpg")
    resized_image4 = image4.resize((200, 200))  # Adjust the width and height as needed
    img4 = ImageTk.PhotoImage(resized_image4)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img4 , bg="black", fg="white", border=0, command=parking1).place(x=1420, y=600)

    image5 = Image.open("event.jpg")
    resized_image5 = image5.resize((200, 200))  # Adjust the width and height as needed
    img5 = ImageTk.PhotoImage(resized_image5)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img5 , bg="black", fg="white", border=0, command=event1).place(x=1700, y=600)

    label2 = tk.Label(screen, text="ADMIN", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=80, y=850)

    label3 = tk.Label(screen, text="USER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label3.place(x=480, y=850)


    label4 = tk.Label(screen, text="SHOPKEEPER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label4.place(x=810, y=850)


    label5 = tk.Label(screen, text="ARCADE", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label5.place(x=1160, y=850)

    label6 = tk.Label(screen, text="PARKING", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label6.place(x=1450, y=850)


    label7 = tk.Label(screen, text="EVENTS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label7.place(x=1740, y=850)



    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    screen
    

def signin3():
    image = Image.open("signin2.jpg")
    resized_image = image.resize((1920,1080 ))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(root, image=img, bg="blue").place(x=0, y=0)

    image4 = Image.open("userr.jpg")
    resized_image4 = image4.resize((200, 100))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image4)
    root.configure(bg="#fff")
   # Button(root, width=200, image=img3 ,  fg="white", border=0, ).place(x=530, y=930)

    image5 = Image.open("admin1.jpg")
    resized_image5 = image5.resize((200, 100))  # Adjust the width and height as needed
    img5 = ImageTk.PhotoImage(resized_image5)
    root.configure(bg="#fff")
   # Button(root, width=200, image=img5 ,  fg="white", border=0, ).place(x=1250, y=930)


    screen.mainloop()

    
def admin1():
    global s
    s="admin"
    signin1()

def user1():
    global s
    s="user"
    signin1()
def shopkeeper1():
    global s
    s="shopkeeper"
    signin111()
        

def arcade1():
    global s
    s="arcade"
    signin1()
def parking1():
    global s
    s="parking"
    signin1()
def event1():
    global s
    s="event"
    signin1()   

def signin1():
    global user, passi,s
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    if s=="admin":
        
        image8 = Image.open("admin.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="user":
            
        image8 = Image.open("user.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)


    elif s=="shopkeeper":
            
        image8 = Image.open("shopkeeper.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="arcade":
            
        image8 = Image.open("arcade.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="parking":
            
        image8 = Image.open("parking.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="event":
            
        image8 = Image.open("event.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)
    

 

    


    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)

    heading = tk.Label(frame, text="Sign IN", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Username")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        passi.delete(0, 'end')

    def on_leave(e):
        name = passi.get()
        if name == "":
            passi.insert(0, "Password")

    passi = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passi.place(x=75, y=140)
    passi.insert(0, "Password")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)
    passi.bind("<FocusIn>", on_enter)
    passi.bind("<FocusOut>", on_leave)


    

    Button(frame, width=39, pady=7, text="Sign IN", bg="#57a1f8", fg="white", border=0, command=signinclassify).place(x=75, y=200)
    label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    label.place(x=75, y=240)
    sign_in = Button(frame, width=6, text="Sign UP", border=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft Yahei UI Light", 11), command=signup1)
    sign_in.place(x=250, y=240)



    screen.mainloop()

    
def signinclassify():
    print("yo1:")
    if s=="admin":
        print("yo2:")
        signinadmin()
    if s=="user":
        signinuser()
    if s=="shopkeeper":
        print("done")
        signinshopkeeper(satch)
    if s=="arcade":
        signinarcade()
    if s=="parking":
        signinparking()
        print("yo")
    if s=="event":
        signinevent()
        

def signinadmin():
    c=0
    print("yo")
    username = user.get()
    password = passi.get()
    with open("admin.csv", "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
                break
        if c>0:
            screen = Toplevel(root)
            screen.title("App")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")
            Label(screen, text='Hello').pack()
            screen.mainloop()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")
    
def signinuser():
    c=0
    username = user.get()
    password = passi.get()
    with open("user.csv", "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
        if c>0:
            userdisplay()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")

def signinshopkeeper(satch):
    if satch ==1:
        j="nike.csv"
    elif satch==2:
        j="gucci.csv"
    elif satch==3:
        j="adidas.csv"
    elif satch==4:
        j="puma.csv"
    print("uye")
        
    c=0
    username = user.get()
    password = passi.get()
    with open(j, "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
        if c>0:
            shopcheck()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")

def signinarcade():
    c=0
    username = user.get()
    password = passi.get()
    with open("arcade.csv", "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
        if c>0: 
            arcade()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")
def signinparking():
    c=0
    username = user.get()
    password = passi.get()
    with open("parking.csv", "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
                print("yo")
        if c>0:
            parking()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")
def signinevent():
    c=0
    username = user.get()
    password = passi.get()
    with open("event.csv", "r") as f:
        csvobj = csv.reader(f)
        for line in csvobj:
            if line[0] == username and line[1] == password:
                c+=1
        if c>0:
            screen = Toplevel(root)
            screen.title("App")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")
            Label(screen, text='Hello').pack()
            screen.mainloop()
         
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")
#--------------------------------------
#signin basic layout over , Ab bas function banake dalne hai

def signup2():

    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
    image8 = Image.open("admin.jpg")
    resized_image8 = image8.resize((200, 200))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=50, y=600)
 

    image1 = Image.open("user.jpg")
    resized_image1 = image1.resize((200, 200))  # Adjust the width and height as needed
    img1 = ImageTk.PhotoImage(resized_image1)# int this add a white frame then black background %%%%%%%%
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img1 , bg="white", fg="white", border=0, command=user11).place(x=420, y=600)

    image2 = Image.open("shopkeeper.jpg")
    resized_image2 = image2.resize((200, 200))  # Adjust the width and height as needed
    img2 = ImageTk.PhotoImage(resized_image2)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img2 , bg="black", fg="white", border=0, command=shopkeeper11).place(x=800, y=600)

    image3 = Image.open("arcade.jpg")
    resized_image3 = image3.resize((200, 200))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image3)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img3 , bg="black", fg="white", border=0, command=arcade11).place(x=1120, y=600)


    image4 = Image.open("parking.jpg")
    resized_image4 = image4.resize((200, 200))  # Adjust the width and height as needed
    img4 = ImageTk.PhotoImage(resized_image4)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img4 , bg="black", fg="white", border=0, command=parking11).place(x=1420, y=600)

    image5 = Image.open("event.jpg")
    resized_image5 = image5.resize((200, 200))  # Adjust the width and height as needed
    img5 = ImageTk.PhotoImage(resized_image5)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img5 , bg="black", fg="white", border=0, command=event11).place(x=1700, y=600)

    label2 = tk.Label(screen, text="ADMIN", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=80, y=850)

    label3 = tk.Label(screen, text="USER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label3.place(x=480, y=850)


    label4 = tk.Label(screen, text="SHOPKEEPER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label4.place(x=810, y=850)


    label5 = tk.Label(screen, text="ARCADE", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label5.place(x=1160, y=850)

    label6 = tk.Label(screen, text="PARKING", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label6.place(x=1450, y=850)


    label7 = tk.Label(screen, text="EVENTS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label7.place(x=1740, y=850)



    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign Up AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)



    screen.mainloop()

    #---------------------------------------------------------
# Asigning roles
def admin11():
    global s
    s="admin"
    signup()

def user11():
    global s
    s="user"
    signup()
def shopkeeper11():
    global s
    s="shopkeeper"
    signupss()
        

def arcade11():
    global s
    s="arcade"
    signup()
def parking11():
    global s
    s="parking"
    signup()
def event11():
    global s
    s="event"
    signup() 
def signup():
    global user, passi,passiconfirm

    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    if s=="admin":
        
        image8 = Image.open("admin.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="user":
            
        image8 = Image.open("user.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)



    elif s=="arcade":
            
        image8 = Image.open("arcade.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="parking":
            
        image8 = Image.open("parking.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    elif s=="event":
            
        image8 = Image.open("event.jpg")
        resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
        img8 = ImageTk.PhotoImage(resized_image8)
        screen.configure(bg="#fff")
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)
    

 

    


    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign Up AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)

    heading = tk.Label(frame, text="Sign UP", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Username")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        passi.delete(0, 'end')

    def on_leave(e):
        name = passi.get()
        if name == "":
            passi.insert(0, "Password")

    passi = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passi.place(x=75, y=140)
    passi.insert(0, "Password")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)
    passi.bind("<FocusIn>", on_enter)
    passi.bind("<FocusOut>", on_leave)

    def on_enter(e):
        passiconfirm.delete(0, 'end')

    def on_leave(e):
        name = passiconfirm.get()
        if name == "":
            passiconfirm.insert(0, "Confirm Password")

    passiconfirm = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passiconfirm.place(x=75, y=200)
    passiconfirm.insert(0, "Confirm Password")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=225)
    passiconfirm.bind("<FocusIn>", on_enter)
    passiconfirm.bind("<FocusOut>", on_leave)



    

    Button(frame, width=39, pady=7, text="sign up", bg="#57a1f8", fg="white", border=0, command=signup1).place(x=75, y=290)
    label = Label(frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    label.place(x=75, y=330)
    sign_in = Button(frame, width=6, text="Sign IN", border=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft Yahei UI Light", 11), command=signin1)
    sign_in.place(x=250, y=330)



    screen.mainloop()

def signupss():
    global user, passi, passiconfirm, s, satch1

    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)

    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    for x, pos in zip(range(220, 1800, 360), range(220, 1800, 360)):#replace thus with original 
        tk.Frame(frame1, width=5, height=50, bg="black").place(x=pos, y=0)

    label = tk.Label(screen, text="Sign Up AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font, command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font, command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)

    heading = tk.Label(frame, text="Sign UP", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def configure_entry(entry, placeholder):
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end') if entry.get() == placeholder else None)
        entry.bind("<FocusOut>", lambda e: entry.insert(0, placeholder) if entry.get() == "" else None)
        entry.insert(0, placeholder)

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    configure_entry(user, "Username")
    user.place(x=75, y=80)
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)

    passi = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    configure_entry(passi, "Password")
    passi.place(x=75, y=140)
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)

    passiconfirm = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    configure_entry(passiconfirm, "Confirm Password")
    passiconfirm.place(x=75, y=200)
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=225)

    if s == "shopkeeper":
        image8 = Image.open("shopkeeper.jpg")
        resized_image8 = image8.resize((400, 400))
        img8 = ImageTk.PhotoImage(resized_image8)
        Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

        # Checkbox variables
        checkbox_var = tk.IntVar()
        checkbox_var1 = tk.IntVar()
        checkbox_var2 = tk.IntVar()
        checkbox_var3 = tk.IntVar()

        # Checkboxes for brand selection
        tk.Checkbutton(frame, text="Nike", variable=checkbox_var).place(x=75, y=250)
        tk.Checkbutton(frame, text="GUCCI", variable=checkbox_var1).place(x=180, y=250)
        tk.Checkbutton(frame, text="adidas", variable=checkbox_var2).place(x=75, y=280)
        tk.Checkbutton(frame, text="Puma", variable=checkbox_var3).place(x=180, y=280)

        # Function to check which brand is selected
        def check_selection():
            global satch1
            if checkbox_var.get() == 1:
                satch1 = 1
                print("Start")
            elif checkbox_var1.get() == 1:
                satch1 = 2
            elif checkbox_var2.get() == 1:
                satch1 = 3
            elif checkbox_var3.get() == 1:
                satch1 = 4
            else:
                satch1 = None
                print(f"Selected brand: {satch1 if satch1 else 'No selection'}")

    # Button to check the selection
        tk.Button(frame, text="Check Selection", command=check_selection).place(x=250, y=250)


    Button(frame, width=39, pady=7, text="sign up", bg="#57a1f8", fg="white", border=0, command=signup1).place(x=75, y=290)
    Label(frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 11)).place(x=75, y=330)
    Button(frame, width=6, text="Sign IN", border=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft Yahei UI Light", 11), command=signin1).place(x=250, y=330)

    screen.mainloop()

    
    
    
    
def signup1():
    global satch1
    username = user.get()
    password = passi.get()
    confirmpass = passiconfirm.get()

    if password == confirmpass and s == "user":
        l = [username, password, s]
        with open("user.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(l)
    elif password == confirmpass and s == "admin":
        l = [username, password, s]
        with open("admin.csv", "a", newline="") as f1:
            writer = csv.writer(f1)
            writer.writerow(l)
    elif password == confirmpass and s == "shopkeeper" and satch1==1:
        l = [username, password, s]
        with open("nike.csv", "a", newline="") as f2:
            writer = csv.writer(f2)
            writer.writerow(l)
    elif password == confirmpass and s == "shopkeeper" and satch1==2:
        l = [username, password, s]
        with open("gucci.csv", "a", newline="") as f3:
            writer = csv.writer(f3)
            writer.writerow(l)
    elif password == confirmpass and s == "shopkeeper" and satch1==3:
        l = [username, password, s]
        with open("adidas.csv", "a", newline="") as f4:
            writer = csv.writer(f4)
            writer.writerow(l)
    elif password == confirmpass and s == "shopkeeper" and satch1==4:
        l = [username, password, s]
        with open("puma.csv", "a", newline="") as f5:
            writer = csv.writer(f5)
            writer.writerow(l)
    elif password == confirmpass and s == "arcade":
        l = [username, password, s]
        with open("arcade.csv", "a", newline="") as f6:
            writer = csv.writer(f6)
            writer.writerow(l)
    elif password == confirmpass and s == "parking":
        l = [username, password, s]
        with open("parking.csv", "a", newline="") as f7:
            writer = csv.writer(f7)
            writer.writerow(l)
    elif password == confirmpass and s == "event":
        l = [username, password, s]
        with open("event.csv", "a", newline="") as f8:
            writer = csv.writer(f8)
            writer.writerow(l)
    else:
        messagebox.showerror("Error", "Passwords do not match")

#-----------------------------------------------------
#Adding Subfunctions
#Parking


def parking():
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image11 = Image.open("mall.jpg")
    resized_image11 = image11.resize((1500, 350))  # Adjust the width and height as needed
    img11 = ImageTk.PhotoImage(resized_image11)

    
 
            
    

    
 


    # Display the image in the main window
    tk.Label(screen, image=img11, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)

    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)
    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)


   
    image = Image.open("park.jpg")
    

    resized_image8 = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=400, image=img, bg="black", fg="white", border=0, command=admin11).place(x=240, y=500)
    
    label = tk.Label(screen, text="PARKING MANAGEMENT", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)
    Button(frame, width=50, pady=12, text="ADD Record ", bg="#57a1f8", fg="white", border=0, command=editpark).place(x=0, y=27)
    Button(frame, width=50, pady=12, text="SEE Record", bg="#57a1f8", fg="white", border=0, command=seerecord).place(x=0, y=97)
   


    screen.mainloop()
def editpark():
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="PARKING MANAGMENT", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)
    Button(frame, width=39, pady=7, text="Enter RECORD", bg="#57a1f8", fg="white", border=0, command=enterpark).place(x=75, y=80)
    Button(frame, width=39, pady=7, text="EXIT RECORD", bg="#57a1f8", fg="white", border=0, command=exitpark).place(x=75, y=150)

def enterpark():
    global user, Model, no  # Declaring them as global variables

    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Enter your Name")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        Model.delete(0, 'end')

    def on_leave(e):
        name = Model.get()
        if name == "":
            Model.insert(0, "No. Plate")

    Model= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    Model.place(x=75, y=140)
    Model.insert(0, "No. Plate")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)
    Model.bind("<FocusIn>", on_enter)
    Model.bind("<FocusOut>", on_leave)

    def on_enter(e):
        no.delete(0, 'end')

    def on_leave(e):
        name = no.get()
        if name == "":
            no.insert(0, "Phone no.")

    no=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    no.place(x=75, y=200)
    no.insert(0, "Phone no.")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=225)
    no.bind("<FocusIn>", on_enter)
    no.bind("<FocusOut>", on_leave)
    Button(frame, width=39, pady=7, text="ADD RECORD", bg="#57a1f8", fg="white", border=0, command=addrecordpark).place(x=75, y=250)

    screenp.mainloop()

def addrecordpark():
    global Model,user,no,parkingtaken
    user1 = user.get()
    Modes = Model.get()
    no1= no.get()
    s2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    q = "INSERT INTO parkrecord VALUES('{}', '{}', {},  '{}' )".format(user1, Modes, no1, s2)
    display(q)
        
def exitpark():
    global model
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)

    def on_enter(e):
        model.delete(0, 'end')

    def on_leave(e):
        name = model.get()
        if name == "":
            model.insert(0, "username")

    model = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    model.place(x=75, y=80)
    model.insert(0, "Enter Model")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    model.bind("<FocusIn>", on_enter)
    model.bind("<FocusOut>", on_leave)
    Button(frame, width=39, pady=7, text="exit", bg="#57a1f8", fg="white", border=0, command=exitdone).place(x=75, y=220)


def exitdone():
    global model1, parkingavailable, parkingtaken
    model1 = model.get()
    parkingtaken=0

    with open("parkrecord.csv", "r", newline="") as f, open("parkrecord2.csv", "w", newline="") as f2:
        csvobj = csv.reader(f)
        writer = csv.writer(f2)
        for line in csvobj:
            if line[1] == model1:
                s2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Extend the line with exit timestamp
                L = line[:4] + [s2]
                writer.writerow(L)
                print("works")
                messagebox.showinfo("Success", "Inventory updated successfully!")
            else:
                writer.writerow(line)  

    with open("parkrecord.csv", "w", newline="") as f4, open("parkrecord2.csv", "r", newline="") as f5:
        obj1 = csv.writer(f4)
        obj2 = csv.reader(f5)
        for i in obj2:
            obj1.writerow(i)

    with open("parkuserdisplaycount.csv", "r", newline="") as f1, open("test.csv", "w", newline="") as f3:
        obj1 = csv.reader(f1)
        obj2 = csv.writer(f3)

        flag = 0
        for i in obj1:
            if i[1] != model1:
                obj2.writerow(i)
            else:
                flag = 1

    with open("parkuserdisplaycount.csv", "w", newline="") as f4, open("test.csv", "r", newline="") as f5:
        obj1 = csv.writer(f4)
        obj2 = csv.reader(f5)
        for i in obj2:
            obj1.writerow(i)
            parkingtaken+=1

    print(c)

        


def seerecord():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screen, image=img, bg="blue").place(x=50, y=50)

    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)
    
    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("Name", "Model", "Phone_No", "Clock_In", "Clock_Out"), show="headings")
    
    # Define the column headings
    tree.heading("Name", text="Name")
    tree.heading("Model", text="Model")
    tree.heading("Phone_No", text="Phone No.")
    tree.heading("Clock_In", text="Clock In")   
    tree.heading("Clock_Out", text="Clock Out")
    
    # Define column widths
    tree.column("Name", width=150)
    tree.column("Model", width=150)
    tree.column("Phone_No", width=150)
    tree.column("Clock_In", width=150)
    tree.column("Clock_Out", width=150)


    # Insert sample data into the table (you can replace this with your actual data)
 
    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    

    screen.mainloop()



   
    

#---------------------------------------------------------------------# 
#shopkeeper    
    
def signin111():
    global user, passi,satch,s
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
 
            
    image8 = Image.open("shopkeeper.jpg")
    resized_image8 = image8.resize((400, 400))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=400, image=img8, bg="black", fg="white", border=0, command=admin11).place(x=240, y=600)

    
 


    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)

    heading = tk.Label(frame, text="Sign IN", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Username")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        passi.delete(0, 'end')

    def on_leave(e):
        name = passi.get()
        if name == "":
            passi.insert(0, "Password")

    passi = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passi.place(x=75, y=140)
    passi.insert(0, "Password")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)
    passi.bind("<FocusIn>", on_enter)
    passi.bind("<FocusOut>", on_leave)
#creating check boxes for diff shops :))
    checkbox_var = tk.IntVar()
    checkbox_var1 = tk.IntVar()
    checkbox_var2 = tk.IntVar()
    checkbox_var3 = tk.IntVar()

    # Checkboxes for brand selection
    tk.Checkbutton(frame, text="Nike", variable=checkbox_var).place(x=75, y=180)
    tk.Checkbutton(frame, text="GUCCI", variable=checkbox_var1).place(x=180, y=180)
    tk.Checkbutton(frame, text="adidas", variable=checkbox_var2).place(x=75, y=210)
    tk.Checkbutton(frame, text="Puma", variable=checkbox_var3).place(x=180, y=210)

    # Function to check which brand is selected
    def check_selection1():
        global satch
        if checkbox_var.get() == 1:
                satch = 1
                print("Start")
        elif checkbox_var1.get() == 1:
            satch = 2
        elif checkbox_var2.get() == 1:
            satch = 3
        elif checkbox_var3.get() == 1:
            satch = 4
        else:
            Satch1 = None
            print(f"Selected brand: {satch1 if satch1 else 'No selection'}")

    # Button to check the selection
    tk.Button(frame, text="Check Selection", command=check_selection1).place(x=250, y=180)

    Button(frame, width=39, pady=7, text="Sign IN", bg="#57a1f8", fg="white", border=0, command=signinclassify).place(x=75, y=250)
    label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    label.place(x=75, y=290)
    sign_in = Button(frame, width=6, text="Sign UP", border=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft Yahei UI Light", 11), command=signup1)
    sign_in.place(x=250, y=290)

    



    screen.mainloop()
def shopcheck():
    global sh,sh1,satch,k
    if satch==1:
        print("yes")
        nike()
        sh="nike"
        sh1="nikeinventory.csv"
        k="nike.jpg"

    elif satch==2:
        nike()
        sh="GUCCI"
        sh1="GUCCIinventory.csv"
        k="GUCCI.jpg"
    elif satch==3:
        nike()
        sh="adidas"
        sh1="adidasinventory.csv"
        k="adidas.jpg"

    elif satch==4:
        nike()
        sh="puma"
        sh1="pumainventory.csv"
        k="puma.jpg"

def nike():
    global sh,sh1,satch,k
    print(k)
    print("working")
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("1920x1080")
    screen.configure(bg="#fff")

    
    image11 = Image.open("mall.jpg")
    resized_image11 = image11.resize((1500, 350))  # Adjust the width and height as needed
    img11 = ImageTk.PhotoImage(resized_image11)

    
 
            
    

    
 


    # Display the image in the main window
    tk.Label(screen, image=img11, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)

    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)
    frame = tk.Frame(screen, width=350, height=350, bg="white")
    frame.place(x=880, y=600)


   
    if satch==1:
        image = Image.open("nike.jpg")
        j="NIKE MANAGEMENT"
    elif satch==2:
        image = Image.open("GUCCI.jpg")
        j="GUCCI MANAGEMENT"
    elif satch==3:
        image = Image.open("adidas.jpg")
        j="ADIDAS MANAGEMENT"
    elif satch==4:
        image = Image.open("puma.jpg")
        j="PUMA MANAGEMENT"
    

    resized_image8 = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=400, image=img, bg="black", fg="white", border=0, command=admin11).place(x=240, y=500)
    
    label = tk.Label(screen, text=j, fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)
    Button(frame, width=50, pady=12, text="ADD Record ", bg="#57a1f8", fg="white", border=0, command=addrecordnike).place(x=0, y=27)
    Button(frame, width=50, pady=12, text="SEE Record", bg="#57a1f8", fg="white", border=0, command=seeshop).place(x=0, y=97)
    Button(frame, width=50, pady=12, text="DELETE RECORD", bg="#57a1f8", fg="white", border=0, command=deleterecord).place(x=0, y=177)


    screen.mainloop()


def addrecordnike():
    global product, unit, price, quantity, img

    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")

    if satch == 1:
        image = Image.open("nike.jpg")
        sh1 = "nikeinventory.csv"
    elif satch == 2:
        image = Image.open("GUCCI.jpg")
        sh1 = "GUCCIinventory.csv"
    elif satch == 3:
        image = Image.open("adidas.jpg")
        sh1 = "adidasinventory.csv"
    elif satch == 4:
        image = Image.open("puma.jpg")
        sh1 = "pumainventory.csv"

    resized_image = image.resize((400, 400))
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = Frame(screenp, width=470, height=400, bg="white")
    frame.place(x=460, y=70)
    tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold")).place(x=60, y=5)

    def create_entry(placeholder, y_pos):
        entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        entry.place(x=75, y=y_pos)
        entry.insert(0, placeholder)
        Frame(frame, width=295, height=2, bg="black").place(x=75, y=y_pos + 27)

        def on_enter(e):
            if entry.get() == placeholder:
                entry.delete(0, 'end')

        def on_leave(e):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry.bind("<FocusIn>", on_enter)
        entry.bind("<FocusOut>", on_leave)
        return entry

    product = create_entry("Product Name", 80)
    unit = create_entry("Unit", 140)
    price = create_entry("Price per Unit", 200)
    quantity = create_entry("Quantity in terms of Unit", 250)

    def update_inventory():
        p = product.get()
        u = unit.get()
        p1 = price.get()
        q = quantity.get()

        # Validate fields
        if p in ["Product Name", ""] or u in ["unit", ""] or p1 in ["price", ""] or q in ["quantity", ""]:
            messagebox.showwarning("Input Error", "Please enter valid values.")
            return

        # Ensure file exists
        if not os.path.exists(sh1):
            with open(sh1, "w", newline="") as f:
                csv.writer(f).writerow(["Product", "Unit", "Price", "Quantity"])

        # Write to CSV
        try:
            with open(sh1, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([p, u, p1, q])
                print("Data written to file:", [p, u, p1, q])  # Debug print
                messagebox.showinfo("Success", "Inventory updated successfully!")
                screenp.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update inventory: {e}")

    Button(frame, width=39, pady=7, text="ADD RECORD", bg="#57a1f8", fg="white", border=0, command=update_inventory).place(x=75, y=340)
   
    
def seeshop():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")

    global img  # Keep the image in memory

    # Determine the CSV file and image based on `satch`
    try:
        if satch == 1:
            image = Image.open("nike.jpg")
            sh1 = "nikeinventory.csv"
        elif satch == 2:
            image = Image.open("GUCCI.jpg")
            sh1 = "GUCCIinventory.csv"
        elif satch == 3:
            image = Image.open("adidas.jpg")
            sh1 = "adidasinventory.csv"
        elif satch == 4:
            image = Image.open("puma.jpg")
            sh1 = "pumainventory.csv"
        else:
            raise ValueError("Invalid `satch` value!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to set up shop: {e}")
        return

    # Display the shop image
    try:
        resized_image = image.resize((400, 400))
        img = ImageTk.PhotoImage(resized_image)
        tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")
        return

    # Create a frame for the table
    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)

    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("product", "unit", "price", "quantity"), show="headings")

    # Define the column headings
    tree.heading("product", text="Product")
    tree.heading("unit", text="Unit")
    tree.heading("price", text="Price")
    tree.heading("quantity", text="Quantity")

    # Define column widths
    tree.column("product", width=150)
    tree.column("unit", width=150)
    tree.column("price", width=150)
    tree.column("quantity", width=150)

    # Insert data from the CSV file
    try:
        print("Loading data from file:", sh1)
        with open(sh1, "r") as f:
            csvobj = csv.reader(f)
            for record in csvobj:
                print("Record:", record)  # Debug: print each row
                if len(record) == 4:  # Ensure the row has the correct number of columns
                    tree.insert("", "end", values=record)
                else:
                    print(f"Invalid record skipped: {record}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {sh1}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load inventory data: {e}")
        return

    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()



def deleterecord():
    global delete1, satch, sh1
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")

    # Open image based on satch value
    if satch == 1:
        image = Image.open("nike.jpg")
        sh1 = "nikeinventory.csv"
    elif satch == 2:
        image = Image.open("GUCCI.jpg")
        sh1 = "GUCCIinventory.csv"
    elif satch == 3:
        image = Image.open("adidas.jpg")
        sh1 = "adidasinventory.csv"
    elif satch == 4:
        image = Image.open("puma.jpg")
        sh1 = "pumainventory.csv"
    
    # Resize image and display
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    # Create frame and heading
    frame = tk.Frame(screenp, width=470, height=400, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)

    # Define focus-in and focus-out behavior for delete entry
    def on_enter(e):
        delete1.delete(0, 'end')

    def on_leave(e):
        name = delete1.get()
        if name == "":
            delete1.insert(0, "Product Name")

    # Create delete entry
    delete1 = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    delete1.place(x=75, y=80)
    delete1.insert(0, "Product Name")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    delete1.bind("<FocusIn>", on_enter)
    delete1.bind("<FocusOut>", on_leave)

    # Define delete function
    def delete():
        global delete1
        d = delete1.get()

        # Open CSV files
        with open(sh1, "r", newline="") as f1, open("test.csv", "w", newline="") as f2:
            obj1 = csv.reader(f1)
            obj2 = csv.writer(f2)

            flag = 0
            for i in obj1:
                if i[0] != d:
                    obj2.writerow(i)
                elif i[0] == d:
                    flag = 1

            if flag == 0:
               messagebox.showerror("Error", f"Record not found!")
            elif flag == 1:
                messagebox.showinfo("Success", "Record deleted successfully!")

            # Rewrite the original CSV with updated data
            with open(sh1, "w", newline="") as f1, open("test.csv", "r", newline="") as f2:
                obj1 = csv.writer(f1)
                obj2 = csv.reader(f2)
                for i in obj2:
                    obj1.writerow(i)

    # Button to delete record
    Button(frame, width=39, pady=7, text="DELETE RECORD", bg="#57a1f8", fg="white", border=0, command=delete).place(x=75, y=340)

    screenp.mainloop()

        
#def shopdisplay():
##### ##   #
#arcade

def arcade():
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("arcade.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="PARKING MANAGMENT", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)
    Button(frame, width=39, pady=7, text="Edit Record", bg="#57a1f8", fg="white", border=0, command=editarcade).place(x=75, y=80)
    Button(frame, width=39, pady=7, text="SEE Record", bg="#57a1f8", fg="white", border=0, command=seerecordarcade).place(x=75, y=150)
def editarcade():
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("arcade.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="PARKING MANAGMENT", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)
    Button(frame, width=39, pady=7, text="Enter RECORD", bg="#57a1f8", fg="white", border=0, command=enterarcade).place(x=75, y=80)
    Button(frame, width=39, pady=7, text="EXIT RECORD", bg="#57a1f8", fg="white", border=0, command=exitarcade).place(x=75, y=150)

def enterarcade():
    global user, Model, no,age,ticket  # Declaring them as global variables

    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("arcade.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Enter your Name")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        age.delete(0, 'end')

    def on_leave(e):
        name = age.get()
        if name == "":
            age.insert(0, "Enter age")

    age= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    age.place(x=75, y=140)
    age.insert(0, "Enter age")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=167)
    age.bind("<FocusIn>", on_enter)
    age.bind("<FocusOut>", on_leave)

    def on_enter(e):
        no.delete(0, 'end')

    def on_leave(e):
        name = no.get()
        if name == "":
            no.insert(0, "Phone no.")

    no=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    no.place(x=75, y=200)
    no.insert(0, "Phone no.")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=225)
    no.bind("<FocusIn>", on_enter)
    no.bind("<FocusOut>", on_leave)


    def on_enter(e):
        ticket.delete(0, 'end')

    def on_leave(e):
        name = ticket.get()
        if name == "":
            ticket.insert(0, "Tickets")

    ticket=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    ticket.place(x=75, y=250)
    ticket.insert(0, "Tickets")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=275)
    ticket.bind("<FocusIn>", on_enter)
    ticket.bind("<FocusOut>", on_leave)
    Button(frame, width=39, pady=7, text="ADD RECORD", bg="#57a1f8", fg="white", border=0, command=addrecordarcade).place(x=75, y=300)

    screenp.mainloop()
def addrecordarcade():
    global age,user,no,parkingtaken,ticket
    user1 = user.get()
    age1 = age.get()
    no1= no.get()
    t=ticket.get()


    l = [user1, age1, no1,t]
    with open("arcaderecord.csv", "a", newline="") as f:
        print("arcade")
        writer = csv.writer(f)
        writer.writerow(l)
def exitarcade():
    global user
    screenp = Toplevel(root)
    screenp.title("App")
    screenp.configure(bg="#fff")
    screenp.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screenp, image=img, bg="blue").place(x=50, y=50)

    frame = tk.Frame(screenp, width=470, height=350, bg="white")
    frame.place(x=460, y=70)
    heading = tk.Label(frame, text="ADD RECORD", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=60, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            model.insert(0, "username")

    def deletearcade():
        global delete1
        d = delete1.get()

        # Open CSV files
        with open("arcaderecord.csv", "r", newline="") as f1, open("test1.csv", "w", newline="") as f2:
            obj1 = csv.reader(f1)
            obj2 = csv.writer(f2)

            flag = 0
            for i in obj1:
                if i[0] != d:
                    obj2.writerow(i)
                elif i[0] == d:
                    flag = 1

            if flag == 0:
               messagebox.showerror("Error", f"Record not found!")
            elif flag == 1:
                messagebox.showinfo("Success", "Record deleted successfully!")

            # Rewrite the original CSV with updated data
            with open("arcaderecor.csv", "w", newline="") as f1, open("test1.csv", "r", newline="") as f2:
                obj1 = csv.writer(f1)
                obj2 = csv.reader(f2)
                for i in obj2:
                    obj1.writerow(i)

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=75, y=80)
    user.insert(0, "Enter Model")
    Frame(frame, width=295, height=2, bg="black").place(x=75, y=107)
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Button(frame, width=39, pady=7, text="exit", bg="#57a1f8", fg="white", border=0, command=deletearcade).place(x=75, y=220)

def seerecordarcade():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")
    image = Image.open("arcade.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screen, image=img, bg="blue").place(x=50, y=50)

    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)
    
    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("Name", "AGE", "Phone_No", "Tickets"), show="headings")
    
    # Define the column headings
    tree.heading("Name", text="Name")
    tree.heading("AGE", text="Model")
    tree.heading("Phone_No", text="Phone No.")
    tree.heading("Tickets", text="Tickets")
    
    # Define column widths
    tree.column("Name", width=150)
    tree.column("AGE", width=150)
    tree.column("Phone_No", width=150)
    tree.column("Tickets", width=150)
  
    
    # Insert sample data into the table (you can replace this with your actual data)
    with open("arcaderecord.csv", "r") as f:
        csvobj = csv.reader(f)
        for record in csvobj:
            tree.insert("", "end", values=record)
    
    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()
##########################################
#user starting#

def userdisplay():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
    image8 = Image.open("admin.jpg")
    resized_image8 = image8.resize((200, 200))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img8, bg="black", fg="white", border=0, command=admin1).place(x=50, y=600)
 

    image1 = Image.open("user.jpg")
    resized_image1 = image1.resize((200, 200))  # Adjust the width and height as needed
    img1 = ImageTk.PhotoImage(resized_image1)# int this add a white frame then black background %%%%%%%%
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img1 , bg="white", fg="white", border=0, command=user1).place(x=420, y=600)

    image2 = Image.open("shopkeeper.jpg")
    resized_image2 = image2.resize((200, 200))  # Adjust the width and height as needed
    img2 = ImageTk.PhotoImage(resized_image2)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img2 , bg="black", fg="white", border=0, command=shopdisplayuser).place(x=800, y=600)

    image3 = Image.open("arcade.jpg")
    resized_image3 = image3.resize((200, 200))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image3)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img3 , bg="black", fg="white", border=0, command=arcade1).place(x=1120, y=600)


    image4 = Image.open("parking.jpg")
    resized_image4 = image4.resize((200, 200))  # Adjust the width and height as needed
    img4 = ImageTk.PhotoImage(resized_image4)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img4 , bg="black", fg="white", border=0, command=parkdisplayuser).place(x=1420, y=600)

    image5 = Image.open("event.jpg")
    resized_image5 = image5.resize((200, 200))  # Adjust the width and height as needed
    img5 = ImageTk.PhotoImage(resized_image5)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img5 , bg="black", fg="white", border=0, command=event1).place(x=1700, y=600)

    label2 = tk.Label(screen, text="ADMIN", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=80, y=850)

    label3 = tk.Label(screen, text="USER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label3.place(x=480, y=850)


    label4 = tk.Label(screen, text="SHOPKEEPER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label4.place(x=810, y=850)


    label5 = tk.Label(screen, text="ARCADE", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label5.place(x=1160, y=850)

    label6 = tk.Label(screen, text="PARKING", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label6.place(x=1450, y=850)


    label7 = tk.Label(screen, text="EVENTS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label7.place(x=1740, y=850)



    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)



    screen.mainloop()
    

    
    
def parkdisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")
    image = Image.open("park.jpg")
    resized_image = image.resize((400, 400))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)
    tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    frame = tk.Frame(screen, width=1000, height=1200, bg="white")
    frame.place(x=580, y=0)

    label1 = tk.Label(frame, text="Total Slots  :  ", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label1.place(x=50, y=80)
    label11 = tk.Label(frame, text=parkingtotal, fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label11.place(x=220, y=80)
    label2 = tk.Label(frame, text="Available Slots  :  ", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=50, y=180)
    label22 = tk.Label(frame, text=parkingtotal-parkingtaken, fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label22.place(x=270, y=180)
    
    

    screen.mainloop()

def shopdisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")
    image = Image.open("mall.jpg")
    resized_image = image.resize((1500, 350))  # Adjust the width and height as needed
    img = ImageTk.PhotoImage(resized_image)

    
    image8 = Image.open("nike.jpg")
    resized_image8 = image8.resize((200, 200))  # Adjust the width and height as needed
    img8 = ImageTk.PhotoImage(resized_image8)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img8, bg="black", fg="white", border=0, command=nikedisplayuser).place(x=50, y=600)
 

    image1 = Image.open("GUCCI.jpg")
    resized_image1 = image1.resize((200, 200))  # Adjust the width and height as needed
    img1 = ImageTk.PhotoImage(resized_image1)# int this add a white frame then black background %%%%%%%%
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img1 , bg="white", fg="white", border=0, command=GUCCIdisplayuser).place(x=420, y=600)

    image2 = Image.open("adidas.jpg")
    resized_image2 = image2.resize((200, 200))  # Adjust the width and height as needed
    img2 = ImageTk.PhotoImage(resized_image2)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img2 , bg="black", fg="white", border=0, command=adidasdisplayuser).place(x=800, y=600)

    image3 = Image.open("puma.jpg")
    resized_image3 = image3.resize((200, 200))  # Adjust the width and height as needed
    img3 = ImageTk.PhotoImage(resized_image3)
    screen.configure(bg="#fff")
    Button(screen, width=200, image=img3 , bg="black", fg="white", border=0, command=pumadisplayuser).place(x=1120, y=600)


    

    label2 = tk.Label(screen, text="ADMIN", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label2.place(x=80, y=850)

    label3 = tk.Label(screen, text="USER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label3.place(x=480, y=850)


    label4 = tk.Label(screen, text="SHOPKEEPER", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label4.place(x=810, y=850)


    label5 = tk.Label(screen, text="ARCADE", fg="black", bg="white", font=("Microsoft Yahei UI Light", 20, "bold"))
    label5.place(x=1160, y=850)



    # Display the image in the main window
    tk.Label(screen, image=img, bg="blue").place(x=250, y=5)
 



    # Create a frame for the buttons
    frame1 = tk.Frame(screen, width=2000, height=60, bg="#57a1f8", bd=5, relief="solid")
    frame1.place(x=4, y=395)

    frame2 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame2.place(x=220, y=0)
    
    frame3 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame3.place(x=580, y=0)

    frame4 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame4.place(x=900, y=0)


    frame5 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame5.place(x=1300, y=0)
    
    frame6 = tk.Frame(frame1, width=5, height=50, bg="black")
    frame6.place(x=1600, y=0)



    label = tk.Label(screen, text="Sign IN AS", fg="black", bg="white", font=("Microsoft Yahei UI Light", 40, "bold"))
    label.place(x=770, y=470)

    # Define font for buttons
    button_font = font.Font(family="Microsoft Yahei UI Light", size=18, weight="bold")

    # Create buttons in the frame
    Button(frame1, width=6, text="About", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=50, y=0)
    Button(frame1, width=6, text="Sign Up", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signup2).place(x=350, y=0)
    Button(frame1, width=6, text="Sign in", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font,command=signin2).place(x=700, y=0)
    Button(frame1, width=6, text="Offer", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1050, y=0)
    Button(frame1, width=6, text="Brands", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1400, y=0)
    Button(frame1, width=6, text="Contact", border=0, bg="#57a1f8", cursor="hand2", fg="white", font=button_font).place(x=1700, y=0)

    
        

    screen.mainloop()
    
def nikedisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")

    global img  # Keep the image in memory

    # Determine the CSV file and image based on `satch`
    
    image = Image.open("nike.jpg")
    sh1 = "nikeinventory.csv"
    

    # Display the shop image
    try:
        resized_image = image.resize((400, 400))
        img = ImageTk.PhotoImage(resized_image)
        tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")
        return

    # Create a frame for the table
    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)

    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("product", "unit", "price", "quantity"), show="headings")

    # Define the column headings
    tree.heading("product", text="Product")
    tree.heading("unit", text="Unit")
    tree.heading("price", text="Price")
    tree.heading("quantity", text="Quantity")

    # Define column widths
    tree.column("product", width=150)
    tree.column("unit", width=150)
    tree.column("price", width=150)
    tree.column("quantity", width=150)

    # Insert data from the CSV file
    try:
        print("Loading data from file:", sh1)
        with open(sh1, "r") as f:
            csvobj = csv.reader(f)
            for record in csvobj:
                print("Record:", record)  # Debug: print each row
                if len(record) == 4:  # Ensure the row has the correct number of columns
                    tree.insert("", "end", values=record)
                else:
                    print(f"Invalid record skipped: {record}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {sh1}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load inventory data: {e}")
        return

    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()

def GUCCIdisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")

    global img  # Keep the image in memory

    # Determine the CSV file and image based on `satch`
    
    image = Image.open("GUCCI.jpg")
    sh1 = "GUCCIinventory.csv"
    

    # Display the shop image
    try:
        resized_image = image.resize((400, 400))
        img = ImageTk.PhotoImage(resized_image)
        tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")
        return

    # Create a frame for the table
    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)

    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("product", "unit", "price", "quantity"), show="headings")

    # Define the column headings
    tree.heading("product", text="Product")
    tree.heading("unit", text="Unit")
    tree.heading("price", text="Price")
    tree.heading("quantity", text="Quantity")

    # Define column widths
    tree.column("product", width=150)
    tree.column("unit", width=150)
    tree.column("price", width=150)
    tree.column("quantity", width=150)

    # Insert data from the CSV file
    try:
        print("Loading data from file:", sh1)
        with open(sh1, "r") as f:
            csvobj = csv.reader(f)
            for record in csvobj:
                print("Record:", record)  # Debug: print each row
                if len(record) == 4:  # Ensure the row has the correct number of columns
                    tree.insert("", "end", values=record)
                else:
                    print(f"Invalid record skipped: {record}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {sh1}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load inventory data: {e}")
        return

    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()    
def adidasdisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")

    global img  # Keep the image in memory

    # Determine the CSV file and image based on `satch`
    
    image = Image.open("adidas.jpg")
    sh1 = "adidasinventory.csv"
    

    # Display the shop image
    try:
        resized_image = image.resize((400, 400))
        img = ImageTk.PhotoImage(resized_image)
        tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")
        return

    # Create a frame for the table
    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)

    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("product", "unit", "price", "quantity"), show="headings")

    # Define the column headings
    tree.heading("product", text="Product")
    tree.heading("unit", text="Unit")
    tree.heading("price", text="Price")
    tree.heading("quantity", text="Quantity")

    # Define column widths
    tree.column("product", width=150)
    tree.column("unit", width=150)
    tree.column("price", width=150)
    tree.column("quantity", width=150)

    # Insert data from the CSV file
    try:
        print("Loading data from file:", sh1)
        with open(sh1, "r") as f:
            csvobj = csv.reader(f)
            for record in csvobj:
                print("Record:", record)  # Debug: print each row
                if len(record) == 4:  # Ensure the row has the correct number of columns
                    tree.insert("", "end", values=record)
                else:
                    print(f"Invalid record skipped: {record}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {sh1}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load inventory data: {e}")
        return

    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()

def pumadisplayuser():
    screen = Toplevel(root)
    screen.title("App")
    screen.configure(bg="#fff")
    screen.geometry("1920x1080")

    global img  # Keep the image in memory

    # Determine the CSV file and image based on `satch`
    
    image = Image.open("puma.jpg")
    sh1 = "pumainventory.csv"
    

    # Display the shop image
    try:
        resized_image = image.resize((400, 400))
        img = ImageTk.PhotoImage(resized_image)
        tk.Label(screen, image=img, bg="blue").place(x=50, y=50)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")
        return

    # Create a frame for the table
    table_frame = Frame(screen, width=600, height=350, bg="white")
    table_frame.place(x=460, y=70)

    # Create the Treeview widget
    tree = ttk.Treeview(table_frame, columns=("product", "unit", "price", "quantity"), show="headings")

    # Define the column headings
    tree.heading("product", text="Product")
    tree.heading("unit", text="Unit")
    tree.heading("price", text="Price")
    tree.heading("quantity", text="Quantity")

    # Define column widths
    tree.column("product", width=150)
    tree.column("unit", width=150)
    tree.column("price", width=150)
    tree.column("quantity", width=150)

    # Insert data from the CSV file
    try:
        print("Loading data from file:", sh1)
        with open(sh1, "r") as f:
            csvobj = csv.reader(f)
            for record in csvobj:
                print("Record:", record)  # Debug: print each row
                if len(record) == 4:  # Ensure the row has the correct number of columns
                    tree.insert("", "end", values=record)
                else:
                    print(f"Invalid record skipped: {record}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {sh1}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load inventory data: {e}")
        return

    # Pack the Treeview widget into the frame
    tree.pack(fill="both", expand=True)

    screen.mainloop()    
#--------------------------------------------------------------------#

image = Image.open("finalmall1.jpg")
resized_image = image.resize((1920,1080 ))  # Adjust the width and height as needed
img = ImageTk.PhotoImage(resized_image)
tk.Label(root, image=img, bg="blue").place(x=0, y=0)

image4 = Image.open("mallabout.jpg")
resized_image4 = image4.resize((250, 80))  # Adjust the width and height as needed
img3 = ImageTk.PhotoImage(resized_image4)
root.configure(bg="#fff")
Button(root, width=250, image=img3 ,  fg="white", border=0, ).place(x=361, y=890)

image5 = Image.open("mallbrands.jpg")
resized_image5 = image5.resize((220, 80))  # Adjust the width and height as needed
img5 = ImageTk.PhotoImage(resized_image5)
root.configure(bg="#fff")
Button(root, width=220, image=img5 ,  fg="white", border=0, ).place(x=604.4, y=890)


image6 = Image.open("mallcontact.jpg")
resized_image6 = image6.resize((220, 100))  # Adjust the width and height as needed
img6 = ImageTk.PhotoImage(resized_image6)
root.configure(bg="#fff")
Button(root, width=220, image=img6 ,  fg="white", border=0, ).place(x=850, y=875)



image8 = Image.open("mallsignup.jpg")
resized_image8 = image8.resize((220, 80))  # Adjust the width and height as needed
img8 = ImageTk.PhotoImage(resized_image8)
root.configure(bg="#fff")
Button(root, width=220, image=img8 ,  fg="white", border=0,command=signup2 ).place(x=1100, y=890)

image9 = Image.open("mallsign.jpg")
resized_image9 = image9.resize((220, 80))  # Adjust the width and height as needed
img9 = ImageTk.PhotoImage(resized_image9)
root.configure(bg="#fff")
Button(root, width=220, image=img9 ,  fg="white",command=signin2, border=0, ).place(x=1342, y=890)




 
# Start the Tkinter event loop
root.mainloop()

