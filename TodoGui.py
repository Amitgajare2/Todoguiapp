import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

# database connection
conn = sqlite3.connect('data.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')

def show():
    query = "SELECT * FROM todo;"
    return conn.execute(query)

def insertdata(task):
    query = "INSERT INTO todo(task) VALUES(?);"
    conn.execute(query, (task,))
    conn.commit()

def deletebytask(taskval):
    query = "DELETE FROM todo WHERE task =?;"
    conn.execute(query, (taskval,))
    conn.commit()


# splash screen  
splash_root = Tk()
splash_root.title("ToDo")
splash_root.iconbitmap("logo.ico")
splash_root.geometry("300x200")
splash_root.config(bg='black')

fra =  Label(splash_root, text="ToDO", font=('champion', 40), fg="white", bg="black")
fra.pack()
fra.place(anchor="center", relx=0.5, rely=0.5)


def main_window():
# add and delete function 
    def add():
        if(len(addtask.get()) == 0):
            messagebox.showerror(
                "ERROR", "No data Available\nPlease Enter Some Task")
        else:
            insertdata(addtask.get())
            addtask.delete(0, END)
            populate()

    def deletetask(event):
        deletebytask(listbox.get(ANCHOR))
        populate()

# main screen start 
    splash_root.destroy()
    main = tkinter.Tk()
    main.title("TODO")
    main.geometry("500x600")
    main.resizable(False, False)
    main.iconbitmap("logo.ico")
    main.configure(
        background="#1d1d1d",
    )

    tkinter.Label(
        main,
        text="TODO APP",
        background="#1d1d1d",
        foreground="#eeeeee",
        font=("champion 25")
    ).pack(pady=10)

    addframe = tkinter.Frame(
        main,
        bg="#1d1d1d",
    )
    addframe.pack()
    addtask = tkinter.Entry(
        addframe,
        font=("Verdana"),
        background="#eeeeee",
    )
    addtask.pack(ipadx=20, ipady=5, side="left")

    addbtn = tkinter.Button(
        addframe,
        text="ADD TASK",
        command=add,
        background="#000000",
        foreground="#eeeeee",
        relief="flat",
        font=("Verdana"),
        highlightcolor="#000000",
        activebackground="#1d1d1d",
        border=0,
        activeforeground="#eeeeee",
    )
    addbtn.pack(padx=20, ipadx=20, ipady=5)

    tkinter.Label(
        main,
        text="Your Tasks",
        background="#1d1d1d",
        foreground="#eeeeee",
        font=("Calibri", 18),
    ).pack(pady=10)

# show function 
    def populate():
        listbox.delete(0, END)
        for rows in show():
            listbox.insert(END, rows[1])


    taskframe = tkinter.Frame(
        main,
        bg="#1d1d1d",
    )
    taskframe.pack(fill=BOTH, expand=300)
    scrollbar = Scrollbar(taskframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(
        taskframe,
        font=("System 17 bold"),
        bg="#1d1d1d",
        fg="#eeeeee",
        selectbackground="#eeeeee",
        selectforeground="#1d1d1d",
    )
    listbox.pack(fill=BOTH, expand=300)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    listbox.bind("<Double-Button-1>", deletetask)
    listbox.bind("<Delete>", deletetask)

    populate()

    tkinter.Label(
        main,
        text="TIP : Double Click On A Task to Delete",
        background="#1d1d1d",
        foreground="#FFEB3B",
        font=("Perpetua", 12),
    ).pack(side=BOTTOM, pady=10)

splash_root.after(1000, main_window)
mainloop()
