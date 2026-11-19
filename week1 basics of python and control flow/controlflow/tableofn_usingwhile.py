# no = int(input("Enter any no "))
# i = 1
# while(i<=10):
#     print(f"{no} X {i} = {no*i}")
#     i = i+1
print("\n no's from 10 to 1 using while loop \n")
n=10
while(n>=1):
    print(n, end=" ")
    n=n-1
print()
print("-"*50)
print("\n hello world 5 times using for loop \n")
print("Hello world "*5)
print("-"*50)
print(" \ncube of all the numbers between 5-10\n")
for i in range (5,11):
    print(i**3 , end=" ")
print()
print("-"*50)
# 4 write a program to count how many numbers are divisible by both 3 and 5 
# between 1-100
count = 0 
for number in range(1,101):
    if(number%3 ==0 and number %5 ==0):
        count=count+1
print(f"\n{count }numbers are divisible by both 3 and 5  between 1-100")
print("-"*50)