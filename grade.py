a=int(input("Enter Maths Marks"))
b=int(input("Enter Sci Marks"))
c=int(input("Enter Punja Marks"))
m = a+b+c
mark=m/3
print("your percentage is::::",mark)
if mark > 90 :
	print("mark a+ grade")
elif mark > 80 and mark< 90 :
	print ("mark a grade ")
elif mark > 70 and mark< 80 :
	print ("mark b grade")
elif mark > 60 and mark< 70 :
	print ("mark c grade")
else:
	print ("fail")
		