a=int(input("enter the maths marks"))
b=int(input("enter the english marks"))
c=int(input("enter the science marks"))
d=int(input("enter the punjabi marks"))
e=int(input("enter the hindi marks"))
xx=''
if a <40 or b <40 or c<40 or d<40 or e<40:
	if a<40:
		xx+=" Maths "
	if b<40:
		xx+=" English "
	if c<40:
		xx+=" Science "
	
	if d<40:
		xx+=" Punjabi "
	if e<40:
		xx+="Hindi"
	print("You are Fail in",xx)
else:	
	m=a+b+c+d+e
	marks=m/5
	print("your percentage",marks)
	if marks >90:
		print("marks a+ grade")
	elif marks>80 and marks<90:
		print("marks a grade")
	elif marks>70 and marks<80:
		print("marks b grade")
	elif marks>60 and marks<70:
		print("marks c grade")
	else:
		print("fail")

