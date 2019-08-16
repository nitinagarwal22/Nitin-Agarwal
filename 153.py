n=int(input("Enter Any number"))
yy=n
sum=0
while (n>0):
	x=n%10
	sum=sum+x**3
	n=n//10
print(sum)
if yy==sum:
	print("Armstrong")
else:
	print("Not Armstrong")