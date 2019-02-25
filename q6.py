p=input("Enter password : ")

small=['a','b','c','d','e','f','g','h','i',\
		'j','k','l','m','n','o','p',\
		'q','r','s','t','u','v','w','x','y','z']

ad=small.copy()

l=[]

for i in ad:
	l.append(i.upper())

ch=['#','$','@']

no=[]
for i in range(0,10):
	no.append(i)



password=""

for x in p:
	if x is small or l or ch or no:
		if len(p)<6 and len(p)>12:
			print("Your password minimum length is 6 and maximum lenght is 12")
		else:
			password=password+x


if password is small[::] and password[::] is ch[::] and password is no[::] and password is l[::]:
	print(password)
else:
	print("""password must contain :
1. At least 1 letter between [a-z] 
2. At least 1 letter between [A-Z] 
3. At least 1 letter between [0-9] 
4. At least 1 character from [$#@] 
		""")