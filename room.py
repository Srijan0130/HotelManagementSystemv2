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

        enty_contact = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btnFetchData = Button(labelframeleft, text="Fetch Data", font=(
            "times new roman", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347, y=4)

        # Check_in Date
        check_in_date = Label(labelframeleft, text="Check_in Date:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check_out Date
        lbl_Check_out = Label(labelframeleft, text="Check_Out Date:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_RoomType["value"] = (
            "Single", "Double", "Luxury", "Sweet", "Deluxe")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No Of Days:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPT = Label(labelframeleft, text="Paid Tax:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblPT.grid(row=7, column=0, sticky=W)

        txtPT = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtPT.grid(row=7, column=1)

        # Sub Total
        lblST = Label(labelframeleft, text="Sub Total:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblST.grid(row=8, column=0, sticky=W)

        txtST = ttk.Entry(labelframeleft, font=(
            "times new roman", 13, "bold"), width=29)
        txtST.grid(row=8, column=1)

        # Total Cost
        lblTC = Label(labelframeleft, text="Total Cost", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblTC.grid(row=9, column=0, sticky=W)

        txtTC = ttk.Entry(labelframeleft, font=(
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

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk. Treeview(details_table, column=(
            "ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Poof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
