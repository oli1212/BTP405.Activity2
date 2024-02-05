import math

def getPrimeNumber(input):
    numList = []
    for num in range(2,input):
        if isPrime(num):
            numList.append(num)

    return numList

def isPrime(num):
    
    if num <= 1:
        return False
    
    # int() rounds down float nums
    # 1 is added to round up the num and also to allow the for loop to iterate the square root number
    # range 2,2 is empty range, nothing inbetween
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

primeNums = getPrimeNumber(50)

print(primeNums)