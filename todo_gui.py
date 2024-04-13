import tkinter as tk
from tkinter import messagebox
from todo_core import load_tasks, save_tasks

# At the start where the tasks variable is initialized
tasks = load_tasks()


def refresh_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        refresh_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "The task cannot be empty.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks.pop(task_index)
        refresh_listbox()
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def on_closing():
    save_tasks(tasks)
    root.destroy()

root = tk.Tk()
root.title("Todo List")
tasks = load_tasks()

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

task_entry = tk.Entry(root, width=52)
task_entry.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, command=lambda: save_tasks(tasks))
button_save_tasks.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
refresh_listbox()

root.mainloop()
