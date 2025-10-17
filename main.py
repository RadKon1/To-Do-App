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
        self.style = Style(theme="darkly")
        self.task_vars = {}

        self.current_tasks = []
        self.list_of_task_buttons = []
        self.list_of_checkbuttons = []
        self.add_task_bool = False
        self.del_task_bool = False
        self.task_text = ttk.StringVar()
        self.cur_tas_text_height = 65
        self.yaxis = 100  # liczy jak ustawiać kolejne labele i checkbutton.
        self.add_task_bt()
        self.del_task_bt()
        self.text_current_tasks()

    def run_app(self):
        """Running the app"""
        self.root.mainloop()

    def add_task_bt(self):
        """Showing add task button"""
        self.new_task_bt = ttk.Button(self.root,
                                      text="New Task",
                                      bootstyle="primary-outline",
                                      command=self.adding_task)
        self.new_task_bt.place(x=180, y=10, width=90, height=40)

    def del_task_bt(self):
        """Showing the button meant for deletion of tasks"""
        self.del_task_bt = ttk.Button(self.root,
                                      text="Del Task",
                                      bootstyle="danger-outline",
                                      command=self.delete_task)
        self.del_task_bt.place(x=180, y=55, width=90, height=40)

    def adding_task(self):
        """Function shows the place where you can type task name"""
        if not self.add_task_bool:
            self.new_task = ttk.Entry(self.root,
                                      bootstyle="light",
                                      textvariable=self.task_text)
            self.new_task.place(x=70, y=190, width=140, height=60)
            self.new_task.bind("<Return>", self.confirm_task)
            self.add_task_bool = True
        else:
            self.new_task.destroy()
            self.add_task_bool = False

    def confirm_task(self, event=None):
        """Confirming the task and adding it to the list of current tasks"""
        text = self.task_text.get()
        if text:
            self.current_tasks.append(text)
            self.task_vars[text] = IntVar(value=0)
            self.task_text.set("")
            self.new_task.destroy()
            self.show_current_tasks()
            self.add_task_bool = False

    def delete_task(self):
        """Confirming the deleiton of the task written in the box"""
        if not self.del_task_bool:
            self.del_task = ttk.Entry(self.root,
                                      bootstyle="light",
                                      textvariable=self.task_text)
            self.del_task.place(x=70, y=190, width=140, height=60)
            self.del_task.bind("<Return>", self.confirm_deletion)
            self.del_task_bool = True
        else:
            self.del_task.destroy()
            self.del_task_bool = False

    def confirm_deletion(self, event=None):
        """deleting the task form the list of tasks and
        showint updated list of tasks"""
        text = self.task_text.get()
        if text:
            if text in self.current_tasks:
                self.current_tasks.remove(text)
            self.task_vars.pop(text, None)
            self.task_text.set("")
            self.del_task.destroy()
            self.show_current_tasks()
            self.del_task_bool = False
            self.yaxis -= 40
            self.cur_tas_text_height -= 40

    def text_current_tasks(self):
        self.current_tasks_label = ttk.Labelframe(self.root,
                                                  bootstyle="info",
                                                  text="Current Tasks")
        self.current_tasks_label.place(x=10,
                                       y=10,
                                       width=145,
                                       height=self.cur_tas_text_height)

    def show_current_tasks(self):
        """Showing all the current tasks"""
        self.yaxis = 30
        if len(self.current_tasks) >= 3:
            self.cur_tas_text_height = len(self.current_tasks) * 60
        else:
            self.cur_tas_text_height += 40
        self.current_tasks_label.destroy()
        self.text_current_tasks()
        for button in self.list_of_task_buttons:
            button.destroy()

        for check in self.list_of_checkbuttons:
            check.destroy()

        for i, task in enumerate(self.current_tasks):

            new_task = ttk.Label(self.root, bootstyle="warning", text=task)
            new_task.place(x=20, y=self.yaxis, width=110, height=40)
            new_task_check = ttk.Checkbutton(self.root,
                                             bootstyle="success",
                                             variable=self.task_vars[task])
            new_task_check.place(x=125, y=self.yaxis + 12)
            self.yaxis += 40
            self.list_of_task_buttons.append(new_task)
            self.list_of_checkbuttons.append(new_task_check)


if __name__ == "__main__":
    ai_app = ToDoApp()
    ai_app.run_app()
