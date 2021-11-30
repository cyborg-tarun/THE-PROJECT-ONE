import sqlite3, hashlib
from tkinter import *

window = Tk()


window.title("vaultl gui")

def loginscreen():
    window.geometry("350x300")

    lbl=Label(window, text="vault login")
    lbl.config(anchor=CENTER)
    lbl.pack()
    Text= Entry(window,width="20")
    Text.pack()
    btn= Button(window,text="submit", command="checkpassword")
    btn.pack(pady=20)

loginscreen()    

window.mainloop()