x=input('no. ')
l=len(x)
sum=0
for j in range(0,len(x)):
	sum+=int(x[j])**l
if int(x)==sum:
	print('Armstrong no.')
else:
	print('not armstrong no.')
