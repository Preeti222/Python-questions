# num=int(input())
# i=1
# c=0
# while i<=num:
#     if num%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("prime number",num)
# else:
#     print("Not prime number")

num=int(input())
ans=0
if num<2:
    ans=1
else:
    for i in range(2,num):
        if num%i==0:
            ans=1
            break
if ans==1:
    print('Not prime')
else:
    print("prime number")