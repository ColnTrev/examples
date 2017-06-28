#Welcome to Python! This is a comment

print("Hello World!") # The print function prints things to the screen
print(4) # Print will print the number 4

# There are no curly braces ({}) or semicolons (;) in Python
# The interpreter relies on the indentation to determine what code to run
# For example, look at the if else statements:

if 2 == 2:
    print("2 is equal to 2")

if 2+2 == 5:
    print("We live in another reality!")
else:
    print("Nah, it equals 4")

# Below is an example of getting input from the user

x = input("Enter a number: ")

# The text inside the input function is the prompt that will appear on screen!
# That's pretty cool right??

# Python reads everything in as a string, so if we want to have an integer or
# a double, we have to convert it like Below

x = int(x)

#alternatively, this could be done on one line like this:

y = int(input("Enter another number: "))

# else if is abbreviated to elif look at the if statement Below

if x > y:
    print("x is greater than y!")
elif x < y:
    print("x is less than y!")
else:
    print("They're equal I guess!")
