x=int(input())

for i in range(0,x,1):
	a=x
	while(a>i+1):
		print(" ",end=" ") 
		a=a-1
	while(a>0):
		print (a,end=" ")
		a=a-1
	print("\n")