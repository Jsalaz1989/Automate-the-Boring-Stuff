#! python3
# textMyself.py - Defines the textmyself() function that texts a message passed to it as a string.

# Preset values:
accountSID = 'AC8a0c8ab114fcd6debde5c25b3cdd28a9'
authToken = 'e1b1797832b5a50bd8b8d04a02df4936'
twilioNumber = '+12015716627'
myNumber = '+34605725691'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)