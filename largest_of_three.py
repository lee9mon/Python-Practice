num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    max = num1
else:
    max = num2 
if num3 > max:
    max = num3
print(f"The largest number is: {max}")
