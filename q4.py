s="a+aa+aaa+aaaa"
n=0
for i in s:
	c=0
	if i=="+":
		continue
	if i=="a":
		c+=1
	n=n+c
print(n)
