from tkinter import messagebox
from tkinter.font import families
import pytest


def login(username, password):
    if username == "" and password == "":
        return False
    elif len(username) < 4 and len(password) < 4:
        return False
    else:
        return True


def test_login_emtpy_field():
    assert login("", "") == False


def test_login_emtpy_len():
    assert login("ab", "ab") == False


def test_valid_login():
    assert login("srijangrg", "12345") == True


# signup

def signup(username, password, confirm_password):
    if username == "" and password == "" and confirm_password == "":
        return False
    elif len(username) < 4 and len(password) < 4 and len(confirm_password) < 4:
        return False
    elif password != confirm_password:
        return False
    else:
        return True


def test_signup_emtpy_field():
    assert signup("", "", "") == False


def test_login_signup_len():
    assert signup("ab", "ab", "ab") == False


def test_unmatched_password():
    assert signup("srijangrg", "12345", "56789") == False


def test_valid_signup():
    assert signup("srijangrg", "12345", "12345") == True


# customer

def customer(customer_ref, customer_name, mother_name, gender, post_code, mobile_number, email, nationality, id_proof, id_number, address):
    if len(customer_ref) < 1 and len(customer_name) < 1 and len(mother_name) < 1 and len(gender) < 1 and len(post_code) < 1 and len(mobile_number) < 1 and len(email) < 1 and len(nationality) < 1 and len(id_proof) < 1 and len(id_number) < 1 and len(address) < 1:
        return "All fields are required"
    elif "@" not in email:
        return "invalid email"
    elif len(mobile_number) != 10:
        return "not valid phone number"

    else:
        return"valid data"


def test_customer_empty_data():
    assert customer("", "", "", "", "", "", "", "", "",
                    "", "") == "All fields are required"


def test_customer_email_validator():
    assert customer("12", "SrijanGurung", "DeepaGurung", "male", "1100", "9843807234",
                    "srijangrggmail.com", "nepali", "Citizenship", "1200", "imadole") == "invalid email"


def test_customer_phone_validator():
    assert customer("12", "SrijanGurung", "DeepaGurung", "male", "1100", "98438072",
                    "srijangrg@gmail.com", "nepali", "Citizenship", "1200", "imadole") == "not valid phone number"


def test_customer_valid_data():
    assert customer("12", "SrijanGurung", "DeepaGurung", "male", "1100", "9843807234",
                    "srijangrg@gmail.com", "nepali", "Citizenship", "1200", "imadole") == "valid data"

# roombook


def roombook(customer_contact, check_in_date, check_out_date, room_type, available_room, meal, no_of_days, paid_tax, sub_total, total_cost):
    if len(customer_contact) < 1 and len(check_in_date) < 1 and len(check_out_date) < 1 and len(room_type) < 1 and len(available_room) < 1 and len(meal) < 1 and len(no_of_days) < 1 and len(paid_tax) < 1 and len(sub_total) < 1 and len(total_cost) < 1:
        return "All fields are required"
    elif customer_contact != "12":
        return False
    else:
        return True


def test_customer_data():
    assert roombook("", "", "", "", "", "", "", "", "", "") == "All fields are required"


def test_roombook_contact_number():
    assert roombook("12","12","12","12","12","12","12","12","12","12") == True


# details
def details(floor, room_no, room_type):
    if len(floor) < 1 and len(room_no) < 1 and len(room_type)<1:
        return "All fields are required"
    # else:
    #     return True


def test_data():
    assert details("", "", "") == "All fields are required"
