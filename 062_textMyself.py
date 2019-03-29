#!/usr/bin/env python3

# defined a function textmyself() that send text message passed to it as string

# preset values:

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+******'
twilioNumber = '+******'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(authToken,authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

