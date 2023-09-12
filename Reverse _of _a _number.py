# num=int(input())
# reverse=""
# while num>0:
#     dig=num%10
#     reverse+=str(dig)
#     num//=10
# print(int(reverse))

num=int(input())
reverse=0
while num>0:
    dig=num%10
    reverse=reverse*10+dig
    num//=10
print(reverse)