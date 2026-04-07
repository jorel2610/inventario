# main.py
from archivo import load_tasks
from functions import (
    
    add_task,
    list_tasks,
    search_task,
    update_task,
    delete_task
)


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 55)
    print("           TASK MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add new task")
    print("2. List all tasks")
    print("3. Search task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")
    print("=" * 55)


def main():
    print("Starting Task Management System...\n")
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("\nSelect an option (1-6): ").strip()

        if option == "1":
            tasks = add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            search_task(tasks)
        elif option == "4":
            tasks = update_task(tasks)
        elif option == "5":
            tasks = delete_task(tasks)
        elif option == "6":
            print("\nThank you for using the Task Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()