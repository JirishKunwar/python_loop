import random
def boy():
    
    secret = random.randint(1,10)
    a = 3
    print("hello sir you got only 3 guess ")
    for i in range (1,a+1):
        b= int (input(f" guess left {i}/3.Enter a number :"))
        if b == secret :
            print("win!")
        elif b < secret:
            print("number is low")
        else:
            print("number is high")
    else:
        print(f"you fail to guess number . secret number is {secret}")
boy()