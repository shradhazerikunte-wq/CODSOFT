def display_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks):
            status = "✓" if task.startswith("[Done]") else " "
            print(f"{i+1}. [{status}] {task.replace('[Done]', '').strip()}")
        print("------------------")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def update_task(tasks):
    """Updates an existing task."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_num] = new_task
            print(f"Task {task_num+1} updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task(tasks):
    """Marks a task as completed."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            if not tasks[task_num].startswith("[Done]"):
                tasks[task_num] = f"[Done] {tasks[task_num]}"
                print(f"Task {task_num+1} marked as completed.")
            else:
                print("This task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list program."""
    tasks = []
    
    while True:
        print("\n--- Menu ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()