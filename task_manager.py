import json

USERNAME = "user@gmail.com"
PASSWORD = "user123"


class Task:
    def __init__(self, task_id, task_name, is_completed=False):
        self.task_id = task_id
        self.task_name = task_name
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'task_name': self.task_name,
            'is_completed': self.is_completed
        }


def login():
    print("Welcome to Task Manager CLI")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == USERNAME and password == PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

# Load tasks from file
def load_tasks():
    try:
        with open('tasks.json', 'r') as fobj:
            tasks_data = json.load(fobj)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as fobj:
        json.dump([task.to_dict() for task in tasks], fobj)

# Add a new task
def add_task(tasks):
    task_id = len(tasks) + 1
    task_name = input("Enter task name: ")
    new_task = Task(task_id, task_name)
    tasks.append(new_task)
    print(f"Task '{task_name}' added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Completed" if task.is_completed else "Not Completed"
            print(f"ID: {task.task_id}, Task: {task.task_name}, Status: {status}")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    task = next((task for task in tasks if task.task_id == task_id), None)
    if task:
        tasks.remove(task)
        print(f"Task '{task.task_name}' deleted successfully!")
    else:
        print("Task not found!")
#Complete task
def complete_task(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    task = next((task for task in tasks if task.task_id == task_id), None)
    if task:
        task.mark_completed()
        print(f"Task '{task.task_name}' marked as complete!")
    else:
        print("Task not found!")

def main():
    if not login():
        exit()  

    tasks = load_tasks()  

    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)  
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
