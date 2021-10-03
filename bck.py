from tkinter import*
from tkinter import ttk
#from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
#import mysql.connector
from Hotel import HotelManagementSystem


def main():
    win = Tk()
    app = Login_Window(win)
    win. mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotImage(file="C:/Users/gurun/Desktop/.png")
        lbl_bg = Label(self.root, image=self.bg)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=90, height=430)

        # img1= Image.open("C:/Users/gurun/Desktop/.png)
        #img1= img1.resize((90,90),Image.ANTIALIAS)
        #self.photoimg1= ImageTk.PhotoImage(img1)

        #lblimg1= Label(image=self.photoimg1, bg="black",borderwidth=0)
        #lblimg1.place(x=730,y=170, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.pace(x=95, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # Login Buttton
        loginbutton = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                             bd=3, relief=RIDGE, fg="white", bg="red", activforeground="white", activebackground="red")
        loginbutton.place(x=110, y=300, width=120, height=35)

        # Register Buttton
        loginbutton = Button(frame, text="New user register", font=("times new roman", 15, "bold"),
                             borderwidth=0, fg="white", bg="black", activforeground="white", activebackground="red")
        loginbutton.place(x=15, y=350, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields Required")
        elif self.txtuser.get() == "srijan" and self.txtpass.get() == "grg":
            messagebox.showinfo("Success", "Welcom To Hotel Management System")
        else:
            messagebox.showerror("Inavlid", "Inavalid Username or Password")

    if __name__ == "__main__":
        root = Tk()
        app = Login_Window(root)
        root.mainloop()
