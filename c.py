import tkinter as tk
from tkinter import messagebox

tasks = []


def add_task():
    task = entry_task.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    
    tasks.append(task)
    update_listbox()
    entry_task.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox_tasks.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_completed():
    try:
        selected = listbox_tasks.curselection()[0]
        tasks[selected] = tasks[selected] + " ✔"
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        update_listbox()
    except:
        pass 

def clear_all():
    tasks.clear()
    update_listbox()


root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("500x450")
root.configure(bg="#1e1e2f")

label_title = tk.Label(root, text="TO-DO LIST MANAGER", 
                       font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
label_title.pack(pady=10)

entry_task = tk.Entry(root, font=("Arial", 14), width=30)
entry_task.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", width=15, bg="#4caf50", fg="white",
                    font=("Arial", 12), command=add_task)
btn_add.pack(pady=5)

frame_list = tk.Frame(root)
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(frame_list, width=50, height=10, 
                           font=("Arial", 12), yscrollcommand=scrollbar.set)
listbox_tasks.pack()

scrollbar.config(command=listbox_tasks.yview)

frame_buttons = tk.Frame(root, bg="#1e1e2f")
frame_buttons.pack(pady=10)

btn_delete = tk.Button(frame_buttons, text="Delete Task", width=15,
                       bg="#f44336", fg="white", font=("Arial", 12),
                       command=delete_task)
btn_delete.grid(row=0, column=0, padx=5)

btn_complete = tk.Button(frame_buttons, text="Mark Completed", width=15,
                         bg="#2196f3", fg="white", font=("Arial", 12),
                         command=mark_completed)
btn_complete.grid(row=0, column=1, padx=5)

btn_save = tk.Button(root, text="Save Tasks", width=15,
                     bg="#ff9800", fg="white", font=("Arial", 12),
                     command=save_tasks)
btn_save.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", width=15,
                      bg="#9c27b0", fg="white", font=("Arial", 12),
                      command=clear_all)
btn_clear.pack(pady=5)

load_tasks()
root.mainloop()
