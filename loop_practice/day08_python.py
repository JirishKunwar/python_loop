import random
secret = random.randint(1,11)
guess=3
print("Guess the number(1,11)")
for i in range(0,3):
    a=int(input(f"guess left {i+1}/3 :"))
    if a == secret :
        print("win!")
        break
    elif a < secret:
        print("number is low ")
    else:
        print("number is hig")

else:
    print(f"you fail to geuess the number .and secret number is {secret}")