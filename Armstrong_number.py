num=int(input())
length=len(str(num))
temp=num
res=0
while num>0:
    dig=num%10
    res+=dig**length
    num//=10
if res==temp:
    print("armstrong")
else:
    print("not armstrong")