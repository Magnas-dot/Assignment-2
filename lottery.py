import random
while(True):
    l1,l2,l3=[],[],[]
    sum1,sum2,sum3=0,0,0
    guess_num=int(input("Guess any number between 5 to 75:"))
    for i in range(5):
        num=random.randint(1,15)
        l1.append(num)
    sum1=sum(l1)
    for i in range(5):
        num=random.randint(1,15)
        l2.append(num)
    sum2=sum(l2)   
    for i in range(5):
        num=random.randint(1,15)
        l3.append(num)
    sum3=sum(l3)   
    # print(l1,l2,l3)
    # print(sum1,sum2,sum3)
    largest=sum1
    if(largest<sum2):
        largest=sum2
    elif(largest<sum3):
        largest=sum3
    print(largest)
    if(guess_num==largest):
        print("CONGRATULATIONS!! YOU HAVE WON THE LOTTERY")
    else:
        print("Better luck next time")
    
