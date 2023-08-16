r=0
def reverseNum(n):
    global r
    if n==0:
        return r
    if n>0:
        temp=n%10
        
        r= r*10 +temp
        reverseNum(n//10)
    return r
  
    
n=int(input())
print(reverseNum(n))
