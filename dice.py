#write a program to print random numbers
import random
while True:
	i=input("enter'r' to roll the dice,'q' to quit")
	if (i=='r'):
		print(random.randint(1,6))
	elif(i=='q'):
		print("END")
		break
	else:
		print("give either'r' or 'q'")


