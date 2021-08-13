something = "None"

if something:
    print('this is true')
else:
    print("this is false")
    
# The above is going to print out the false statement cause thats what the none thingy does

something = "This is a string that will return"

if something:
    print(something, "True")
else:
    print("This is false")
    
something = ""

if something:
    print("Will an empty String print me out?")
else:
    print("Empty Strings will return False values")
    
something = " "

if something:
    print("Turns out that a space in a string will change it from an empty string to a string!!")
else:
    print("Empty Strings will return False values")
    
lst = []

if lst:
    print("An empty list is True")
else:
    print('An empty list is False')

lst = ["Item 1", "Item 2","Item 3"]

if something:
    print(lst, "A list with items will print True")
else:
    print("A list with Items will print False")
    
sets = {
    "Key" : "Value",
    "Name": "Thomas"
}

if sets:
    print(sets["Name"])
else:
    print("This is False")
    
sets = {
    
}

if sets:
    print(sets["Name"])
else:
    print("Empty Sets will print False")
    
tuples = ()

if sets:
    print("An empty tuple will print True")
else:
    print("An empty tuple will print False")
    
tuples = ("Thomas","Cohen", "Sandra")

if tuples:
    print(tuples, "are True")
else:
    print("An empty tuple will print False")