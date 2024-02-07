import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def add_task():
    task = entry.get()
    priority = priority_var.get()

    if task:
        task_text = f"{task} (Priority: {priority})"
        listbox.insert(tk.END, task_text)
        entry.delete(0, tk.END)
        priority_var.set("Low")  # Reset priority to default after adding a task
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def toggle_task():
    try:
        index = listbox.curselection()
        task_text = listbox.get(index)
        if task_text.startswith("✓ "):
            task_text = task_text[2:]
        else:
            task_text = "✓ " + task_text
        listbox.delete(index)
        listbox.insert(index, task_text)
    except:
        messagebox.showwarning("Warning", "Please select the task you've done.")

window = tk.Tk()
window.title("Customizable To-Do List")
window.configure(bg="thistle")

# Create an entry widget to add tasks
entry = tk.Entry(window, width=60)  # Adjusted the width
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")  # Use grid and sticky option

# Priority Level
priority_var = tk.StringVar(window)
priority_var.set("Low")  # Default priority

# Priority Label and Dropdown using grid
priority_label = tk.Label(window, text="Priority:", font=("Arial", 14))  # Increased font size
priority_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)  # Use grid and sticky option

priority_menu = tk.OptionMenu(window, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)  # Use grid and sticky option

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="violet", height=60)  # Set height for the frame
button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Use grid and sticky option

button_font = Font(family="Arial", size=12, weight="bold")

# an "Add Task" button
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=button_font, width=10)  # Adjusted width
add_button.pack(side=tk.LEFT, padx=5)

# a "Delete Task" button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=button_font, width=10)  # Adjusted width
delete_button.pack(side=tk.LEFT, padx=5)

# a "Done Task" button
toggle_button = tk.Button(button_frame, text="Done Task", command=toggle_task, font=button_font, width=10)  # Adjusted width
toggle_button.pack(side=tk.LEFT, padx=5)

# a listbox to display tasks
listbox = tk.Listbox(window, width=60, height=10)  # Adjusted width and height
listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")  # Use grid and sticky option

# a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=3, column=2, sticky=tk.NS)  # Use grid for the scrollbar

# Link the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

window.mainloop()
