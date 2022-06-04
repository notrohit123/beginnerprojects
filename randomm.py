import random
def guess(x):
     secret=random.randint(1,x)
     guess=0
     while guess!=secret:
         guess=int(input(f"enter the number bw 1 and {x}"))
         if guess>secret:
             print("you have entered a large number")
         elif guess<secret:
            print("you have entered small number")
         elif guess==secret:
             print("found the number :))")
             break
def computer(y):
    low=1
    high=y
    feedback=""
    while feedback!="c":
        guess=random.randint(low,high)
        print(f"computer guesses is {guess}")
        feedback=input("enter the feedback H,L,C").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
        elif feedback=="c":
            print("computer has guessed it right :))")
            break
computer(20)                
        