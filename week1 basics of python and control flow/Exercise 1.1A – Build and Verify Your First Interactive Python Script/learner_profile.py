"""
create a small learner profile and weekly study-hours calculator. 
The program will collect simple information, perform a calculation
and display a formatted summary.
"""
firstname = input("Enter name")
currentrole = input("Enter current role")
no_of_hrs_daily = int(input("Enter no of daily study hrs"))
no_of_training_days_in_week = 5
total_no_of_study_hrs = no_of_hrs_daily* no_of_training_days_in_week
print("Learner Name ",firstname)
print("current Role ", currentrole)
print("daily study hrs ", no_of_hrs_daily)
print("weekly total study hrs ", total_no_of_study_hrs)




