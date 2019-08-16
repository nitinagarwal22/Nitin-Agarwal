# I/P A2B3  O/P ACBE

X= "A2B3F5"
Y=''
o=''
p=''

for i in X:
	if i.isalpha():
		o+=i
		p=i
	else:
		o=o+chr(ord(p)+int(i))
print(o)
	