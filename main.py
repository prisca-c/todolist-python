from tkinter import Tk


class Main:
    def __init__(self, master):
        self.master = master
        master.title("My ToDo List")
        master.geometry("1280x720")


root = Tk()
app = Main(root)
root.mainloop()
