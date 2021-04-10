import random
a=random.randint(0,100)
p=9
print("Instructions: Your computer is hidding a number from you that lies between 1 to 100 and you have to guess that number within 9 trails")
print("Remaining Trials: ",p)
print("Guess the number that PC is hidding from you:")
x=int(input())
while(True):
    if p==1:
        if x==a:
            print("Congratulations!!! You have guessed the correct answer ;)")
            print("You have guessed the answer in 9 trials")
            break
        else:
            print("Game Over!!!")
            break
    if x>a:
        p = p - 1
        print("Remaining Trials: ", p)
        print("Guess a bit smaller number:")
        x = int(input())
        continue
    elif x<a:
        p = p - 1
        print("Remaining Trials: ", p)
        print("Guess a bit larger number:")
        x = int(input())
        continue
    elif x==a:
        print("Congratulations!!! You have guessed the correct answer ;)")
        p=p-1
        print("You have guessed the answer in just",9-p,"trials")
        break
    else:
        print("Invalid input")
        p = p - 1
        print("Remaining Trials: ", p)
        continue
