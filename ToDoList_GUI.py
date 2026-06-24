import customtkinter as ctk
from tkinter import messagebox
import json
import os

SAVE_FILE = 'Tasks.json'

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

def load_tasks():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as file:
                task_list = json.load(file)
                for task in task_list:
                    task_textbox.insert('end', task+'\n')
        except:
            print('Starting fresh.')

def save_task():
    raw_text = task_textbox.get('1.0', 'end-1c').strip()
    if raw_text == '':
        all_tasks = []
    else:
        all_tasks = raw_text.split('\n')

    with open(SAVE_FILE, 'w') as file:
        json.dump(all_tasks, file, indent=4)


def add_task():
    task_text = task_entry.get().strip().title()
    if task_text != "":
        task_textbox.insert("end", task_text + "\n")
        task_entry.delete(0, "end")
        save_task()
    else:
        messagebox.showwarning("Warning", "You must type a task")

def clear_all():
    task_textbox.delete('1.0','end')
    save_task()

root = ctk.CTk()
root.title('To Do List')
root.geometry('400x500')

title_label = ctk.CTkLabel(root, text='My Tasks', font=('Arial', 24, 'bold'))
title_label.pack(pady=20)

task_entry = ctk.CTkEntry(root, placeholder_text='What needs to be done?',width=300, height=40, font=('Arial', 14))
task_entry.pack(pady=10)

add_button = ctk.CTkButton(root, text='Add Task', width=200,height=35,font=('Arial',13,'bold'),command=add_task)
add_button.pack(pady=5)

task_textbox = ctk.CTkTextbox(root, width=320, height=220, font=('Arial', 14),corner_radius=10)
task_textbox.pack(pady=15)

clear_button = ctk.CTkButton(root, text='Clear', width=200,height=35, fg_color='#D9534F', hover_color='#C9302C',font=('Arial',13,'bold'),command=clear_all)
clear_button.pack(pady=5)

load_tasks()

root.mainloop()
