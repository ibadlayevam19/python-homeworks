import random
scoreC=0
scoreU=0
l=['rock', 'paper', 'scissors']
while( scoreC<5 and scoreU<5):
    s=random.choice(l)
    i=input("Your choice: ").lower()
    print(f'Mine is {s}')
    if((s=='rock' and i=='scissors') or (s=='paper' and i=='rock') or (s=='scissors' and i=='paper')):
        scoreC+=1
        print('I won this round!')
    elif(s==i):
        print('Draw')
    else:
        scoreU+=1
        print('You won this round!')
print(f'Me: {scoreC} and You: {scoreU}')
if(scoreC==5):
    print('Winner is Me!')
else:
    print('Winner is you!')