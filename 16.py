R=input()
P=input()
for i in range(R,P+1):
    if(i>1):
       for K in range(2,i):
           if(i%K==0):
               break
       else:
           print(i)
