for _ in range(int(input())): 
 n=int(input())
 l=list(map(int,input().split()))
 d={}
 for i in l:
    d[i]=d.get(i,0)+1 
 d2={}
 for i in list(d.values()):
    d2[i]=d2.get(i,0)+1 
 maxm=0
 for i in d2:
    if d2[i]>maxm:
        maxm=d2[i]
        num=i
    if d2[i]==maxm:
        if i<num:
            num=i 
 print(num)            
    