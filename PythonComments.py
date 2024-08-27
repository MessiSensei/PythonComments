#Single Line Comments 
# This is a single-line comment
print("Hello, World!")  # This is also a single-line comment



#Multi-line Comments
# This is a comment
# that spans multiple lines
print("Multi-line comment example")

"""
This is another way to write
multi-line comments using a 
multi-line string.
"""

#When to Use Comments
#Explaining complex logic
# Checking if the number is prime
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(num, "is not a prime number")
        break


#Documenting the purpose of a function or class
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

#Leaving reminders or TODOs

# TODO: Optimize this loop for performance
for i in range(1000000):
    pass

#Disabling code
# print("This line is commented out and won't execute")
print("This line will execute")

"""
Best Practices for Writing Comments
Be concise and relevant: Comments should be short but informative, focusing on explaining why the code does something, not what it does (the code itself should be clear enough to understand the "what").

Keep comments up-to-date: If the code changes, make sure to update the corresponding comments so they remain accurate.

Avoid obvious comments: Don't comment on something that is clear from the code itself.

# Increment x by 1 (This is an obvious comment and should be avoided)
x += 1
"""
