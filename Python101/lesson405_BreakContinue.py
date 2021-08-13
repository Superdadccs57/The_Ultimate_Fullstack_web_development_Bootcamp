print("Welcome to Lesson 405 Break and Continue")

print("Example One")

items = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

for item in items:
    if item == 'Two' or item == 'Four' or item == 'Six':
        continue
    print(item)

for item in items:
    if item == "Three":
        break
    print(item)

print("Example Two")

num = 0

while num <= 20:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)
    
print("Example Three")

num = 0
while num <= 1_000_000:
    num = num + 1
    if num == 13:
        break
    print(num)