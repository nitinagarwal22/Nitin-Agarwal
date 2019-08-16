x= "i love python python i love "
f='python'
pos=-1
y=0
while True:
	pos=x.find(f,pos+1,len(x))
	if pos==-1:
		break
	print("item found at",pos)
	y=1
if y==0:
	print ("search item not found") 