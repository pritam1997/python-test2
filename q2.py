s=input("Enter sentence :")
n=""
count=0
alp=0
for i in range(len(s)):
	for n in range(11):
		if s[i]==n:
			count+=1
			print(count)
		else:
			n+=1
print(n,count)