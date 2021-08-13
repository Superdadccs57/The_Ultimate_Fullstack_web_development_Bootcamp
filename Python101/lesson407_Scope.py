print('')
name = input("What is your name?")
print('')

def welcome(name):
    print(name,"Welcome to Lesson 407: Scope")
    
welcome(name)
print('***************************************')

print("Example 1: Variables declared within a function can't be used outside of a function")
print('')

def myfunc():
    car = "Chevelle"
    return car
myfunc()
#print(car)

print('I have commented out the print(car) on line 16 because it causes an undefined variable error')
print('')

print('In the function below will it print a new name that is within the function or will it print the name declared at the beginning of the program?')

def myfunc():
    name = "Cohen"
    if name.lower() == "cohen":
        print("Looks like it printed the name within the function:")     
    else:
        print("Nope it printed the name that was input at the beginning of the program!")
    return name

print(myfunc())

print('')
print(name, "is the name that you entered at the beginning of the program!")