def SumOfDigits(n):
    if n==0:
        return 0
    
    return ((n%10)+ SumOfDigits(n//10))

n=int(input())
print(SumOfDigits(n))