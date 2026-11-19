# amount = float(input("Enter amount"))
# premium_member = input("Are you a premium member : yes/no")
# if(amount>5000 or premium_member=="yes"):
#     print("Discount Available")
# else:
#     print("no Discount")
# scholarship: a student gets scholarship if either marks are greater than 90
# or family income is below 20000
marks = int(input("Enter marks "))
family_income = float(input("Enter family income "))
if(marks>=90 or family_income<20000):
    print("Eligible for scholarship")
else:
    print("not Eligible for Scholarship")