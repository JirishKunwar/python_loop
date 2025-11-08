import random
secret = random.randint(1,10)
print("Guess number (1 - 10)")
a = int (input ("enter a number :"))
if a == secret:
    print("You win")
else:
    print (f"you loss{secret}" )