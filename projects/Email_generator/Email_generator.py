import smtplib
import ssl

s_email=input("Enter your emai address")
s_passw=input("Enter the password of your mail")

def read_cred(f):
    try:
        user =''
        with open(f, "r") as f:
            mails=[]
            for mail in f.readlines():
                if("\n" in mail):mail=mail.replace("\n","")
                mail.append(mail)
        return mails
    except FileNotFoundError:
        file=input("Enter the file containing the recievers email")
        read_cred(file)
    
def m_read_cred(f):
    try:
        mess=f.read()
        return mess
    except FileNotFoundError:
        m_file=input("Enter the file containing the message")
        m_read_cred(m_file)
file=input("Enter the file containing the recievers email")
mails= read_cred(file)

m_file=input("Enter the file containing the message")
messg=m_file.read(m_file)
port = 465

for mail in mails:
    message =f"""\
    Subject: Welcome To Secure Chat This is your password

    {messg}

    Thank you
    """

    context = ssl.create_default_context()

    print("-----------------Starting to send-----------------")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as serv:
        serv.login(s_email, s_passw)
        serv.sendmail(s_email, mail, message)

    print("------------------Email Sent to {}----------------------".format(mail))