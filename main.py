from tkinter import Tk
from data.db_config import main


class Main:
    def __init__(self, master):
        self.master = master
        master.title("My ToDo List")
        master.geometry("1280x720")

        self.db = main()


root = Tk()
app = Main(root)
root.mainloop()
