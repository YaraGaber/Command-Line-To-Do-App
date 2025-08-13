import datetime
import re
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if os.path.exists(TASKS_FILE) and os.path.getsize(TASKS_FILE) > 0:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    """Adds a new task to the list."""
    description = input("Enter task description: ")
    priority = input("Enter priority (low/medium/high): ")
    
    stop_words = ["a", "an", "the", "in", "on", "at", "to", "for", "with", "and", "or", "from", "of", "is", "are", "be", "call", "send"]
    
    words = re.findall(r'\b\w+\b', description.lower())
    tags = [word for word in words if word not in stop_words and len(word) > 2]
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_task = {
        'description': description,
        'priority': priority,
        'tags': tags,
        'timestamp': timestamp,
        'done': False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task added! Tags automatically generated: {', '.join(tags)}")

def list_tasks(tasks):
    """Lists all tasks."""
    print("\n📋 Simple To-Do App (with priority, tags, and timestamps)")
    if not tasks:
        print("No tasks to display.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        
        tags_string = ', '.join(task.get('tags', []))
        
        print(f"{i}. {status} {task['description']} | Priority: {task['priority']} | Tags: {tags_string} | Added: {task['timestamp']}")

def done_task(tasks, task_number):
    """Marks a task as complete."""
    try:
        task_index = int(task_number) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['done'] = True
            save_tasks(tasks)
            print(f"✅ Task {task_index + 1} marked as done!")
        else:
            print("❌ Invalid task number.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter a valid task number.")

def delete_task(tasks, task_number):
    """Deletes a task from the list."""
    try:
        task_index = int(task_number) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"🗑️ Task '{deleted_task['description']}' deleted!")
        else:
            print("❌ Invalid task number.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter a valid task number.")

def main():
    """Main function to run the application."""
    tasks = load_tasks()

    while True:
        print("\nCommands: add | list | done <task_number> | delete <task_number>")
        command = input("> ").strip().lower()

        if command == "add":
            add_task(tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command.startswith("done"):
            try:
                _, task_number = command.split(' ', 1)
                done_task(tasks, task_number)
            except ValueError:
                print("❌ Invalid 'done' command. Usage: done <task_number>")
        elif command.startswith("delete"):
            try:
                _, task_number = command.split(' ', 1)
                delete_task(tasks, task_number)
            except ValueError:
                print("❌ Invalid 'delete' command. Usage: delete <task_number>")
        else:
            print("❌ Invalid command.")

if __name__ == "__main__":
    main()
