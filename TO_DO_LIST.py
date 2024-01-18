import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json


TODO_FILE = "todo_list.json"
class TodoApp:
    def __init__(self,root):
        self.root=root
        self.root.title("To-Do List App")
        self.todo_list=self.load_todo_list()
        self.task_var=tk.StringVar()
        self.due_date_var=tk.StringVar()
        self.create_widgets()


    def create_widgets(self):
        # Task Entry in to the App
        tk.Label(self.root,text='Task:').grid(row=0,column=0,padx=10,pady=5)
        tk.Entry(self.root,textvariable=self.task_var).grid(row=0,column=1,padx=10,pady=5)


        #Entering the Due Date in the App
        tk.Label(self.root,text="Due Date (YYYY-MM-DD):").grid(row=1,column=0,padx=10,pady=5)
        tk.Entry(self.root,textvariable=self.due_date_var).grid(row=1,column=1,padx=10,pady=5)


        #Button for Adding Task
        tk.Button(self.root,text='Add Task',command=self.add_task).grid(row=2,column=0,columnspan=2,pady=10)


        #To Do List Button
        self.listbox=tk.Listbox(self.root,selectmode=tk.SINGLE,height=10,width=40)
        self.listbox.grid(row=3,column=0,columnspan=2,padx=10,pady=5)


        #Task Completed Button
        tk.Button(self.root,text="Mark Task As Completed",command=self.mark_completed).grid(row=4,column=0,columnspan=2,pady=10)


        #Load The To-Do-List
        self.load_todo_list_gui()


    def add_task(self):
        title=self.task_var.get()
        due_date_str=self.due_date_var.get()

        try:
            due_date=datetime.strptime(due_date_str,"%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error","Invalid date format. Please use YYYY-MM-DD")
            return
        
        self.todo_list.append({"title":title,"due_date":due_date,"completed":False})
        self.save_todo_list()
        self.load_todo_list_gui()


    def mark_completed(self):

        selected_index=self.listbox.curselection()

        if not selected_index:
            messagebox.showerror("Error","Please Select a task")
            return
        
        task_index=selected_index[0]
        self.todo_list[task_index]["completed"]=True
        self.save_todo_list()
        self.load_todo_list_gui()


    def load_todo_list(self):
        if tk.messagebox.askyesno("Load To-Do List","Do You Want To Load Your Existing To-Do List?"):
            try:
                with open(TODO_FILE,"r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
        else:
            return []
        

    def load_todo_list_gui(self):
        self.listbox.delete(0,tk.END)

        for task in self.todo_list:
            status="(Completed)" if task["completed"] else "(Pending)"
            color = "green" if task["completed"] else "red"
            self.listbox.insert(tk.END,f"{task['title']}- Due: {task['due_date']} {status}")


    def save_todo_list(self):
        with open(TODO_FILE,"w") as file:
            json.dump(self.todo_list,file)


if __name__=="__main__":
    root=tk.Tk()
    app=TodoApp(root)
    root.mainloop()
