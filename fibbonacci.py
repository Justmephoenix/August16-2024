def FibonnaciSeris(a,b,n):
    if n==0:
        return
    next=a+b;
    print(next)
    a=b
    b=next
    FibonnaciSeris(a,b,n-1)
    
a=0
b=1
n=int(input())
print(a)
print(b)
FibonnaciSeris(a,b,n)