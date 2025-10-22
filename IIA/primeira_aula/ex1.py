''' 
FizzBuzz: Print numbers 1..50, replacing multiples of 3 with Fizz,
 5 with Buzz, and both with FizzBuzz.

'''

i = 1

for i in range(50):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)