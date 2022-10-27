s = 'abfcdefghf'
print(s)
print(len(s))
print(s.count('f'))
print(s.find('fc'))
print(s[2:5])
print(s[2:])
# first 2 characters
print(s[:2])
# last 2 characters
print(s[-2:])
print('-------------')
s2 = 'abc\ndef\tfałąąśććęężgaga\tgwrgw'
print(s2)

print(ord('a'))
print(ord('A'))

s3 = '  agsdbaqb asbsa '
# Getting rid of spaces in front and back
print(s3.strip())
s4 = '66'
s5 = '6363.2363'
i4 = int(s4)
f5 = float(s5)
c = i4 + f5
print(type(c))
print(c)

s8 = 'absdavbsd;ggsgwr;45636;2526237;727'
print(s8.split(';'))
print(s8.split(';')[2])
