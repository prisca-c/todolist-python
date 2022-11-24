from tkinter import *
from data.users import create_user, select_user


class Login:

    def __init__(self, master):
        Label(master, text="Username").pack()
        username = StringVar()
        Entry(master, textvariable=username).pack()

        Label(master, text="Password").pack()
        password = StringVar()
        Entry(master, textvariable=password, show='*').pack()

        #  Button that will check if the user exists in the database
        Button(master, text="Login", command=lambda: select_user(username.get(), password.get())).pack()
        Button(master, text="Create Account", command=lambda: CreateAccount()).pack()


class CreateAccount:

    def __init__(self):
        master = Tk()
        frame = Frame(master)
        frame.pack()
        master.title("Create Account")
        master.geometry("300x250")
        Label(frame, text="Create a new Account").pack(fill='both', pady=15)

        Label(frame, text="Username").pack()
        username = StringVar()
        Entry(frame, textvariable=username).pack()

        Label(frame, text="Password").pack()
        password = StringVar()
        Entry(frame, textvariable=password, show='*').pack()

        #  Button that will create a new user in the database
        Button(frame, text="Create",
               command=lambda: create_user(username.get(), password.get())).pack(side=LEFT, padx=5, pady=15)
        Button(frame, text="Cancel",
               command=lambda: frame.destroy()).pack(side=RIGHT, padx=5, pady=15)
