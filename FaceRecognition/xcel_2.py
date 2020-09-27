# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def send_mail_it():
    print("Preparing to send mail ")
    fromaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    toaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "IT Attendance sheet"
    body = ""
    msg.attach(MIMEText(body, 'plain')) 
    filename = "IT.xlsx"
    attachment = open("/home/q8/Desktop/FINAL_YEAR_PROJECT/FaceRecognition/Result/IT.xlsx", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "sunitha1998") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    print("mail sent successfully") 

def send_mail_cse():
    print("Preparing to send mail ")
    fromaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    toaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "CSE Attendance sheet"
    body = ""
    msg.attach(MIMEText(body, 'plain')) 
    filename = "CSE.xlsx"
    attachment = open("/home/q8/Desktop/FINAL_YEAR_PROJECT/FaceRecognition/Result/CSE.xlsx", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "sunitha1998") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    print("mail sent successfully") 

def send_mail_ece():
    print("Preparing to send mail ")
    fromaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    toaddr = "sunithadevi.p.2016.it@rajalakshmi.edu.in"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "ECE Attendance sheet"
    body = ""
    msg.attach(MIMEText(body, 'plain')) 
    filename = "ECE.xlsx"
    attachment = open("/home/q8/Desktop/FINAL_YEAR_PROJECT/FaceRecognition/Result/ECE.xlsx", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "sunitha1998") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    print("mail sent successfully") 

def send_multiple_mail():
    send_mail_it()
    send_mail_cse()
    send_mail_ece()

#send_multiple_mail()