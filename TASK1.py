import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            removed_task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Task Removed", f'Task "{removed_task}" removed.')
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()