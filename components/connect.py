from tkinter import *
from components.users import create_user, check_user, select_username


def handle_create_user(master, username, password):
    if username == "" or password == "":
        print("Username or password is empty")
    else:
        create_user(username, password)
        master.destroy()


class Login:

    def __init__(self, master):
        
        Label(master, text="TODO !", bd=20, font=('arial', 20, 'bold')
              , fg="white", bg="#5fce9c").pack(fill=X)

        frame = Frame(master)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        frame.configure(bg="white")

        Label(frame, text="Connect to your account", bg="white", font=('arial', 10, 'bold')).pack(pady=10, padx=10)
        Label(frame, text="Username", bg="white").pack()
        username = StringVar()
        Entry(frame, textvariable=username).pack()

        Label(frame, text="Password", bg="white").pack()
        password = StringVar()
        Entry(frame, textvariable=password, show='*').pack()

        buttons = Frame(frame)
        buttons.pack(pady=15)
        buttons.configure(bg="white")

        #  Button that will check if the user exists in the database
        Button(buttons, text="Login", bg="#5fce9c", width=16, height=1,
               command=lambda: check_user(username.get(), password.get())).pack()
        Button(buttons, text="Create Account", bg="#e8c976", width=16, height=1,
               command=lambda: CreateAccount(master)).pack(pady=10)


class CreateAccount:

    def __init__(self, master):
        frame = Toplevel(master)
        frame.title("TODO - Create Account")
        frame.geometry("300x250")
        frame.configure(bg="white")
        frame.iconbitmap("assets/icon.ico")
        Label(frame, text="Create a new Account", bg="#5fce9c", bd=15, fg="white"
              , font=('arial', 10, 'bold')).pack(fill=BOTH)

        Label(frame, text="Username", bg="white").pack()
        username = StringVar()
        Entry(frame, textvariable=username).pack()

        Label(frame, text="Password", bg="white").pack()
        password = StringVar()
        Entry(frame, textvariable=password, show='*').pack()

        #  Button that will create a new user in the database
        Button(frame, text="Create", bg="white",
               command=lambda: handle_create_user(master, username.get(), password.get())).pack(padx=5, pady=15)
        Button(frame, text="Cancel", bg="white",
               command=lambda: frame.destroy()).pack(padx=5)
