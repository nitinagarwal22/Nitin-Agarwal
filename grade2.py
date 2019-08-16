a=int(input("enter the maths mark"))
b=int(input("enter the english marks"))
c=int(input("enter the science marks"))
d=int(input("enter the punjabi marks"))
e=int(input("enter the hindi marks"))
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
else marks<60:
	print("marks fail")
