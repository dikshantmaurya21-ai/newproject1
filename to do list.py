
list = []
file = input("enter you want:")
def add_task():
    global file
    file = ("file.txt","a") 
print("add task successfully")

def view_tasks():
    try:
        with open("file.txt","r") as file:
            tasks = file.readlines()
            for task in tasks:
                print(task.strip())
    except FileNotFoundError:
        print("No tasks found.")

def update_task():
    update_task = input("enter the task you want to update:")
    for i, task in enumerate(tasks, 1):
        print(i, ".", task)

    number = int(input("Enter task number: "))
    new_task = input("Enter new task: ")

    tasks[number - 1] = new_task

    print("Task updated successfully!")
    
     

