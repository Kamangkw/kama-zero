import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def save_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def delete_task(task_to_delete):
    tasks = load_tasks()
    tasks = [task for task in tasks if task != task_to_delete]
    save_tasks(tasks)
