import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def add_task():
    global entry_task
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task():
    global entry_task
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        new_task = entry_task.get()
        if new_task:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")

def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        listbox_tasks.delete(selected_task_index)

def main():
    global entry_task, listbox_tasks
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry('550x550+550+130')

    frame1 = tk.Frame(root)
    
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)

    label_title = tk.Label(frame2, text="TO DO LIST", fg="blue")
    label_font = font.Font(size=30, family='comic sans ms')
    label_title['font'] = label_font
    label_title.grid(pady=(10,10), column=2, columnspan=2)

    entry_task_font = font.Font(size=20,family='comic sans ms')
    entry_task = tk.Entry(frame2, width=30, font=entry_task_font, fg="maroon")
    entry_task.grid(row=2, pady=(20, 10), column=2, padx=(20, 5), columnspan=2)
    frame2.pack()
#######################################
    btn_font = font.Font(size=18)

    button_add = tk.Button(frame3, text='Add', fg='red',command = add_task, height=1, width=5,)
    button_add['font'] = btn_font
    button_add.grid(row=3, pady=(20,10), column=1, padx=(20,5))

    button_update = tk.Button(frame3, text='update', fg='red', command=update_task)
    button_update['font'] = btn_font
    button_update.grid(row=3, pady=(20,10), column=3, padx=(20,5))

    button_delete = tk.Button(frame3,text='delete', fg='red', command=delete_task)
    button_delete['font'] = btn_font
    button_delete.grid(row=3, pady=(20,10), column=2, padx=(20,5))

    frame3.pack()
    
    listbox_tasks_font = font.Font(size=14, family="comic sans ms")  # Adjust the size as needed
    listbox_tasks = tk.Listbox(frame1, height=10, width=30, font=listbox_tasks_font, fg="maroon")
    listbox_tasks.grid(row=4, pady=(20, 10), column=2, padx=(20, 5))
    
    frame1.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
