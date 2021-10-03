from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
#import mysql.connector
from Hotel import HotelManagementSystem
from Signup import Signup_Window
import psycopg2


def main():
    win = Tk()
    app = Login_Window(win)
    win. mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")

        # self.bg = Image.open(
        #     "C:/Users/gurun/Desktop/CollegeProject/image/topimg.jpg")
        # lbl_bg = Label(self.root, image=self.bg)

        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=170, width=600, height=430)

        # img1= Image.open("C:/Users/gurun/Desktop/.png)
        #img1= img1.resize((90,90),Image.ANTIALIAS)
        #self.photoimg1= ImageTk.PhotoImage(img1)

        #lblimg1= Label(image=self.photoimg1, bg="black",borderwidth=0)
        #lblimg1.place(x=730,y=170, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=150, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=150, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=150, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=150, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=150, y=250, width=270)

        # Login Buttton
        loginbutton = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                             bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white")
        loginbutton.place(x=150, y=300, width=120, height=35)

        # Register Buttton
        loginbutton = Button(frame, text="New user register", command=self.signup_details, font=("times new roman", 15, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        loginbutton.place(x=150, y=350, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields Required")
        elif len(self.txtuser.get()) > 1 and len(self.txtpass.get()) > 1:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash

            cursor = conn.cursor()
            cursor.execute("select*from REGISTER ")
            postgreSQL_select_Query = "select * from REGISTER where username = %s"
            cursor.execute(postgreSQL_select_Query, (self.txtuser.get(),))
            # cursor.execute(
            #     "select*from REGISTER where username = %s", self.txtuser.get())
            rows = cursor.fetchall()
            new_username = rows[0][0]
            new_password = rows[0][1]
            print(rows)
            print(new_username, new_password)
            if(new_username == self.txtuser.get() and new_password == self.txtpass.get()):
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)

        else:
            messagebox.showerror("Inavlid", "Inavalid Username or Password")

    def signup_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Signup_Window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
