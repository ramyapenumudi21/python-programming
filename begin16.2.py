p1=int(input())
p2=int(input())
for p in range(p1,p2):
   if p> 1:
       for i in range(2,p):
           if (p % i) == 0:
               break
       else:
           print(p)

