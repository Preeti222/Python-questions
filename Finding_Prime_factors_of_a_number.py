num=int(input())
i=2
while num>1:
    if num%i==0:
        print(i)
        num//=10
    else:
        i+=2
    

n=int(input())
i=1
while i<=n:
    c=0
    if n%i==0:
        j=1
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print(i)
    i+=1