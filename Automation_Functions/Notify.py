# Notify.py - Module to send and check emails easier 
# aka adding a notification feature to programs

import imaplib

import smtplib

import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notify:
    def __init__(self):
        pass

    def Send_Email(self, recevier, subject , message):
        
        #? Logging in and starting email service
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('bcotterman06@gmail.com','dwmwyupcqtcrbzar')

        #? Adding information to email in format suitable for gmail 
        words = MIMEMultipart()
        words['From'] = 'bcotterman06@gmail.com'
        words['To'] = recevier
        words['Subject'] = subject 
        words.attach(MIMEText(message))

        mailserver.sendmail('bcotterman06@gmail.com', recevier , words.as_string())
        
    def Fetch_Inbox(self):
        imaplib._MAXLINE = 100000


        mailserver = imaplib.IMAP4_SSL("imap.gmail.com")
        mailserver.login('bcotterman06@gmail.com','dwmwyupcqtcrbzar')
        mailserver.select("Inbox")

        email_data = []
        
        #? Function will automatically mark emails with seen after searched
        _, msgnums = mailserver.search(None, "UNSEEN")
        
        for msgnum in msgnums[0].split():
            #? "RFC822" weird code means the whole message
            _, data = mailserver.fetch(msgnum,"(RFC822)")
            
            message = email.message_from_bytes(data[0][1])
            From = message.get("From")
            To = message.get("To")
            Date =  message.get("Date")
            Subject = message.get("Subject")
            
            #? Turns nonetype to a string to stop errors
            if message.get("Content") == None: 
               Content = "No Content"
            else: 
                Content = message.get("Content")
                
            m = []
            
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    m += part.get_payload()
            msg = "".join(m)

           
            email_data.append({'From':From,'To':To, 'Date':Date,'Subject':Subject,'Content':Content,"Message":msg}) #? a list of dicts so i can store data with keys and use indexing
        mailserver.close()
        mailserver.logout() #? Logout and close
        num_emails = len(email_data) 
        if num_emails == 0:
            email_data = "No emails available"
        
        #!  when I call variables has to be in this order 
        return email_data , num_emails 
        
        
if __name__ == '__main__': 
    #? sets where I want the message to go and creates notify object
    Me = Notify()
    #EX: Notify.Send_Email(Recevier, Subject , Message) 
    
    #? changes tuple to useable values and bring values into use for main code 
    email_data , num_emails  = Me.Fetch_Inbox() 
    #? |
    #?\_/ Loop to print all new emails and all the stuff in it 
    if num_emails == 0:
        print(email_data)
    else:
        for i in range(0,num_emails):
            print(f"{email_data[i]['From']} {email_data[i]['To']}\n{email_data[i]['Date']}\n{email_data[i]['Subject']}\n")
            i += 1
    

