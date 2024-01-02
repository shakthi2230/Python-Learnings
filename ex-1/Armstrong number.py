import math
#Armstrong number 
def getdigitcount(n):
    t=n
    l=str(n)
    c=len(l)
    r=0
    for i in l:
        r+=int(i)**c

    return r

n=156

if getdigitcount(n)==n:
    print("True")
else:
    print("False")


#short code of chatgpr
# def is_armstrong_number(n):
#     return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

# n = 156
# print("True" if is_armstrong_number(n) else "False")
