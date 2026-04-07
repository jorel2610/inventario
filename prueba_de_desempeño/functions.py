# functions.py
from archivo import save_tasks


def generate_id(tasks):
    """Generate a new unique ID"""
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(tasks):
    """Add a new task"""
    print("\n--- Add New Task ---")
    title = input("Title: ").strip()
    if not title:
        print("Error: Title is required.")
        return tasks

    description = input("Description: ").strip()

    # Priority validation
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Please enter only: high, medium or low.")

    task = {
        "id": generate_id(tasks),
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully! (ID: {task['id']})")
    return tasks


def list_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("No tasks registered yet.")
        return

    print("\n" + "=" * 95)
    print(f"{'ID':<4} {'Title':<30} {'Priority':<12} {'Status':<12} Description")
    print("=" * 95)

    for t in tasks:
        desc = t["description"][:55] + "..." if len(t["description"]) > 55 else t["description"]
        print(f"{t['id']:<4} {t['title']:<30} {t['priority'].capitalize():<12} "
              f"{t['status'].capitalize():<12} {desc}")

    print("=" * 95)


def search_task(tasks):
    """Search for tasks"""
    print("\n--- Search Task ---")
    criterion = input("Search by (id / title / status): ").strip().lower()

    if criterion not in ["id", "title", "status"]:
        print("Invalid criterion. Please use: id, title or status.")
        return

    term = input("Search term: ").strip().lower()

    found = [t for t in tasks if 
             (criterion == "id" and str(t["id"]) == term) or
             (criterion == "title" and term in t["title"].lower()) or
             (criterion == "status" and term in t["status"].lower())]

    if not found:
        print("No tasks found matching your search.")
        return

    print(f"\nFound {len(found)} task(s):\n")
    for t in found:
        print(f"ID: {t['id']} | Title: {t['title']}")
        print(f"Priority: {t['priority'].capitalize()} | Status: {t['status'].capitalize()}")
        print(f"Description: {t['description']}")
        print("-" * 70)


def update_task(tasks):
    """Update an existing task"""
    print("\n--- Update Task ---")
    try:
        task_id = int(input("Enter the task ID to update: "))
    except ValueError:
        print("Error: ID must be a number.")
        return tasks

    for t in tasks:
        if t["id"] == task_id:
            print("\nLeave blank to keep current value.\n")

            new_title = input(f"Title ({t['title']}): ").strip()
            if new_title:
                t["title"] = new_title

            new_desc = input(f"Description ({t['description']}): ").strip()
            if new_desc:
                t["description"] = new_desc

            # Priority
            priority = input(f"Priority ({t['priority']}): ").strip().lower()
            if priority in ["high", "medium", "low"]:
                t["priority"] = priority
            elif priority:
                print("Invalid priority. Keeping current value.")

            # Status
            status = input(f"Status ({t['status']}): ").strip().lower()
            if status in ["pending", "completed"]:
                t["status"] = status
            elif status:
                print("Invalid status. Use 'pending' or 'completed'. Keeping current value.")

            save_tasks(tasks)
            print("Task updated successfully.")
            return tasks

    print("No task found with that ID.")
    return tasks


def delete_task(tasks):
    """Delete a task"""
    print("\n--- Delete Task ---")
    try:
        task_id = int(input("Enter the task ID to delete: "))
    except ValueError:
        print("Error: ID must be a number.")
        return tasks

    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            confirm = input(f"Delete task '{t['title']}'? (y/n): ").strip().lower()
            if confirm == "y":
                del tasks[i]
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Deletion cancelled.")
            return tasks

    print("No task found with that ID.")
    return tasks