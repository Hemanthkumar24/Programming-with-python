#tic tac toe
a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print("....|...|....")
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print("....|...|....")
	print('|',a[6],'|',a[7],'|',a[8],'|')



p1=True
while(True):
	printboard()
	if p1:
		p=input("p01 choose your place:")
		if p in a:
			a[int(p)-1]='X'
			p1=not p1
	else:
		p=input("p02 choose your place:")
		if p in a:
			a[int(p)-1]='O'
			p1=not p1
	for i in(0,3,6):
		if(a[i]==a[i+1] and a[i+2]):
			print("Game over")
			if(a[i]=='X'):
				print("player 1 has won")
			else:
				print("player 2 has won ")	
			printboard()
			exit()
	if(a[0]==a[4] and a[0]==a[8]):
		print("Game over")
		if(a[0]=='X'):
				print("player 1 has won")
		else:
				print("player 2 has won ")
		printboard()
		exit()
	if(a[2]==a[4] and a[2]==a[6]):
		print("Game over")
		if(a[2]=='X'):
				print("player 1 has won")
		else:
				print("player 2 has won ")
		printboard()
		exit()
	else:
		print("you have entered an invalid position")

		
