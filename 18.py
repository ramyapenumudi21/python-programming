p1 = input()
p2 =input()
for num in range(p1,p2+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
        print(num)
