import constant

# Add string with single or double code [starting with ''' and end with ''']
str = '''Python's course  for beginners'''

# get string length
print(str.__len__())

# get a string from length
print(str[5])

# get substring from a string
print(str[0:5])
print(str[1:-1])

# Formatting text
f_name = "Amaresh"
l_name = 'Adak'
msg = f'{f_name} {l_name}'
print(msg)

# string convert upper case & lower case
print(str.upper())
print(str.lower())

# Title string
un_title_str = 'mY naME IS AmArESh AdAk'
print(un_title_str.title())

# Find string index from a string
print(str.find("co"))  # case sensitive & if return -1 then no string found

# Replace string
new_string = str.replace('P', 'S')
print(new_string)

# Check string if exists or not
print('Python' in str)
print('python' in str)
