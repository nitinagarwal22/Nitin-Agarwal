import time
import os
u='123'
p='321'
u=input("enter the username::")
c=0
if u == '123':
	p=input("enter the password::")
	while(p!='321'):
		print("more than two attempts")
		for i in range (10,0,-1):
			print("come back after ",i,"secs...")
			time.sleep(1)
			os.system('cls')
		break
	else:
		print("wellcome to my screen")
else:
	print ("username invalid")