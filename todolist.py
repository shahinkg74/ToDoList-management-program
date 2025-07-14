import tkinter as tk
import json
import os


class  ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title ("manage your to-do list")

        self.tasks = self.load_tasks()

        self.task_entry =  tk.Entry(root, width = 50)
        self.task_entry.pack(pady = 10)

        self.add_task_button = tk.Button(root, text = "add a task", command = self.add_task)
        self.add_task_button.pack(pady = 5)

        self.task_listbox = tk.Listbox(root, width = 50,height = 10)
        self.task_listbox.pack(pady = 10)

        self.delete_task_button = tk.Button(root, text = "delete task", command = self.delete_task)
        self.delete_task_button.pack(pady = 5)

        self.load_tasks_to_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task":task , "done":False})
            self.save_tasks()
            self.load_tasks_to_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()    
        if selected_task_index:
            del self.tasks[selected_task_index[0]]   
            self.save_tasks()
            self.load_tasks_to_listbox()    

    def load_tasks(self):
        if os.path.exists("task.jason"):
            with open("task.json", "r") as file:
                return json.load(file)
        return[]
    
    def save_tasks(self):
        with open("task.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks_to_listbox(self):
          self.task_listbox.delete(0, tk.END)
          for task in self.tasks:
              self.task_listbox.insert(tk.END, task["task"])


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
                    



