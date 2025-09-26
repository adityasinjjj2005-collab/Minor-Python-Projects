import random

target = random.randint(1,100)

while True:
    userchoice = int(input("Guess the target :"))
    if(userchoice == target):
        print("Success : correct guess")
    elif(userchoice < target):
        print("your number was too small. take a bigger guess..")
    else:
        print("your number is too big.take a small guess")     


print("....game over...")           
