print("Welcome to Lesson 403 For Loops")
# Looping through a dictionary
person = {
    "name": "Thomas",
    "age": 40,
    "profesion": "Heavy Duty Mechanic",
}

for key, value in person.items():
    print(f"The key is {key} and the Value is {value}")
    
#Looping through a list of people in my family
lst = ["Thomas", "Cohen","Sandra","Oreo","Sasha"]
lst = set(lst)

for lst in lst:
    print(f"My family consists of {lst}")
    
# Lets loop through the letters of a string!!

car = "Honda Civic"

for letter in car:
    print(letter)    