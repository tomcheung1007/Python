import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{5}|\(\d{5}\))?             #area code - match ddddd or (ddddd)
    (\s|-|\.)?                     #separator - or . (optional)
    (\d{3})                        #first 3 digits
    (\s|-|\.)                      #separator
    (\d{3})                        #last 3 digits
    (\s*(ext|x|ext.)\s*(\d{2.5}))? #extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       #@ symbol
    [a-zA-z0-9.-]+          #domain name e.g. gmail yahoo
    (\.[a-zA-z]{2,4})       #dot something e.g. .com co.uk
    )''', re.VERBOSE)

#Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
      phone_num += ' x' + groups[8]
      matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#TO DO: copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
