#using functions,rock papper scissor
import random
A={1:'r',2:'p',3:'s'}
while True:
	yc=input("Your choice:r/p/s:")
	cc=A[random.randint(1,3)]
	print("Computer gave:",cc)


	if(cc==yc):
		print("tie")
	elif(cc=='r'and yc=='s'or cc=='p'and yc=='r'or cc=='s'and yc=='p'):
		print("computer won")
	else:
		print("you won")








