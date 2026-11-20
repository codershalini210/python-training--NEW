def assess_progress(attendance,assignment_completion):
    status = ""
    if(attendance>=90 and assignment_completion>=90):
        status ="Green"
    elif(attendance>=75 and assignment_completion>=75):
        status ="Amber"
    else:
        status = "Red"
    return status
att= int(input("Enter attendence percentage"))
assign= int(input("Enter assignment completion percentage"))

progress_status = assess_progress(att,assign)
    
print(f"attendence percentage {att}")
print(f"assignment completion percentage {assign}")
print(f"your progress status is {progress_status}")
