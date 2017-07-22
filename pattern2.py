x=int(input())
y=x
if (x%2==0):
	x=x/2
elif (x%2!=0):
	x=(x/2)+1
	x=int(x)
a=1
j=x
for i in range(0,x):
	j=x
	while(j>0):
		print(" ",end=" ")
		j=j-1
	b=a
	while (b>0):
		print("*",end=" ")
		b=b-1
	a=a+2
	x=x-1
	print("\n")