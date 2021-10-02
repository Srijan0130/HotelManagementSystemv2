from tkinter import*
#from PIL import Image,ImageTk
from tkinter import ttk
import random
#import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofday = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # title
        lbl_title = Label(self.root, text="ROOMOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        # img2= Image.open("C:/Users/gurun/Desktop/.png)
        # img2= img2.resize((100,40),Image.ANTIALIAS)
        # self.photoimg2= ImageTk.PhotoImage(img2)

        # lblimg= Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=0, width=230, height=140)

        # labelFrame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",  font=(
            "times new roman", 18, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # labels and entries
        # customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=(
            "times new roman", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btnFetchData = Button(labelframeleft, text="Fetch Data", command=self.fetch_contact, font=(
            "times new roman", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347, y=4)

        # Check_in Date
        check_in_date = Label(labelframeleft, text="Check_in Date:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=(
            "times new roman", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check_out Date
        lbl_Check_out = Label(labelframeleft, text="Check_Out Date:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=(
            "times new roman", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_RoomType["value"] = (
            "Single", "Double", "Luxury", "Sweet", "Deluxe")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=(
            "times new roman", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=(
            "times new roman", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No Of Days:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofday, font=(
            "times new roman", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPT = Label(labelframeleft, text="Paid Tax:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblPT.grid(row=7, column=0, sticky=W)

        txtPT = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=(
            "times new roman", 13, "bold"), width=29)
        txtPT.grid(row=7, column=1)

        # Sub Total
        lblST = Label(labelframeleft, text="Sub Total:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblST.grid(row=8, column=0, sticky=W)

        txtST = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=(
            "times new roman", 13, "bold"), width=29)
        txtST.grid(row=8, column=1)

        # Total Cost
        lblTC = Label(labelframeleft, text="Total Cost", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblTC.grid(row=9, column=0, sticky=W)

        txtTC = ttk.Entry(labelframeleft, textvariable=self.var_total, font=(
            "times new roman", 13, "bold"), width=29)
        txtTC.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(labelframeleft, text="BILL", font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # -----------Buttons--------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET",  font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Rightside image
        # img3= Image.open("C:/Users/gurun/Desktop/.png)
        # img3= img2.resize((520,200),Image.ANTIALIAS)
        # self.photoimg3= ImageTk.PhotoImage(img3)

        # lblimg= Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        # lblimg.place(x=760,y=55, width=520, height=200)

        # table frame search system

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=(
            "times new roman", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_gender = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=(
            "times new roman", 13, "bold"), width=24, state="read only")
        combo_gender["value"] = ("Contact", "Room")
        combo_gender.current(0)
        combo_gender.grid(row=0, column=1)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=(
            "times new roman", 13, "bold"), width=29)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=(
            "times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=(
            "times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk. Treeview(details_table, column=(
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays", "show"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkin", text="Check-in")
        self.room_Table.heading("checkout", text="Check-out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noOfdays", text="NoOfDays")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=120)
        self.room_Table.column("checkin", width=120)
        self.room_Table.column("checkout", width=120)
        self.room_Table.column("roomtype", width=120)
        self.room_Table.column("roomavailable", width=120)
        self.room_Table.column("meal", width=120)
        self.room_Table.column("noOfdays", width=120)
        self.room_Table.pack(fill=BOTH, expand=1)

    # All data fetch
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="local", username="root", password="", database="")
            my_cursor = conn.cursor()
            query = ("Select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "This Number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:",
                                font=("times new roman", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=(
                    "times new roman", 12, "bold"))
                lbl.place(x=90, y=0)

                # Gender

                conn = mysql.connector.connect(
                    host="local", username="root", password="", database="")
                my_cursor = conn.cursor()
                query = ("Select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:",
                                  font=("times new roman", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl = Label(showDataframe, text=row, font=(
                    "times new roman", 12, "bold"))
                lbl.place(x=90, y=30)

                # Email
                conn = mysql.connector.connect(
                    host="local", username="root", password="", database="")
                my_cursor = conn.cursor()
                query = ("Select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Email:",
                                  font=("times new roman", 12, "bold"))
                lblGender.place(x=0, y=60)

                lbl = Label(showDataframe, text=row, font=(
                    "times new roman", 12, "bold"))
                lbl.place(x=90, y=60)

                # Nationality
                conn = mysql.connector.connect(
                    host="local", username="root", password="", database="")
                my_cursor = conn.cursor()
                query = ("Select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Nationality:",
                                  font=("times new roman", 12, "bold"))
                lblGender.place(x=0, y=90)

                lbl = Label(showDataframe, text=row, font=(
                    "times new roman", 12, "bold"))
                lbl.place(x=90, y=90)

                # Address
                conn = mysql.connector.connect(
                    host="local", username="root", password="", database="")
                my_cursor = conn.cursor()
                query = ("Select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Address:",
                                  font=("times new roman", 12, "bold"))
                lblGender.place(x=0, y=120)

                lbl = Label(showDataframe, text=row, font=(
                    "times new roman", 12, "bold"))
                lbl.place(x=90, y=120)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
