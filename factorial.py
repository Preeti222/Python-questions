# num=int(input())
# fact=1
# while num>0:
#     fact*=num
#     num-=1
# print(fact)


def factorial(n):
    if n==0:
        return 1
    return (n*factorial(n-1))
n=int(input())
print(factorial(n))