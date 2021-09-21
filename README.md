# Recurring-Gmail-Sender
This year I am coordinating a local volunteer project called Biocycle. There isn't any food waste collection service provided by the council in Southampton, so instead this project collects food waste from houses by bicycle and uses it for compost. We send out an email the night before reminding each house on the days route that their collection will happen tomorrow. Previously this was done manually so I decided to apply some of my programming knoweledge to automate this! There were commercial options but they required a monthly subscription!!

## The Project
The email addresses for each day are contained in an excel spreadsheet. Saving each page as a CSV, this data is then imported into the script. Depending on the day the script then decides which recipients are required for todays sending and then on running of the script will send the email to these addresses. The message is contained within a text document within the folder. For some extra functionality there is an option to send emails to all addresses, which is very useful when sending out updates. This script has been loaded onto a raspberry pi which acts as an email server and then an email is sent every night at 18:30 using CRON. Since the script auto updates there is no need to have 6 different scripts for the different email days.

To get this to work you first need to set up your Gmail account:

## Setting up GMail account to work with SMTPLIB:
Firstly you have to ensure the Gmail account is allowing access to less secure apps. A good link how to do that is below:

[Allowing less secure apps to access your account](https://support.google.com/accounts/answer/6010255)

This should solve the authentication email. For this use I didn't want to chagne the main Biocycle account to work with this due to sensitive information, so instead I created a new empty Gmail to act as an email sender. This is one of the unfortunate drawbacks with this method!

## Requirements to run:
* A Gmail account which enables third party applications

## Libraries:
* pandas
* smtplib
* itertools
* email.message

## Next Steps:
* Create an app that users will sign up to and automatically updates the script with the correct users for each day, will get rid of the need to manually update the CSV files with every new user of the project.
