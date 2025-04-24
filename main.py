def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter new task to add: ")
    tasks.append({"task_added": task, "is_complete": False})
    print("Your task list has been expanded. Start knocking them out!")

def view_tasks(tasks):
    if not tasks:
        print("Free-day! No tasks found. Go do something productive!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["is_complete"] else "Not Completed"
            print(f"{index}. {task['task_added']} - {status}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["is_complete"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Enter a valid task number that corrisponds with completed task")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

