 # Method 1: Using Brute Force
# number=int(input())
# if number<0:
#     print("Negative number",number)
# elif number>0:
#     print("Positive number",number)
# else:
#     print("zero")



#second way nested if else

# num=int(input())
# if num>=0:
#     if num==0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

# Ternary Operator Syntax
# ( Condition ) ? ( if True : Action) : ( if False : Action) ;

#third way by ternary operator
num=int(input())
print("positive" if num>0 else "negative" )