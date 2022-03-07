import random
myRandom = random.randrange(1,11)
k=1
correct = False
print("Welcome to Guess the number.")
print("This game will ramdom number 1 to 10.")
print("You only have 3 chances to guess the number.")
while True:
    number = int(input("Enter your answer =====>  "))
    correct = (number == myRandom)
    if not correct:
        if number>myRandom:
            print("It's greater.")
        if number<myRandom:
            print("It's lower.")
    if correct :
        print("You Win!!")
        break
    if number < 0 or k == 3 or number > myRandom:
        break
    k+=1
if not correct:
    print("Try again.")
    print("The answer is ",myRandom)






