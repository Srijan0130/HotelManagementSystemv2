from tkinter import*
#from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
#import mysql.connector
from tkinter import messagebox


class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # title
        lbl_title = Label(self.root, text="DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        # img2= Image.open("C:/Users/gurun/Desktop/.png)
        # img2= img2.resize((100,40),Image.ANTIALIAS)
        # self.photoimg2= ImageTk.PhotoImage(img2)

        # lblimg= Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=0, width=230, height=140)

        # labelFrame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",  font=(
            "times new roman", 18, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=520, height=350)

        # Floor
        lbl_floor = Label(labelframeleft, text="Floor:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W, padx=20)

        self.var_floor = StringVar()
        enty_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, font=(
            "times new roman", 13, "bold"), width=20)
        enty_floor.grid(row=0, column=1, sticky=W)

        # Room no
        lbl_RoomNo = Label(labelframeleft, text="Room No:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)

        self.var_RoomNo = StringVar()
        enty_RoomNo = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=20)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)

        self.var_RoomType = StringVar()
        enty_RoomType = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=20)
        enty_RoomType.grid(row=2, column=1, sticky=W)

        # -----------Buttons--------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_details, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", command=self.delete, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET", command=self.reset, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame search system

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_Table = ttk. Treeview(Table_Frame, column=(
            "floor", "roomno", "roomType"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("floor", text="Floor")
        self.room_Table.heading("roomno", text="Room No")
        self.room_Table.heading("roomType", text="Room Type")

        self.room_Table["show"] = "headings"

        self.room_Table.column("floor", width=120)
        self.room_Table.column("roomno", width=120)
        self.room_Table.column("roomType", width=120)

        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_details()

        # add data

    def add_details(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="local", username="root", password="", database="")
                my_cursor = conn.cursor()
                my_cursor.exexute("insert info details value(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_RoomNo.get(),
                    self.var_RoomType.get()


                ))
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showwinfo("New Room Added Successfully")
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    # fetch data
    def fetch_details(self):
        conn = mysql.connector.connect(
            host="local", username="root", password="", database="")
        my_cursor = conn.cursor()
        my_cursor.execute("select*from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(
                *self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self, events=""):
        cursor_row = self.room_Table.Focus()
        content = self.room_Table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])

     # Update Function

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror(
                "Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="local", username="root", password="", database="")
            my_cursor = conn.cursor()
            my_cursor.execute("update the details set Floor=%s,RoomType=%s where RoomNo=%s", (

                self.var_floor.get(),
                self.var_RoomNo.get(),
                self.var_RoomType.get()

            ))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo(
                "Update", "Room details has been updated success", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno(
            "Hotel Management System", "do you want to delete this room details", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="local", username="root", password="", database="")
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo=%s"
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_details()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
