import datetime
import re

# 전화번호 
p = re.compile(r'^\d{2,3}-\d{3,4}-\d{4}$')

print(p.match('010-8756-2387'))
print(p.match('02-704-2387'))
print(p.match('054-371-3073'))

# MAC address
p = re.compile(r'^((\w){2}:){5}\w{2}$')
print(p.match('00:A0:50:3B:48:93'))
print(p.match('aa:df:ew:ew:23:76:43'))
#print('time' + datetime.datetime.now())
#print('time: ' + str(datetime.datetime.now()))