 x=0
for i in range(5):
	print(" "*(5-i),end='')
	for j in range(i):
		x+=1
	if x%2:

		print(x,end=' ')
	print()
	