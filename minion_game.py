def minion_game(s):
 l=len(s)
 sum1=0
 sum2=0
 
 for i in range(0,l):
    if (s[i]=='A')or(s[i]=='E')or(s[i]=='I')or(s[i]=='O')or(s[i]=='U'):
        sum1=sum1+l-i
    else:
        sum2=sum2+l-i
 
 if sum1>sum2:
    print('Kevin '+str(sum1))
 elif sum2>sum1:
    print('Stuart '+str(sum2))
 else:
    print('Draw')
    