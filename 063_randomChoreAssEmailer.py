#!/usr/bin/env python3

# pratice : program to randomly assign tasks by emails


import random, smtplib, sys

# chores, ppl, and their emails

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

emailList = {
    "a": "a@gmail.com",
    "b": "b@gmail.com",
    "c": "c@gmail.com",
    "d": "d@gmail.com"
    }


# log in to email account

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
myemail= 'my_email_address@gmail.com'
smtpObj.login(myemail, sys.argv[1])


# random chore assignement

def randomChore(list):
    choresSet = set()
    while len(choresSet) != len(list):
        choresSet.add(random.choice(list))
    return choresSet

results = []

for person in emailList:
    results[person] = list(randomChore(chores))

for person in emailList:
    duties = [person]
    duties.append(", Your duties for the next {0} weeks:".format(len(chores)))
    for i in range(len(results[person])):
        duties.append("\nWeek {0}: {1}".format(i+1, results[person][i]))
    mailText = "vbhq_470wpfn@interia.pl\r\nSubject: Duties for 4 weeks.\r\nBody: {0}\n".format(" ".join(duties))
    smtpObj.sendmail(myemail, emailList[person], mailText)
    print(mailText)

smtpObj.quit()