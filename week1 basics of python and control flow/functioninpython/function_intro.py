def hello():
    print("Hello world how are you today")      

def greet(name):
    print(f"welcome {name}")
    
def sum(x,y):
    s = x+y
    return s
hello()
greet('Alex')
greet('Ron')

firstno = int(input("Enter first no "))
secondno = int(input("Enter second no "))
# addition = sum(firstno,secondno)
# print("sum is ",addition)
print("sum is ",sum(firstno,secondno))

# Write a function that prints your name and city.
# Write a function that accepts a number and prints its square.
# Write a function that returns the cube of a number.