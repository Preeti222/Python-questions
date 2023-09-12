# N=int(input())
# i=1
# sum=0
# while i<=N:
#     sum+=i
#     i+=1
# print(sum)

# using recursion
def getsum(num):
    if num==1:
        return 1
    else:
        return num+getsum(num-1)
num=int(input())
print(getsum(num))