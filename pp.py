xyz=[]
l=int(input("Enter lower limit"))
u=int(input("Enter upper limit"))
for i in range(l,u+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		xyz.append(i)
print(xyz)

for i in range(len(xyz)):
	for j in range(i+1):
		print(xyz[i],end=' ')
	print()





# xyz=[]
# l=int(input("enter the lower limit"))
# u=int(input("enter the uper limit"))
# for i in range (l,u+1):
	# for j in range(2,i):
		# if i%j==0:
			# break
		# else:
			# xyz.append(i)
# print(xyz)
"""
for i in range (xyz):
	for j in range (i):
		
		print("*",end='')
	print()
	"""