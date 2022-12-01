from tkinter import *


class Dashboard:
    def __init__(self, master):
        Label(master, text="Dashboard", fg="white", bg='#5fce9c', bd=20, font=('arial', 20, 'bold')).pack(fill=X)

        main = Frame(master)
        main.pack()
        main.configure(bg="white", width=1280, height=720,
                       highlightthickness=4, relief="solid", padx=10, pady=10, highlightbackground='#5fce9c')
        Label(main, text="Tasks", bg="white", font=('arial', 10, 'bold')).pack(pady=10, padx=10)
        table = Frame(main)
        table.pack()
        table.configure(bg="white", width=1280, height=720/1.5,
                        highlightthickness=4, relief="solid", padx=10, pady=10, highlightbackground='#5fce9c')
        Label(main, text="Create a new task", bg="white", font=('arial', 10, 'bold')).pack(pady=10, padx=10)
        form = Frame(main)
        form.pack()
        form.configure(bg="white", width=1280/2, height=720/5,
                          highlightthickness=4, relief="solid", padx=10, pady=10, highlightbackground='#5fce9c')

