#A5B7D9 O/P AAAAABBBBBB.....

x1="A5B7D9"
x=''
p=''
d=0
for i in x1:
	if i.isalpha():
		p=i
	else:
		d=int(i)
		x+=(p*d)
print("----",x)
	