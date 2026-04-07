# archivo.py
import json
import os

FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file"""
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                tasks = json.load(f)
            print(f"{len(tasks)} tasks loaded successfully.")
            return tasks
        except Exception:
            print("Error reading the file. Starting with an empty list.")
            return []
    else:
        print("No tasks file found. A new one will be created when you save your first task.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file"""
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print("Changes saved successfully.")
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False