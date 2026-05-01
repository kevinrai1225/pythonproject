patient='rahUL DAHal'
print(patient.title())

pwd='Pass@123'
print(pwd.lower())

movie='spider-man no way home'
print(movie.title())

text='annual sports day'
print(text.upper())

text='hELLO wORLD'
print(text.swapcase())

msg='System error detected, error code 404'
print(msg.find('error'))

email='test@gmail.com'
print(email.endswith('@gmail.com'))

msg='Get free stuff, free gifts and free coupons now!'
print(msg.count('free'))

url='https://example.com'
print(url.startswith('https'))

text='I know Python well'
print('Python' in text)

msg='Transaction FAILED due to low balance'
print(msg.index('FAILED'))

file='budget_report.pdf'
print(file.endswith('.pdf'))

num='+977-9841123111'
print(num.startswith('+977'))

url='https://www.moha.gov.np/'
print('.gov.np' in url)

text='  Great service!  '
print(text.strip())

msg='I hate this, hate it completely'
print(msg.replace('hate','*****'))

file='///student_records.pdf'
print(file.lstrip('/'))

price='Price: $120.33   '
print(price.rstrip().replace('Price: $',''))

num='+977 984-123-4567'
print(num.replace('-','').replace(' ',''))

data='Aarav,22,Kathmandu,Computer Science'
print('\n'.join(data.split(',')))

tags='Python, Coding, Nepal, Tech'
print('#'+' #'.join(tags.split(', ')))

names='Ram, Shyam, Hari, Sita'
print(len(names.split(', ')))

words=['The','flight','departs','at','6AM']
print(' '.join(words))

age='25ab'
print(age.isdigit())

user='Kevin123'
print(user.isalnum())

name='Ram'
print(name.isalpha())

pin='ASDF'
print(pin.isupper())

field='   '
print(field.isspace())