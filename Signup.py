from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
#import mysql.connector
from Hotel import HotelManagementSystem
from login import Login_Window

def main():
    win = Tk()
    app = Signup_Window(win)
    win. mainloop()


class Signup_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")

        # self.bg = Image.open(
        #     "C:/Users/gurun/Desktop/CollegeProject/image/topimg.jpg")
        # lbl_bg = Label(self.root, image=self.bg)

        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=170, width=600, height=450)

        # img1= Image.open("C:/Users/gurun/Desktop/.png)
        #img1= img1.resize((90,90),Image.ANTIALIAS)
        #self.photoimg1= ImageTk.PhotoImage(img1)

        #lblimg1= Label(image=self.photoimg1, bg="black",borderwidth=0)
        #lblimg1.place(x=730,y=170, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=150, y=55)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=150, y=100)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=150, y=130, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=150, y=175)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=150, y=205, width=270)

        password = lbl = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=150, y=250)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=150, y=280, width=270)

        # Login Buttton
        loginbutton = Button(frame, command=self.login, text="Sign-Up", font=("times new roman", 15, "bold"),
                             bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white")
        loginbutton.place(x=150, y=330, width=120, height=35)

        # Register Buttton
        loginbutton = Button(frame, text="Registered User", font=("times new roman", 15, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        loginbutton.place(x=150, y=380, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields Required")
        elif self.txtuser.get() == "srijan" and self.txtpass.get() == "grg":
            messagebox.showinfo("Success", "Welcom To Hotel Management System")
        else:
            messagebox.showerror("Inavlid", "Inavalid Username or Password")
    
    def login_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_Window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Signup_Window(root)
    root.mainloop()
