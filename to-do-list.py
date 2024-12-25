import tkinter as tk
from tkinter import messagebox
import json

class ToDoAppGUI:
    def __init__(self, root, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
        self.root = root
        self.root.title("To-Do List Application")
        
        self.task_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=1, column=0, padx=10, pady=5)
        
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=10, pady=5)
        
        self.complete_button = tk.Button(root, text="Complete Task", width=20, command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        self.refresh_task_list()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "status": "Pending"})
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['status'] = 'Completed'
            self.save_tasks()
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.save_tasks()
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['status']}")

def main():
    root = tk.Tk()
    app = ToDoAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
