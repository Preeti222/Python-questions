num=int(input())
num2=int(input())
for i in range(num,num2+1):
    length=len(str(num))
    temp=i
    sum=0
    while temp>0:
        dig=temp%10
        sum+=dig**length
        temp//=10
    if sum==i:
        print(sum,end="")

