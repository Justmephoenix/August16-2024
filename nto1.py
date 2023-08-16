def NToOne(n):
    if n==0:
        return
    print(n)
    NToOne(n-1)
  
    
n=int(input())
NToOne(n)