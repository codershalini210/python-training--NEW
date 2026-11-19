# """ student is eligible for exam only if attendence is greater than 75 
# and marks are greater than or equal to 40"""
# attendance = int(input("Enter attendance"))
# marks = int(input("Enter marks "))
# if( attendance>=75 and marks >=40):
#     print("Eligible for exam")
# else:
#     print("Not eligible ")
#DL : age must be greater than 18  and passed the driving test 
age = int(input("Enter age "))
test_result = input("Enter test result : True/False")
if(age> 18 and test_result=="True"):
    print("Eligible for DL")
else:
    print("Not eligible for DL ")