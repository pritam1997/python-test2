print("""Please enter debit for (d) &
		withdrawl for (w)
 """)


def fun():
	c=input("Debit or Withdrawl : ")
	b=0
	if c.lower()=='d':
		d=int(input("Enter debit amount: "))
	# if d>0:
		b=b+d

	elif c.lower()=='w':
		w=int(input("Enter withdrawl amount: "))
		b=b-w
	else:
		print("Please enter correctly!!!!!")

for x in range(100):
	fun()		
	q=input("To end type {end or END}")
	if q.lower()=="end":
		break

print(f"Your bank balance is : {b}")

