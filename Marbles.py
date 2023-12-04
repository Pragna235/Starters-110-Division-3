
def marbles(a,b):
    
    
    A,B = a,b
    c,C = 0,0
    
   
    if a%b == 0:
        return 0
        
    
    while b > 0:
        if a%b == 0:
            break
        a,b = a+1,b-1
        c += 1 
        
   
    if B>=A:
        return c
    
   
    while A%B != 0:
        if A%B == 0:
            break
        A,B = A-1,B+1 
        C += 1
    
     
    return min([c,C])
            
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(marbles(a,b))
