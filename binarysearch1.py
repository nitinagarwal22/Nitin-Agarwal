l=[2,4,6,8,11,13,17,20,22]
start=0
item=int(input("enter any number"))
end=len(l)-1
while start<=end:
	mid=(start+end)//2
	if item==l[mid]:
		print(mid)
		break
	else:
		if item<l[mid]:
			end=mid-1
		else:
			start=mid+1