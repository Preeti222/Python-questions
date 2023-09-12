num=int(input())
sum=0
temp=num
while num>0:
    fact=1
    dig=num%10
    while dig>0:
        fact*=dig
        dig-=1
    sum+=fact
    num//=10
if temp==sum:
    print("strong number")
else:
    print("not strong number")