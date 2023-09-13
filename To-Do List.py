import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Enter your task.")

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def clear_tasks():
    task_list.delete(0, tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x470")

# Set background color
root.configure(bg="red")

# Create and place widgets
task_label = tk.Label(root, text="Enter your Task:", font=("Arial", 16), bg="yellow",fg="black")
task_label.pack(pady=(20, 5))

task_entry = tk.Entry(root, font=("Arial", 16))
task_entry.pack(pady=(0, 10), padx=10, fill=tk.X)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 16), bg="light green", fg="black")
add_button.pack(padx=10, pady=(0, 5), fill=tk.X)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 16), bg="light green", fg="black")
remove_button.pack(padx=10, pady=(0, 5), fill=tk.X)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, font=("Arial", 16), bg="light green", fg="black")
clear_button.pack(padx=10, pady=(0, 5), fill=tk.X)

exit_button = tk.Button(root, text="Exit", command=exit_app, font=("Arial", 16), bg="light green", fg="black")
exit_button.pack(padx=10, pady=(0, 20), fill=tk.X)

task_list = tk.Listbox(root, font=("Arial", 16), selectbackground="grey")
task_list.pack(padx=5, fill=tk.BOTH, expand=False)

root.mainloop()
