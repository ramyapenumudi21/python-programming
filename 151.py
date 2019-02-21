s=input()
c=0
for x in range(0,len(s)):
    if(s[x]!='a' and s[x]!='b'):
        c=c+1
if(c>1):
    print("no")
else:
    print("yes")
