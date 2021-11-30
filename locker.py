import base64
import os
import time
import sys

password = "password"  
encode = base64.b64encode(password.encode("utf-8"))

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    pw = str(input("Enter your password for Lock or Unlock your folder: "))

    if pw == base64.b64decode(encode).decode("utf-8")  :
    # Change Dir Path where you have Locker Folder
        os.chdir('''C:\\Users\\cybor\\Desktop\\THE PROJECT ONE''')
    # If Locker folder or Recycle bin does not exist then we will be create Locker Folder 
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
        
    else:
        print ("Wrong password!, Please Enter right password")
        time.sleep(5)
        goto(1)
