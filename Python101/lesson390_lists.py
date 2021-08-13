#Lists are how we can store multiple items in one variable

lst = ["String", 1, 3.14, ["item"], "Thomas"]
print(lst)

for item in lst:
    print("The Item is a:", item)

# Here is some examples of list manipulation

names = ["Thomas","Cohen"]
print(names)

names.append("Sandra")
names.append("Oreo")
names.append("Sasha")
print(names)

names.remove("Sasha")
print(names)

Oreo = names.pop()
print(names)