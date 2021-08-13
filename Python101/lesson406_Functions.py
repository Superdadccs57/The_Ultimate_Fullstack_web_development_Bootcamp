print("")

def welcome(name):
    print(f"Welcome to Lesson 406 Functions; {name}")
    print("________________________________________")
    
welcome("Thomas")

print("")
print("The welcome message just happens to be the first example of this lesson and is designed to welcome me into the lesson using a function!")

print("")
print("Example 2: Multiple Parameters and a default Parameter")

def somename(name, food="Pizza"):
    print(f"Hello {name}. Let's eat some {food}")
    
somename('Thomas')

print("When I called the function somename I declared 'Thomas' for the name parameter but did not use a parameter for the food. Because I set the food parameter to have a default parameter it printed pizza, below I will run the fuction again but this time I will include food parameter to be different from the default Pizza!")

print('')

somename('Cohen', 'Ribs')

print('')
print('Example 3: Creating a basic exponent Calculator')
print('')

def exp(num1, num2):
    total = num1 ** num2
    return total
print("33 ** 6 = ")
big_number = exp(33, 6)
print(big_number)
    
