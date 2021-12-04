import sqlite3, hashlib
from tkinter import *
import base64
import os
import time
import sys


window = Tk()


window.title("vaultl gui")

def loginscreen():
    window.geometry("350x300")

    lbl=Label(window, text="vault login enter password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    Text= Entry(window,width="20", show="*")
    Text.pack()
    Text.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def checkpassword():
        password= "testpw"
        if password == Text.get():
           passwordVault()
           folderlock()
        else:
            lbl1.config(text="wrong password")    


    btn= Button(window,text="submit", command=checkpassword)
    btn.pack(pady=20)
def passwordVault():    
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("768x360")    

    lbl= Label(window, text="Vault opened")
    lbl.config(anchor=CENTER)
    lbl.pack()


def folderlock():

    os.chdir('''D:\\private project''')
    if not os.path.exists("Locker"):
        if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
            os.mkdir("Locker")
        else:
            os.popen('attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}","Locker")
            sys.exit()
            

    else:
        os.rename("Locker","Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
        os.popen('attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
        sys.exit()
        

    


loginscreen()    

window.mainloop()
