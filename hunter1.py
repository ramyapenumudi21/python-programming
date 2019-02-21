g=int(input())
l=input().split()
a=" ".join(map(str,l))
s=[]
for i in a:
    if(i not in s):
        if(a.count(i)>1):
            s.append(i)
a="".join(s) 
print(a)
