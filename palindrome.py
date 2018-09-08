p=int(input("enter a number"))
temp=p
rev=0
while(p>0):
 digit=p%10
 rev=rev*10+digit
 p=p/10
 if(temp==rev):
   print("Palindrome")
 else:
    print("not Palindrome")
