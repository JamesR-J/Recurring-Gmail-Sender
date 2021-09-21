import smtplib
import itertools

import pandas as pd

from email.message import EmailMessage
from datetime import datetime


with open("./message.txt") as fp: #opens the plain text file which is the sent email content
    msg = EmailMessage()
    msg.set_content(fp.read())

SMTP_SERVER = 'smtp.gmail.com' #email server (don't change!)
SMTP_PORT = 587 #server port (don't change!)
GMAIL_USERNAME = '<your_gmail_account>' #change this to match your gmail account
GMAIL_PASSWORD = '<your_gmail_password>' #change this to match your gmail password


class Emailer:
    def __init__(self, Recip_type='auto'):
        days = ['2', '3', '4', '5', '6', '7', '1']
        #day_number = 5    ###THIS IS TO ENABLE MAIN TEST WITHOUT SENDING TO 
        #ANY ADDRESSES BUT MINE###
        day_number = datetime.today().isoweekday()
        day = days[day_number - 1] #this means that it sends the email the 
        #night before the collection date on the CSV
        dctRecipPaths = {}
        dctRecipPaths['1'] = "./Email Addresses/2021 houses continuing - MONDAY.csv"
        dctRecipPaths['2'] = "./Email Addresses/2021 houses continuing - TUESDAY.csv"
        dctRecipPaths['3'] = "./Email Addresses/2021 houses continuing - WEDNESDAY.csv"
        dctRecipPaths['4'] = "./Email Addresses/2021 houses continuing - THURSDAY.csv"
        dctRecipPaths['5'] = "./Email Addresses/2021 houses continuing - FRIDAY.csv"
        dctRecipPaths['6'] = "./Email Addresses/TEST.csv" #this contains
        #my personal email to check email receipts and to ensure they were BCC
        dctRecipPaths['7'] = "./Email Addresses/2021 houses continuing - SUNDAY.csv"
        
        if Recip_type == 'auto':
            #the default setting, sends emails on the correct day for the emails
            self.recipients = self.read_email_recipients(dctRecipPaths[day])
        elif Recip_type == 'All':
            #adds all the emails together to enable an email to be sent to everyone
            self.recipients = [self.read_email_recipients(dctRecipPaths[x]) for x in dctRecipPaths]
            self.recipients = list(itertools.chain.from_iterable(self.recipients))
        elif Recip_type == 'Test':
            #combines the addresses with the test addresses for each day
            if day != '6':
                self.recipients = self.read_email_recipients(dctRecipPaths[day])
                (dctRecipPaths[day]) + self.read_email_recipients(dctRecipPaths['6'])
            elif day == '6':
                self.recipients = self.read_email_recipients(dctRecipPaths[day])
            
    
    
    def sendmail(self, msg):
        
        msg['Subject'] = "Biocycle Collection Tomorrow"
        msg['From'] = "<your_gmail_account>"
        #msg['To'] = TO
        #msg['Cc'] = CC
        msg['Bcc'] = self.recipients #i only needed BCC for this use
        
        
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD) #logs into your gmail
                  
        session.send_message(msg) #sends the message
        session.quit

        
    def read_email_recipients(self, file_path):

        df = pd.read_csv(file_path)
        df.dropna(subset = ['Email'], inplace=True)
        
        if int((df.columns[-1])) == len(df['Email']):
            print("Email Recipients and Expected Values Match")
            recipients = df['Email'].tolist()
            #for ease of mind I added a header to the csv which totalled the 
            #no of email recipients for that day, if this value matches the 
            #length of the email column then it works out fine
        else:
            raise ValueError("Email Recipients Don't Match Value Expected")
            #otherwise it raises this error
        
        return recipients
    

if __name__ == "__main__":
    sender = Emailer('Test')
    sender.sendmail(msg)
