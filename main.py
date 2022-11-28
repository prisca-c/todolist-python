from tkinter import Tk
from data.db_config import create_main_tables
from components.connect import Login


class Main:
    def __init__(self, master):
        self.master = master
        master.title("TODO")
        master.geometry("1280x720")
        master.configure(bg="white")

        create_main_tables()
        #  Button(master, text="Create Account", command=main).pack()
        Login(master)


root = Tk()
app = Main(root)
root.mainloop()
