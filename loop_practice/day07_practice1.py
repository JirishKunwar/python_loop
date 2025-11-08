import random
secret = random.randint(1,15)
print ("3 chances to guess (1-15)!")
for change in range (1,4):
    guess = int (input (f"change {change}/3:"))
    if guess == secret:
        print ("win")
        break
    elif guess < secret:
        print("too low !!!!")
    else:
        print("too high !!!")
else:
    print(f"game over? secret number is :{secret}")
         