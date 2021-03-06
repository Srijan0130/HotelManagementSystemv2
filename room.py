from tkinter import*
#from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import psycopg2


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
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="dark green",
                          fg="white", bd=4, relief=RIDGE)
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
            "times new roman", 13, "bold"), width=29)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        #btnFetchData = Button(labelframeleft, text="Fetch Data", command=self.fetch_contact, font=(
            #"times new roman", 8, "bold"), bg="dark green", fg="white", width=8)
        #btnFetchData.place(x=347, y=4)

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

        # conn = mysql.connector.connect(
        #     host="local", username="root", password="", database="")
        # my_cursor = conn.cursor()
        # my_cursor.execute("select RoomType from details")
        # ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_RoomType["value"] = ("SINGLE","DOUBLE","LUXURY","DELUXE","PLATINUM","SWEET")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        # txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=(
        # "times new roman", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1)

        # conn = mysql.connector.connect(
        #     host="local", username="root", password="", database="")
        # my_cursor = conn.cursor()
        # my_cursor.execute("select RoomNo from details")
        # rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_RoomNo["value"] = ("B45","C90","F34","G56")
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

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
        # btnBill = Button(labelframeleft, text="BILL", command=self.total, font=(
        #     "times new roman", 12, "bold"), bg="dark green", fg="white", width=10)
        # btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # -----------Buttons--------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_details, font=(
            "times new roman", 12, "bold"), bg="dark green", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update, font=(
            "times new roman", 12, "bold"), bg="dark green", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", command=self.delete, font=(
            "times new roman", 12, "bold"), bg="dark green", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET", command=self.reset, font=(
            "times new roman", 12, "bold"), bg="dark green", fg="white", width=10)
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

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=(
            "times new roman", 11, "bold"), bg="dark green", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_details, font=(
            "times new roman", 11, "bold"), bg="dark green", fg="white", width=10)
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

        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_details()

    # add data

    def add_details(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All filds are required", parent=self.root)
        else:
            try:
                conn = psycopg2.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        password='12345',
                                        database='hotelmanagement')  # To remove slash
                cursor = conn.cursor()
                cursor.execute("insert into roombook ( customer_contact, check_in_date,check_out_date,room_type,available_room,meal,no_of_days,paid_tax,sub_total,total_cost) values (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)", (

                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofday.get(),
                    self.var_paidtax.get(),
                    self.var_actualtotal.get(),
                    self.var_total.get()
                ))

                # cursor.execute("insert info room value(%s,%s,%s,%s,%s,%s,%s)", (
                #     self.var_contact.get(),
                #     self.var_checkin.get(),
                #     self.var_checkout.get(),
                #     self.var_roomtype.get(),
                #     self.var_roomavailable.get(),
                #     self.var_meal.get(),
                #     self.var_noofday.get()

                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("Success", "Room has been booked")
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    # fetch data
    def fetch_details(self):
        conn = psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                user='postgres',
                                password='12345',
                                database='hotelmanagement')  # To remove slash
        my_cursor = conn.cursor()
        my_cursor.execute("select*from roombook")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofday.set(row[6])

    # Update Function

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter mobile number", parent=self.root)
        else:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash
            cursor = conn.cursor()
            cursor.execute("update roombook set check_in_date=%s, check_out_date=%s, room_type=%s,available_room=%s,meal=%s,no_of_days=%s,paid_tax=%s,sub_total=%s,total_cost=%s where customer_contact=%s ", (

                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofday.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get(),
                self.var_contact.get()

            ))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo(
                "Update", "Room details has been updated success", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno(
            "Hotel Management System", "do you want to delete this customer", parent=self.root)
        if delete > 0:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash
            cursor = conn.cursor()
            query = "delete from roombook where customer_contact=%s"
            value = (self.var_contact.get(),)
            cursor.execute(query, value)
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
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofday.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    # All data fetch

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter Contact Number", parent=self.root)
        else:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash
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

    # search system

    def search(self):
        conn = psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                user='postgres',
                                password='12345',
                                database='hotelmanagement')  # To remove slash
        my_cursor = conn.cursor()
        if self.search_var.get() == 'Contact':
            postgreSQL_select_Query = "select * from roombook where customer_contact = %s"
        else:
            postgreSQL_select_Query = "select * from roombook where available_room = %s"
        my_cursor.execute(postgreSQL_select_Query, (self.txt_search.get(),))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(
                *self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofday.set(abs(outDate-inDate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofday.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%2f" % ((q5)*0.1))
            ST = "Rs."+str("%2f" % ((q5)))
            TT = "Rs."+str("%2f" % ((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofday.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%2f" % ((q5)*0.1))
            ST = "Rs."+str("%2f" % ((q5)))
            TT = "Rs."+str("%2f" % ((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Deluxe"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofday.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%2f" % ((q5)*0.1))
            ST = "Rs."+str("%2f" % ((q5)))
            TT = "Rs."+str("%2f" % ((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
