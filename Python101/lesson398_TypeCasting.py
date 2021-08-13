# Type Casting is turning one data type to another data type!

age = input("What is your age?")
data_type = type(age)
print(data_type)

age = int(age)
data_type = type(age)
print(data_type)

print("Your age in dog years is", age * 7)

print("This is a grocery list can you tell what data type it is?")
grocery_list = ['Apples', 'Orange', 'Bananas', 'Apples']
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))

print("This is a grocery list can you tell what data type it is?")
grocery_list = ['Eggs', 'Pizza', 'Coffee', 'Cat Food']
grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))