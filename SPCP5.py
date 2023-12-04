# cook your dish here
from sympy import isprime
for t in range(int(input())):
    h = int(input())
    power= 1 
    moves=0 
    
    if(h==1):
        print(1)
        continue 
    if(h==0):
        print(-1)
        continue
    while h>0 and not isprime(h):
        h=h-power 
        power*=2
        moves+=1
    if(h<0):
        moves=-1
    elif isprime(h):
        moves+=1
    print(moves)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    