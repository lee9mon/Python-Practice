def write_tasks(task):
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')

def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet!")
                return
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

def remove_task(task_number):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print(f"Task {task_number} has been deleted.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

def show_menu():
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            write_tasks(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                remove_task_number = int(input("Enter task number to remove: "))
                remove_task(remove_task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

show_menu()