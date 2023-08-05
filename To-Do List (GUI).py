import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

def add_task():
    task = entry.get()
    due_date = calendar.get()
    if task and due_date:
        listbox.insert(tk.END, f"{task} (Due: {due_date})")
        entry.delete(0, tk.END)
        calendar.set_date("")  # Clear the calendar after adding a task
    else:
        messagebox.showwarning("Warning", "Please enter a task and select a due date.")

def delete_task():
    try:
        selected_indices = listbox.curselection()
        for index in reversed(selected_indices):  # Delete in reverse to handle shifting indices
            listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        current_task = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, current_task.split(" (Due:")[0])
        date_str = current_task.split("(Due: ")[1][:-1]
        calendar.set_date(date_str)
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def toggle_selection(event):
    try:
        x, y, width, height = listbox.bbox(listbox.nearest(event.y))
        if event.x > x + width - 20:  # Check if click is in the right corner of the task
            selected_index = listbox.nearest(event.y)
            is_selected = listbox.selection_includes(selected_index)
            if is_selected:
                listbox.selection_clear(selected_index)
            else:
                listbox.selection_set(selected_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x670")
root.configure(bg="#1f1f1f")  # Set dark background color

# Create listbox to display tasks with light yellow background
listbox = tk.Listbox(root, bg="#FFFFE0", fg="#000000", font="Helvetica 14 bold", selectbackground="#2c2c2c", selectforeground="#ffffff", bd=0, selectmode=tk.MULTIPLE)
listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
listbox.bind("<<ListboxSelect>>", toggle_selection)

# Create entry widget to add/edit tasks
entry = tk.Entry(root, bg="#2c2c2c", fg="#ffffff", font="Helvetica 14", bd=0)
entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Add a calendar using tkcalendar.DateEntry with white text on black background
calendar = DateEntry(root, bg="#000000", fg="#ffffff", font="Helvetica 14", bd=0, selectbackground="#444444", selectforeground="#ffffff", date_pattern="yyyy-mm-dd")
calendar.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Create buttons with rounded corners
add_button = tk.Button(root, text="Add Task", bg="#007BFF", fg="#ffffff", font="Helvetica 14 bold", bd=0, command=add_task, relief=tk.RAISED, padx=15, pady=5, cursor="hand2")
add_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

delete_button = tk.Button(root, text="Delete Task", bg="#DC3545", fg="#ffffff", font="Helvetica 14 bold", bd=0, command=delete_task, relief=tk.RAISED, padx=15, pady=5, cursor="hand2")
delete_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

edit_button = tk.Button(root, text="Edit Task", bg="#28a745", fg="#ffffff", font="Helvetica 14 bold", bd=0, command=edit_task, relief=tk.RAISED, padx=15, pady=5, cursor="hand2")
edit_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Start the main loop
root.mainloop()
