n=int(input())
n1=0
n2=1
sum=0
for i in range(n):
    print(n2,end="")
    sum=n1+n2
    n1=n2
    n2=sum