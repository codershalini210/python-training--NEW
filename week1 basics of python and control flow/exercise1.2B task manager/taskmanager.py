tasks=[]
def show_menu():
    print(" press \n 1: Add task,\n 2: View tasks,\n 3 : Show task count \n, 4: Exit.") 
def add_task():
    task_item = input("Enter task ")
    if(task_item==""):
        print("Empty task not allowed")
    else:
        tasks.append(task_item)
        print("Task added successfully")
def view_tasks(task_list):
    if(len(task_list)==0):
        print("Empty list ")
    else:
        for t in task_list:
            print(t)
            
def task_count(task_list):
    return len(task_list)

while(True):
    show_menu()
    ch=input()
    if(ch=="1"):
        add_task()
    elif(ch=="2"):
        view_tasks(tasks)
    elif(ch=="3"):
        print("Total tasks",task_count(tasks))
    else:
        break
