from tkinter import*
#from PIL import Image,ImageTk
from tkinter import ttk
import random
#import mysql.connector
from tkinter import messagebox
import psycopg2


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # variable
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        # title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        # img2= Image.open("C:/Users/gurun/Desktop/.png)
        # img2= img2.resize((100,40),Image.ANTIALIAS)
        # self.photoimg2= ImageTk.PhotoImage(img2)

        # lblimg= Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=0, width=230, height=140)

        # labelFrame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",  font=(
            "times new roman", 18, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # labels and entries
        # custRef
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=(
            "times new roman", 13, "bold"), width=29, )
        enty_ref.grid(row=0, column=1)

        # cust name
        cname = Label(labelframeleft, font=("times new roman", 12,
                      "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=(
            "times new roman", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # mother name
        lblmname = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=(
            "times new roman", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lblPostCode = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Post Code:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=(
            "times new roman", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # mobile number
        lblMobile = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Mobile Number:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=(
            "times new roman", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="E-mail:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=(
            "times new roman", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # nationality
        lblNationality = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=(
            "times new roman", 13, "bold"), width=27, state="read only")
        combo_Nationality["value"] = (
            "Nepali", "American", "African", "Australian", "British")
        combo_Nationality .current(0)
        combo_Nationality .grid(row=7, column=1)

        # idproof type combobox
        lblIdProof = Label(labelframeleft, font=("times new roman", 12, "bold"), text="ID Proof:", padx=2,
                           pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_Id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("times new roman", 13, "bold"), width=27,
                                state="read only")
        combo_Id["value"] = ("Citizenship", "Passport", "Driving License", )
        combo_Id.current(0)
        combo_Id.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=(
            "times new roman", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # address
        lblAddress = Label(labelframeleft, font=(
            "times new roman", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=(
            "times new roman", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

        # -----------Buttons--------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

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

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=(
            "times new roman", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_gender = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=(
            "times new roman", 13, "bold"), width=24, state="read only")
        combo_gender["value"] = ("Mobile", "Ref")
        combo_gender.current(0)
        combo_gender.grid(row=0, column=1)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=(
            "times new roman", 13, "bold"), width=29)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=(
            "times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_details, font=(
            "times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table

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
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_details()

    def add_details(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
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
                cursor.execute("insert into CUSTOMERS (customer_ref,customer_name,mother_name,gender,post_code,mobile_number,email,nationality,id_proof,id_number,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()

                # my_cursor = conn.cursor()
                # my_cursor.exexute("insert info customer
                # conn.commit()

                conn.close()
                self.fetch_details()
                # messagebox.showwinfo("Success", "Customer has been added")
            except Exception as es:
                print(es)
                messagebox.showwarning(
                    "Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_details(self):
        conn = psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                user='postgres',
                                password='12345',
                                database='hotelmanagement')  # To remove slash

        cursor = conn.cursor()
        cursor.execute("select*from CUSTOMERS")
        rows = cursor.fetchall()
        print(rows)
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()
        pass

    def get_cursor(self, events=""):
        cursor_row = self.Cust_Details_Table.Focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row=[0]),
        self.var_cust_name.set(row=[1]),
        self.var_mother.set(row=[2]),
        self.var_gender.set(row=[3]),
        self.var_post.set(row=[4]),
        self.var_mobile.set(row=[5]),
        self.var_email.set(row=[6]),
        self.var_nationality.set(row=[7]),
        self.var_id_proof.set(row=[8]),
        self.var_id_number.set(row=[9]),
        self.var_address.set(row=[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror(
                "Error", "Please enter mobile number", parent=self.root)
        else:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash

            cursor = conn.cursor()
            cursor.execute("update customers set customer_name=%s, mother_name=%s,gender=%s,post_code=%s,mobile_number=%s,email=%s,nationality=%s,id_proof=%s,id_number=%s,address=%s where customer_ref=%s ", (

                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo(
                "Update", "Customer details has been updated success", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno(
            "Hotel Management System", "do you want to deletebthis customer", parent=self.root)
        if delete > 0:
            conn = psycopg2.connect(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password='12345',
                                    database='hotelmanagement')  # To remove slash

            cursor = conn.cursor()
            query = "delete from customers where customer_ref=%s"
            value = (self.var_ref.get(),)
            cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_details()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                user='postgres',
                                password='12345',
                                database='hotelmanagement')  # To remove slash

        cursor = conn.cursor()
        rows = None
        if self.search_var.get() == 'Mobile':
            postgreSQL_select_Query = "select * from REGISTER where mobile_number = %s"
        else:
            postgreSQL_select_Query = "select * from REGISTER where username = %s"

            cursor.execute("select * from customer where " +
                        str(self.search_var.get()) + "LIKE'%"+str(self.txt_search.get()+"%'"))
            rows = cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
