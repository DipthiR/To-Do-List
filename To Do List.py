import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASK_FILE = "tasks.txt"
tasks = []

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = tasks[index]
        tasks[index] = f"✔️ {task}" if not task.startswith("✔️") else task.replace("✔️ ", "")
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to mark as done.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("420x450")

task_entry = tk.Entry(root, font=("Segoe UI", 12), width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", width=15, command=mark_done)
done_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Segoe UI", 12), width=50, height=10)
task_listbox.pack(pady=10)

# Load saved tasks
load_tasks()
update_listbox()

# Start app
root.mainloop()
