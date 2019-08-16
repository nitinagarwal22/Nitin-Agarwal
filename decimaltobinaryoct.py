n=int(input("Enter number"))
s=''
while(n>0):
	x=int(n%8)
	s+=str(x)
	n=n//8
print(s[::-1])
