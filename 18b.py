l = int(raw_input())
u = int(raw_input())
 
for num in range(l,u):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
