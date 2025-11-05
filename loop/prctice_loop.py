b = int ( input ("Enter the number :"))
for i in range (2 , b):
    if  b % i == 0 :
        print ("not a prime number ")
        break
else :
    print ("prime number ")