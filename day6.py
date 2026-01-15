# PRIME OR NOT
def prime(n):
    if n <=1:
        return False
    elif n ==2:
        return True
    elif n ==3:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
        return True
    

# PALIDROME OR NOT
def pali(n):
    n=n.lower()
    return n ==n[::-1]
print(pali('pratik'))


# REVERSED THE STRING WITHOUT SLICING
def revese(n):
    rev=""
    for ch in n:
        rev=ch + rev
    return rev

# print(revese('pratik'))

# FREQUENCY COUNTER
def freq(n):
    result={}
    for items in n:
        if items in result:
           result[items]+=1
        else:
            result[items]=1
    return result

# print(freq([3232,323,23,32,3,33,32,32,32,33,233,23,2232,32,2,2,32]))

# EVEN NUMBER  COUNTER
def even(numbers):
    count=0
    for num in numbers:
        if num % 2==0:
            count+=1
    return count
# print(even([2,3,2,3,2,4,5,6,5,44,8,10]))

# FIBONACCI SERIES
def fibo(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b

# fibo(13)


# GCD(greates common difference)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
        print(a)

# gcd(32,30)
