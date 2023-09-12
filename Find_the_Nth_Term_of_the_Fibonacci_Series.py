def fibonaci(n):
    if n<0:
        return "invalid input"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n+1):
            sum=a+b
            a=b
            b=sum
        return b
print(fibonaci(10))