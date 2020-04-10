import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def otp_on_email(email_id):
    fromaddr = "demosenderemail@gmail.com"  #Sender's Email id 
    senders_pass = "demopass@123" #password of sender's Email id 
    toaddr =  email_id #reciever's Email ID

    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "OTP by ZeeBank"

    otp = random.randrange(100001,999999) #Generating Random number b/w 100001 and 999999
    body = """
            Your OTP is [ {} ] and you can use it to verify your account.
            _____________________________
            @expert.py
            Feel free to contact
    """.format(otp)

    msg.attach(MIMEText(body, 'plain')) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, senders_pass) 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 
    c_txt="OPT send on your email ({}******{}  )".format(toaddr[0:2],toaddr[6:])
    print (c_txt)
    return otp

entered_email_id = input("Ënter you valid Email ID : ")
generated_otp = otp_on_email(entered_email_id)

user_entered_otp = int(input("Ënter OTP : "))
if generated_otp == user_entered_otp:
    print("OTP matched")
else :
    print("You entered wrong OTP")