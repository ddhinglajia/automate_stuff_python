def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi Moshi is a phone number:')
print(isPhoneNumber('Moshi Moshi'))

print ('\n\n')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done\n\n')

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found :' + mo.group())

# matching multiple format of phone number

message1 = ('list of numbers  415.555.4242 ,  (415) 555-4242, 415-555-4242')


#phoneMulRegex = re.compile(r'''(
                           #(/d{3}|\(\d{3}))?
                           #(\s|-|\.)?
                           #\d{3}
                           #(\s|-|\.)
                           #\d{4}
                           #(\s*(ext|x|ext.)\s*d{2,5})?
                           #)''', re.VERBOSE)
print('\n\n\n')

phoneMulRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? 
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''', re.VERBOSE)



phoneMulRegex.findall(message1)
#print(mo.group(1))
#print('Phone number found :' + mo.group())
