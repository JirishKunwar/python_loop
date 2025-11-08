def factrioon(n):
    if n == 0 or n == 1:
        return 1
    return n * factrioon(n-1)
n = int (input ("enter a factriol number "))
print(f"the number of this factroil is :{factrioon(n)}")