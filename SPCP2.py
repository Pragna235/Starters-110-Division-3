# cook your dish here
for i in range(int(input())):
    x,n=map(int,input().split())
    already = x*100 
    remaining = n-already
    if(remaining>0):
        if(remaining%100 == 0):
            print(remaining//100)
        else:
            print((remaining//100)+1)
    else:
        print(0)
