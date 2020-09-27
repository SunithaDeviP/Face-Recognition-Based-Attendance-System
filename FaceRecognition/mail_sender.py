import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from os
username = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
password = "sunitha1998"
toaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
addrlist = []

def addr_list():
    
    rootdir = "/home/q8/Desktop/FINAL_YEAR_PROJECT/FaceRecognition/Result/"
    Files = []
    for subdir, dirs, Files in os.walk(rootdir):
        print(Files)

    for val in Files: 
        str1 = rootdir + val
        print(str1)
        addrlist.append(str1)

def send_mail_gmail(username,password,toaddrs_list,msg_text,fromaddr=None,subject="Test mail",attachment_path_list=None):

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username, password)
    #s.set_debuglevel(1)
    msg = MIMEMultipart()
    sender = fromaddr
    recipients = toaddrs_list
    msg['Subject'] = subject
    if fromaddr is not None:
        msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    if attachment_path_list is not None:
        for each_file_path in attachment_path_list:
            try:
                file_name=each_file_path.split("/")[-1]
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(each_file_path, "rb").read())

                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                msg.attach(part)
            except:
                print ("could not attache file")
    msg.attach(MIMEText(msg_text,'html'))
    s.sendmail(sender, recipients, msg.as_string())

    addr_list()
    tolist = ["sunithadevi.p.2016.it@rajalakshmi.edu.in"]
    send_mail_gmail("sunithadevi.p.2016.it@rajalakshmi.edu.in","sunitha1998", "Attendance Report", tolist,"Automated Attendance System", addrlist)