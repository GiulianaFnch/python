# Temperature Converter: Convert a list of Celsius temps to Fahrenheit using a list comprehension.

celsius = ["30.6", "21.9", "12.0", "12.9", "45.9"]

# newlist = [expression for item in iterable if condition == True]

# Use a list comprehension to convert to Fahrenheit, round to 1 decimal, and keep as floats
fahrenheit = [round(float(n) * 1.8 + 32, 1) for n in celsius]

print(fahrenheit)