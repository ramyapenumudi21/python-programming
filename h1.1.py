S=int(input())
a= []
for val in range(0,S):
   p = int(input())
   a.append(p)
a.sort()
b = sorted(set(a))
c = []
if a==b:
   print "unique"

else: 
    for j in range(len(b)):
        if(a.count(b[j]) > 1 ):
           c.append(b[j])
    print (' '.join (str(k) for k in c))
