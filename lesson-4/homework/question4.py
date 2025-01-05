import random
i=0
l=['Y','YES', 'y','yes','ok']
s=random.randint(1,100)
while(i<=10):
    if(i<10):
        num=int(input("Guess the number: "))
        if(s>num):
            print("Too low!")
            i+=1
        elif(s<num):
            print("Too high!")
            i+=1
        else:
            print("You guessed it right!")
            i=0
            break
    else:
        other=input(f"You lost. The number was {s} Want to play again?")
        if(other in l):
            i=0
            s=random.randint(1,100)

