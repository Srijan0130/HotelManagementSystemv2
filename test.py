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
        return "on invalid email"
    elif len(mobile_number) == 10:
        return "not valid phone number"

    else:
        return"valid data"


def test_customer_empty_data():
    assert customer("", "", "", "", "", "", "", "", "",
                    "", "") == "All fields are required"

def test_customer_email_validator():
    assert customer("12","SrijanGurung")