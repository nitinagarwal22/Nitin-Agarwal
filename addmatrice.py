r=int(input("enter no. of rows"))
c=int(input("enter no.of colums"))
l1=[]
l2=[]
out=[]
print("enter elements for first matrix")
for i in range(r):
	l1.apend([])
	for j in range(c):
		x=int(input("enter element :"))
		l1[i].append(x)
print("list1=",l1)
print("list2=",l2)
for i in range(r):
	out.append([])
	for j in range(c):
	   x=int(input("enter element :"))
	out[i].append(0)
print(out)
print("sum of both matrix")
for i in range(r):
	for j in range(c):
		out[i][j]=l1[i][j]+l2[i][j]
print("sum=",out)