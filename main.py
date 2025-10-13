import tkinter as tk
from tkinter import IntVar
import ttkbootstrap as ttk
from ttkbootstrap import Style

class ToDoApp:
    """Class responsible for running the app"""
    def __init__(self):
        """Initialization of the class"""
        self.root = tk.Tk()
        self.root.geometry("280x500")
        self.root.title("To Do App")
        self.style = Style(theme = "darkly")
        self.task_vars = []

        self.current_tasks = []
        self.add_task_bool = False
        self.task_text = ttk.StringVar()

        self.add_task_bt()
        self.text_current_tasks()

    def run_app(self):
        """Running the app"""
        self.root.mainloop()
    def add_task_bt(self):
        """Showing add task button"""
        self.new_task_bt = ttk.Button(self.root,
                                      text = "New Task",
                                      bootstyle = "primary",
                                      command = self.adding_task)
        self.new_task_bt.place(x = 180, y = 10, width = 90, height = 40)

    def adding_task(self):
        """Function shows the place where you can type task name"""
        if not self.add_task_bool:
            self.new_task = ttk.Entry(self.root, bootstyle = "light", textvariable = self.task_text)
            self.new_task.place(x = 70, y = 190, width = 140, height = 60)
            self.new_task.bind("<Return>", self.confirm_task)
            self.add_task_bool = True
        else:
            self.new_task.destroy()
            self.add_task_bool = False

    def confirm_task(self, event = None):
        """Confirming the task and adding it to the list of current tasks"""
        text = self.task_text.get()
        if text:
            self.current_tasks.append(text)
            self.task_vars.append(IntVar(value = 0))
            self.task_text.set("")
            self.new_task.destroy()
            self.show_current_tasks()
            self.add_task_bool = False
    def text_current_tasks(self):
        self.current_tasks_label = ttk.Label(self.root, bootstyle = "inverse-info", text = "Current Tasks")
        self.current_tasks_label.place(x = 10, y = 10, width = 90, height = 40)
 
    def show_current_tasks(self):
        """Showing all the current tasks"""
        #showing all current tasks
        yaxis = 50
        for i, task in enumerate(self.current_tasks):
            new_task = ttk.Label(self.root, bootstyle = "warning", text = task)
            new_task.place(x = 10, y = yaxis, width = 110, height = 40)
            new_task_check = ttk.Checkbutton(self.root, bootstyle = "success", variable = self.task_vars[i])
            new_task_check.place(x = 125, y = yaxis + 12)
            yaxis += 40


        

if __name__ == "__main__":
    ai_app = ToDoApp()
    ai_app.run_app()
