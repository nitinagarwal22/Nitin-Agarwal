l=[10,20,30,40,50]
key=int(input("enter the element u want to search:"))
if key in l:
		print("element found at loc:",l.index(key))
else:
		print("element not in list")
