from .database import *
from .functions import *



def login_db():

    names = ["adminBG", "adminLV"]
    usernames = ["adminBG", "adminLv"]
    passwrods = ["enodve34","strangepassword"]

    hashed_passwords = stauth.Hasher(passwrods).generate()


    for(usernames,names,hashed_passwords)in zip(usernames,names,hashed_passwords):
        db.insert_user(usernames,names,hashed_passwords)

