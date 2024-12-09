import random

print('hello world')

vars = 'saif'
vars1 = ['apple', 'orange', 'banana']

print(vars)
print(vars1)

if(vars1 != 'apple') :print('good')

else: print('not good')

print('hello Phyton')

# Generate a random number
print(f"Random num : {random.randint(1, 100)}")

# Convert celsius to fahrenheit

celsius = float(input("Enter temperature in celsius :"))

fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degress celsius is equal to {fahrenheit} degree fahrenheit")