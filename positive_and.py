def chek(n):
    return(n!=0 and (n&(n-1)==0))
    
t=int(input())

while(t>0):
    l=[2,3,1,5,4]
    t-=1
    n=int(input())
    if(n==1):
        print(1)
        continue
    elif(n==3):
        print("1 3 2")
        continue
    elif(n==5):
        for i in l:
            print(i,end=' ')
        continue
    elif(chek(n)):
        print(-1)
        continue
    else:
        i=6
        while(i<=n):
            if(chek(i)):
                l.append(i+1)
                l.append(i)
                i+=2
            else:
                l.append(i)
                i+=1
        for i in l:
            print(i,end=" ")
 