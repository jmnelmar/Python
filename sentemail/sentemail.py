import smtplib, ssl

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


port = 465

#sender, password = read_creds()
sender = 'medreminderapp431@gmail.com'
password = 'medreminder2020'

print ('user:{} ,Pass: {}'.format(sender,password))
recieve = sender

message = """\
Subject: Python Email Tutorial

This is from python!

Tech With Tim
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)

print("sent email!")
#https://myaccount.google.com/lesssecureapps