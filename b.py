import tkinter as tk
from tkinter import messagebox

'''                         Main App class               '''

class TaskManager:
    def init(self,root):
        self.root=root
        self.root.title("Task Manager - GUI Project")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.tasks = []

        self.create_ui()

# UI Layout
def create_ui(self):
        title = tk.Lable(self.root, text="Task Manager", )
        )