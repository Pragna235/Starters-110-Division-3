# cook your dish here
for i in range(int(input())):
    n,x,k = map(int,input().split())
    girls = n-x 
    bg = x//k 
    gg = girls//k 
    
    remb = x - (bg*k)
    remg = girls - (gg*k)
    
    dgrps = min(remb,remg)
    
    rem = remb+remg
    
    print(rem - (dgrps*2))
