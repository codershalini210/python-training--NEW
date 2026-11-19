# def show_result(name,marks):
#     if(marks>=50):
#         print(f"{name } result : pass")
#     else:
#         print(f"{name} result :fail")

# show_result('John',47)
# show_result("Ron",85)

def show_result(name,marks):
    if(marks>=50):
        return f"{name} result : pass"
    else:
        return f"{name} result : fail"
while(True):
    n = input("Enter naem ")
    m = int(input("Enter marks"))
    print(show_result(n,m))
    op = input("Do you want to continue y/n")
    if(op!='y'):
        break