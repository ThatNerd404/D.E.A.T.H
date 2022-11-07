# Notify.py - Module to send and check emails easier 
# aka adding a notification feature to programs

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email



class Notify:

    def __init__(self,recevier):
        self.recevier = recevier 

    def Send_Email(self, subject , message):
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('bcotterman06@gmail.com','dwmwyupcqtcrbzar')

        #? Use this to get message actually readable on the other end
        words = MIMEMultipart()
        words['From'] = 'bcotterman06@gmail.com'
        words['To'] = self.recevier
        words['Subject'] = subject 
        words.attach(MIMEText(message))

        mailserver.sendmail('bcotterman06@gmail.com', self.recevier , words.as_string())
        
    def Check_Mail(self):
        imaplib._MAXLINE = 100000


        mailserver = imaplib.IMAP4_SSL("imap.gmail.com")#? same as smtplib 
        mailserver.login('bcotterman06@gmail.com','dwmwyupcqtcrbzar')
        mailserver.select("Inbox")

        emale = []

        
        _, msgnums = mailserver.search(None, "UNSEEN",) #?Returns a only unseen emails
        for msgnum in msgnums[0].split():
            _, data = mailserver.fetch(msgnum,"(RFC822)")#? weird code means the whole message
            
            message = email.message_from_bytes(data[0][1])
            From = message.get("From")
            To = message.get("To")
            Date =  message.get("Date")
            Subject = message.get("Subject")
            if message.get("Content") == None: #? So I don't get nonetype
               Content = "No Content"
            else: 
                Content = message.get("Content")
                
            m = []
            
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    m += part.get_payload()
            msg = "".join(m)

            emale.append({'From':From,'To':To, 'Date':Date,'Subject':Subject,'Content':Content,"Message":msg}) #? a list of dicts so i can store data with keys and use indexing
        mailserver.close()
        mailserver.logout() #? Logout and close
        num_emails = len(emale) #? fixed num_emails 
        if num_emails == 0:
            emale = "No emails available"
        return emale , num_emails #? Returns a tuple when I call variables has to be in this order
        #!  when I call variables has to be in this order ^
        
        
        #?Will use imap to  check emails

#? Use for modules will only run if original file
#? |   is run not in the file which imports
#? |
#?\_/
if __name__ == '__main__': 
    #? How to use |
    #?           \_/
    Me = Notify('bcotterman06@gmail.com')#? sets where I want the message to go and creates notify object
    #Me.Send_Email('hi' , 'so hewwo')
    #Me.Send_Email("whats up " ," playa")
    #Me.Send_Email("hey" , "how you doin'")
    
    emale , num_emails  = Me.Check_Mail() #? changes tuple to useable values and bring values into use for main code 
    #? |
    #?\_/ Loop to print all new emails and all the stuff in it 
    if num_emails == 0:
        print(emale)
    else:
        for i in range(0,num_emails):
            print(f"{emale[i]['From']} {emale[i]['To']}\n{emale[i]['Date']}\n{emale[i]['Subject']}\n")
            i += 1
    

#? Create object and put paramenter in () dont use self.paramenter
#! YOU DUNCE!!! 
# need to figure out how to store multiple emails  
# need to be able to take all from, to , date and other data and store them in a dict and store all the from and to stuff in lists 
# its a project for tommorow don't stress about it this is supposed to be fun and if it isn't being fun just do  a solid 15 and then get off
# programming has been fun tho i do enjoy it I wouldn't stress so much if I didn't care
# instead of a key for from and to and so forth
