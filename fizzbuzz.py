print("Welcome to FizzBuzz!")
print("Rules: This program prints numbers 1 to 30. For multiples of 3, it prints 'Fizz'. For multiples of 5 prints 'Buzz'. For multiples of both, prints 'FizzBuzz")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)