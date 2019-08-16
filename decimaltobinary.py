n=int(input("Enter number"))
s=''
while(n>0):
	x=n%2
	s+=str(x)
	n=n//2
print(s[::-1])


n=int(input("Enter number"))
s=0
i=1
while(n>0):
	x=n%8
	s=s+x*i
	n=n//8
	i=i*10
	print("I am I::",i)
print(s)


