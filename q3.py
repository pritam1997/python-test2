s=input("Entre sentence : ")
up=0
lw=0
for i in s:
	if i==" ":
		continue
	if i==i.upper():
		up+=1
	elif i==i.lower():
		lw+=1
print(f"Upper letter is {up} and lower letter is {lw}")