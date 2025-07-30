tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.\n")
    else:
        print("Your Tasks:")
        i = 1
        for task in tasks:
            print(str(i) + ". " + task)
            i = i + 1
        print()

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    task_no = int(input("Enter the task number to delete: "))

    if task_no >= 1 and task_no <= len(tasks):
        removed_task = tasks[task_no - 1]
        tasks.remove(removed_task)
        print("Task deleted successfully!\n")
    else:
        print("Invalid task number.\n")

def main():
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

main()
