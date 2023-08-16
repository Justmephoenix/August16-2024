def OneToN(n):
    if n>0:
        OneToN(n-1)
    print(n)
    
    
    
    
n=int(input())
OneToN(n)