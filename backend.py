from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("REGISTRATION")
root.geometry("380x230")
root.resizable(0, 0)

# ================================================# DATABASE #================================================#
def database():
    global conn, cursor
    conn = sqlite3.connect("Test App/Registration.db")
    print ("Created Database")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `pydb` (fname TEXT, lname TEXT, mid TEXT, username TEXT, password TEXT, confirm_password TEXT)")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `pydb` VALUES(?,?,?,?,?,?)",(FNAME.get(), LNAME.get(), MID.get(), USERNAME.get(), PASSWORD.get(), CONFIRM_PASSWORD.get()))
        conn.commit()

# ================================================# Login #================================================#
def register(event = None):
    database()

    if FNAME.get()=="" or LNAME.get()=="" or MID.get=="" or USERNAME.get()=="" or PASSWORD.get()=="" or CONFIRM_PASSWORD.get()=="":
        messagebox.showinfo('Registration', 'Please complete the required field!')

    else:
        cursor.execute("INSERT INTO `pydb` VALUES(?,?,?,?,?,?)",(FNAME.get(), LNAME.get(), MID.get(), USERNAME.get(), PASSWORD.get(), CONFIRM_PASSWORD.get()))
        messagebox.askquestion('Registration', 'Confirm Registration?')
        if 'yes':
            messagebox.showinfo('Registration', 'Registered')
            FNAME.set("")
            LNAME.set("")
            MID.set("")
            USERNAME.set("")
            PASSWORD.set("")
            CONFIRM_PASSWORD.set("")
        else:
            quit()


# ================================================# VARIABLE #================================================#
USERNAME = StringVar()
PASSWORD = StringVar()
FNAME = StringVar()
LNAME = StringVar()
MID = StringVar()
CONFIRM_PASSWORD = StringVar()

Top=Frame(root, bd=2)
Top.pack(side=TOP, fill=X)
Form=Frame(root)
Form.pack()

# ================================================# ENTRIES #================================================#
ent_FName = Entry(Form, textvariable=FNAME)
ent_FName.grid(column=1, row=1)

ent_Surname = Entry(Form, textvariable=LNAME)
ent_Surname.grid(column=1, row=2)

ent_Mid = Entry(Form, textvariable=MID)
ent_Mid.grid(column=1, row=3)

ent_Username = Entry(Form, textvariable=USERNAME)
ent_Username.grid(column=1, row=4)

ent_Password = Entry(Form, textvariable=PASSWORD, show = "*")
ent_Password.grid(column=1, row=5)

ent_ConPas = Entry(Form, textvariable=CONFIRM_PASSWORD, show = "*")
ent_ConPas.grid(column=1, row=6)

# ================================================# LABELS #================================================#
lbl_Register = Label(Form, text="--REGISTER--", fg="Red")
lbl_Register.grid(sticky=E, row=0)

lbl_FName = Label(Form, text="First Name:", fg="Green")
lbl_FName.grid(sticky=E, row=1)

lbl_Surname = Label(Form, text="Surname:", fg="Green")
lbl_Surname.grid(sticky=E, row=2)

lbl_Mid = Label(Form, text="Middle Initials:", fg="Green")
lbl_Mid.grid(sticky=E, row=3)

lbl_Username = Label(Form, text="Username:", fg="Red")
lbl_Username.grid(sticky=E, row=4)

lbl_Password = Label(Form, text="Password:", fg="Red")
lbl_Password.grid(sticky=E, row=5)

lbl_ConPas = Label(Form, text="Confirm Password:", fg="Red")
lbl_ConPas.grid(sticky=E, row=6)

lbl_text = Label(Form)
lbl_text.grid(row=9, columnspan=2)

# ================================================# BUTTONS #================================================#
btn_register = Button(Form, text="Register", fg="Green", bg="Black", command=register)
btn_register.grid(column=0, row=10)

# ================================================ END ================================================ #
root.mainloop()