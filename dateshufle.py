l=['10-02-2019','11-02-2019']
f=[]
for i in l:
	z=[0,0,0]
	y=i.split('-')
	z[0]=y[2]
	z[1]=y[1]
	z[2]=y[0]
	f.append("/".join(z))
print(f)
