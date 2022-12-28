# Regular Expressions, known as regex is a sequence of characters that forms a search pattern. It is a useful way to search for something specific
# e.g. you needed to obtain all telephone numbers in a 1000 page document
# Regex can be used to check if a string contains a specified string e.g telephone number, phrase, name etc

# regex comes from one of the built in modules, import re must be input to retrieve regex

import re

# /d stands for digit character
# e.g. UK telephone numbers have a structure of 5 digits, followed by 6 digits. \d\d\d\d\d - \d\d\d\d\d\d
# You can go further by adding a number in braces. \d{5} - \d{6} is the same as above - \d\d\d\d\d - \d\d\d\d\d\d

phoneNumRegex = re.compile(
    r'\d\d\d-\d\d\d-\d\d\d\d')  # the regex you want to search for is passed into re.compile and then as a variable
# phoneNumRegex now comtains the regex object

mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow. 415 555 9999 is my office ')
# the .search() method is used to search for the contents of what you need looking into
# the .search() method will return none if there are no matches of the regex pattern

# if a pattern is found. Using .group() produces all instances of the pattern
print('Phone number found: ' + mo.group())

# GROUPING WITH PARENTHESES

# you can go further by separating your regex with parentheses. For example (\d\d\d\d\d) - (\d\d\d\d\d\d)
# why is it useful? for example with UK telephones, you can identify geographical location via the first 5 digits

us_num = re.compile(r'(\d\d\d\d\d)-(\d\d\d\d\d\d)')
mo = us_num.search('My number is 01442-292284.')
print(mo.group(1))  # >>>01442 this tells us the call comes from Hemel Hempstead
print(mo.group(2))  # >>>292284
print(mo.group())  # >>>01442292284
print(mo.groups())  # >>>('01442', '292284')

# in case there is a parentheses within the content of what you're searching, you can use \( \) to cancel them out
# if you want to detect any special characters !@£$%^&*() as part of your regex, you need to use the backslash \

us_num = re.compile(r'(\(\d\d\d\d\d\)) (\d\d\d\d\d\d)')
mo = us_num.search('My number is (01442) 292284.')
print(mo.group())  # >>>(01442) 292284

# MATCHING MULTIPLE GROUPS
# The pipe character | i used to match multiple expressions

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batcopter lost a wheel and the Batmobile was destroyed')
print(mo.group())
print(mo.group(1))

# OPTIONAL MATCHING
# Optional matching can be done by placing a ? after the group you wish to optionally match

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# FIND ALL()
# while search() will return the first matched object. findall() will return all matched objects. using findall() doesnt require groups() method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # without groups in regrex
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))  # >>> ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # with grouped regex
print(phoneNumRegex.findall(
    'Cell: 415-555-9999 Work: 212-555-0000'))  # >>> [('415', '555', '9999'), ('212', '555', '0000')]

# SPECIAL CHARACTERS
# ? Optional matching - group preceding ?, if present in string, produce match, otherwise carry on with regex search. Is not required to appear in matched string
# * Zero or more -  group that precedes * can occur any number of times or it can be absent and will still produce match. Is not required to appear in matched string
# + One or more - group that precedes + must appear at least once or more in matched string
# {} Specific repetitions - e.g. (r'(Ha){3}') == 'HaHaHa' / {3, } == three or more repetitions / {3,5} == 3 to 5 repetitions / {,5} == zero to five repetitions
# .* Everything and anything - e.g. you want to match everything and anything that comes after 'First name:'

# \d - any numeric digit from 0 to 9
# \w - any letter
# \s - any space

# USEFUL - you can define your own character class by square brackets (r'[aeiouAEIOU]') says search for following upper and lower case letters
# hyphen (-) uses range e.g. [a-zA-Z0-9] says search for all lower and upper case characters from a to z and numbers from 0 to 9
# ^ - negative character class (r'[^aeiouAEIOU]') means match characters not in regex

# Note - using square brackets means you do not need to use reg ex expressions. You do not need to escape special characters e.g. \? \( \)
