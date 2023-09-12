num=int(input())
reverse=0
temp=num
while num>0:
    dig=num%10
    reverse=reverse*10+dig
    num//=10
if reverse==temp:
    print("palindrome")
else:
    print("not palindrome")