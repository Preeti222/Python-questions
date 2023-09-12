# import math
# n=int(input())
# if (math.ceil(math.sqrt(n)))==(math.floor(math.sqrt(n))):
#     print("yes perfect square")
# else:
#     print("no")

# another way
# def perfect_square(num):
#    i=1
#    while i*i<=num:
#     if i*i==num:
#        return True
#     i+=1
#    return False
# num=int(input())
# print(perfect_square(num))

import math
num=int(input())
if num>0:
    sr=math.sqrt(num)
    if sr*sr==num:
        print("perfect square")
    else:
        print("not perfect square")
else:
    print("invalid input")