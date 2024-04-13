def load_tasks(filename='todo_list.txt'):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        # If the file doesn't exist, we return an empty list
        pass
    return tasks


def save_tasks(tasks, filename='todo_list.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
