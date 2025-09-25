'''
2 = snake
1 = water
0 = gun
'''
import random
computer = random.choice([2,1,0])
youstr = input("enter your choice: ")
youdict = {"s":2,"w":1,"g":0}
yourevesedict = {2:"s",1:"w",0:"g"}

you = youdict[youstr]

print(f"you choose {yourevesedict[you]}\ncomputer choose {yourevesedict[computer]}")

if (computer == you):
	print("It's a tie")
    
else:
	if(computer ==2 and you ==1):
		print("you loss")
	elif(computer ==2 and you ==0):
		print("you win")
	elif(computer ==1 and you ==2):
		print("you loss")
	elif(computer ==1 and you ==0):
		print("you win")
	elif(computer ==0 and you ==2):
		print("you loss")
	elif(computer ==0 and you ==1):
		print("you win")
	else:
		print("something wrong")
			
							    