import os
from deta import  Deta
from dotenv import load_dotenv # pip install python-dotenv


load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
#init with project key
deta = Deta(DETA_KEY)

#conn to db
db = deta.Base("user_db")

def insert_user(username,name,password):
    '''RETURNS THE USER ON A SUCCESSFUL USER CREATION , OTHERWISE RAISES AN ERROR'''
    return db.put({"key":username,"name":name,"password":password})


def fetch_all_users():
    """returns a dict of alll users"""


    res = db.fetch()
    return res.items

def get_key(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return f'{key}: '

    return "key doesn't exist"


def get_user(username):
    return db.get(username)

def update_user(username,updates):

    form = {"key":input("enter username"),"name":input("Enter new name"),"password":input("Enter new password ")}
    temp = ""
    temp += get_key(form["key"],form)
    temp += form["key"]
    update_user(form["key"],updates={temp})


    return db.update(updates,username)
