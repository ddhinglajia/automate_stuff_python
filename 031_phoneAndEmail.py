# search phone numbers and emails from text on clipboard

import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)?
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''' , re.VERBOSE)

emailRegex = re.compile(r'''(
    \w +
    (@) +
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4}){
    )''', r.VERBOSE)

clipText = str(pyperclip.paste())

mo = []

for groups in phoneRegex.findall(clipText):
    phoneNums = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phoneNums += 'x' + groups[8]
    mo.append(phoneNums)
    
for groups in emailRegex.findall(clipText):
    mo.append(groups[0])


if len(mo) > 0:
    pyperclip.copy('\n'.join(mo))
    print('Copied to clipboard:')
    print('\n' .join(matches))
else:
    print('No phone numbers or email addresses found.') 
    
    
#change
