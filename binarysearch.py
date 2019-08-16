l=[1,2,35,57,87,54,33,56]
l.sort()
start=0
end=len(l)-1
while(start<end):
	mid=(start+end)//2
	if l[mid]==item:
	print("your item is on ",mid)
	break
elifl[mid]>item:
	end=mid-1
else:
start=mid+1