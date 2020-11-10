number1 = int(input())
number2 = int(input())
if number2 > number1:
    number1,number2 = number2,number1
print(number1)
print(number2)