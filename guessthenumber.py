import random
print("aaksh you have to guess the number")
guess=random.randint(1,100)
guesses=0
while guesses<7:
    gue=int(input("ente the guess"))
    guesses+=1
    if gue<guess:
        print("less")
    elif gue>guess:
        print("more")
    elif gue==guess:
        break
    
if gue==guess:
    print("found")
else:
    print("not found sorry")
    print("try again")
    
