#smpt-server
import smtplib

#plain text email or HTMl Email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#credentials
username, password = '*****@gmail.com', 'xxxxxxxx'

def send_email(text=None, subject=None, from_addr='Dharani Py <dharani.python@gmail.com>', to_addrs=None, html=None):
   
    #To_address type should be list
    assert isinstance(to_addrs, list)

    email = MIMEMultipart('alternative')
    email['From'] = from_addr
    email['To'] = ", ".join(to_addrs)
    email['Subject'] = subject

    # Send plain text email
    if text != None:
        plain_text_email = MIMEText(text, 'plain')
        email.attach(plain_text_email)
    
    # send HTML email
    if html != None:
        html_email = MIMEText(html, 'html')
        email.attach(html_email)

    mainEmailTemplate = email.as_string()

    #login into SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com',port='587')
    server.ehlo() #Identify yourself to an ESMTP server using EHLO
    server.starttls() #upgrade it to a secure connection
    server.login(username, password) #login
    server.sendmail(from_addr, to_addrs, mainEmailTemplate) #sending dynamic email
    server.quit()

# Trigger the main function here
htmlTemplate = '<h1>This is my HTML template</h1>'
send_email(subject='Different Subject - Python3', to_addrs=['****@gmail.com', '****@gmail.com'], html=htmlTemplate)