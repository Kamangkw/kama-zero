import sys
from todo_core import load_tasks, save_tasks

def main_menu():
    tasks = load_tasks()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter a task to add: ")
            tasks.append(task)
        elif choice == "2":
            if tasks:
                print("Todo List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("Your todo list is empty!")
        elif choice == "3":
            if tasks:
                index = int(input("Enter task number to remove: "))
                try:
                    tasks.pop(index-1)
                except IndexError:
                    print("Invalid task number.")
            else:
                print("Nothing to remove.")
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose from 1-4.")

if __name__ == "__main__":
    main_menu()
