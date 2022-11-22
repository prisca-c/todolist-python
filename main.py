from tkinter import Tk
from data.db_config import create_main_tables


class Main:
    def __init__(self, master):
        self.master = master
        master.title("My ToDo List")
        master.geometry("1280x720")

        create_main_tables()


root = Tk()
app = Main(root)
root.mainloop()
