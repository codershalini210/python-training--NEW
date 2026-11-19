#write a program to take length and width of rectangle 
# from user and then calculate and print area of that rectangle
#take length and width of rectangle from user and convert
# it to float
try:
    length = float(input("Enter length of rectangle"))
    width = float(input("Enter width of rectangle"))
    area = length* width
    print("area of rectangle is ",area)
except:
    print("Invalid input")