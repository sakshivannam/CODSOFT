
print("\n****Welcome to the TO DO Application****")
my_list=[]

def add_task():
    
    task = input("Enter your task:")
    my_list.append(task)
    print("Task added successfully")

def display_task():
    print("****Your To Do List****\n")
    for i in range(len(my_list)):
        print(f'{i+1}. {my_list[i]}')

def remove_task():
    task = input("Enter task to be removed:")
    my_list.remove(task)
    print("Task removed successfully")

def update_task():
    task_index = int(input("Which task you want to update:"))
    task = input("Enter the changes to be updated:")
    my_list[task_index-1] = task

    
while True:
    print("\n____Options____\n")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Quit")
    choice = input("Enter Your Choice:")

    if choice == "1":
        add_task()
        display_task()

    elif choice == "5":
        quit()

    elif choice == "2":
        remove_task()
        display_task()

    elif choice == "3":
        update_task()
        display_task()
       

