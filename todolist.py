import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task field cannot be empty!")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg='#E2B79B')  # Light Brown Background

# Function to change cursor style
def change_cursor(event):
    root.config(cursor="plus")

# Entry for new tasks
entry = tk.Entry(root, width=50, font=("Arial", 14), bd=3, relief=tk.GROOVE, justify=tk.CENTER)
entry.pack(padx=20, pady=(20, 10), ipady=10)  # Increased internal padding (ipady)

# Frame for buttons
button_frame = tk.Frame(root, bg='#E2B79B')  # Light Brown Background
button_frame.pack(pady=10)

# Buttons to add and delete tasks
add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg='#FFFFFF', font=("Arial", 12),
                       bd=2, relief=tk.GROOVE, cursor="hand2")  # Hand-shaped cursor
add_button.pack(side=tk.LEFT, padx=10, ipadx=10)  # Increased internal padding (ipadx)
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg='#FFFFFF', font=("Arial", 12),
                          bd=2, relief=tk.GROOVE, cursor="hand2")  # Hand-shaped cursor
delete_button.pack(side=tk.LEFT, padx=10, ipadx=10)  # Increased internal padding (ipadx)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10, bg='#FFFFFF', font=("Arial", 12), bd=3, relief=tk.GROOVE,
                     selectbackground='#E2B79B')  
listbox.pack(padx=20, pady=(10, 20))

# Bind the change_cursor function to the entry field
entry.bind("<Enter>", change_cursor)

# Start the main loop
root.mainloop()
