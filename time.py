x=int(input('time in seconds '))
a=x//86400
print('DAYS: ')
print(a)
y=a%86400
b=y//3600
print('HOURS: ')
print(b)
z=b%3600
c=z//60
print('MINUTES: ')
print(c)
w=c%60
print('SECONDS ')
print(w)
