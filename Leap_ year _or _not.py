# Leap year or not
number=int(input())
if number%400==0 or (number%4==0 and number%100!=0):
    print("Leap year")
else:
    print("NOT leap year")