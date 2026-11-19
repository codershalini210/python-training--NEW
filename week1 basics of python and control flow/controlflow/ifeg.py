name = input("Enter your name ")
marks = int(input("Enter marks "))
if(marks<0):
    print("Invalid marks ")
elif(marks>100):
    print("Invalid marks")
elif( marks >=90):
    print(f"{name} your Grade : A")
elif(marks>=80):
    print(f"{name} your Grade : B")
elif(marks>=70):
    print(f"{name} your Grade : C")
elif(marks>=50):
    print(f"{name} your Grade : D")
else:
    print(f"{name} your result :fail")
#que write a program to take name and age from user
# and print person is senior citizen or not 
# name = input("Enter name")
# try:
#     age = int(input("Enter age "))

#     if(age>120):
#         print("Invalid age")
#     elif(age>59):
#         print(f"{name} you are a senior citizen")
#     elif(age>0):
#         print(f"{name} you are not a senior citizen")
#     else:
#         print("invalid age")
# except:
#     print("Enter numeric age ")