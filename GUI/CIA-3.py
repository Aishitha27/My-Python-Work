import tkinter as tk
from tkinter import messagebox

# Create a list of pre-stored books
book_list = [
    "1984 by George Orwell",
    "Franny and Zooey by J.D.Salinger",
    "Harry Potter and the Chamber of Scerets by J.K.Rowling",
    "The Notebook by Nicholas Spark",
    "Metamorphosis by Franz Kafka",
]

# Function to display the selected book
def select_book():
    selected_index = book_listbox.curselection()
    if selected_index:
        selected_book = book_list[selected_index[0]]
        messagebox.showinfo("Selected Book", f"You have selected: {selected_book}")
    else:
        messagebox.showwarning("No Selection", "Please select a book.")

# Create the main window
root = tk.Tk()
root.title("Library App")

# Create labels and entry fields for student details
student_name_label = tk.Label(root, text="Student Name:")
student_name_label.pack()
student_name_entry = tk.Entry(root)
student_name_entry.pack()

student_rollno_label = tk.Label(root, text="Roll Number:")
student_rollno_label.pack()
student_rollno_entry = tk.Entry(root)
student_rollno_entry.pack()

student_department_label = tk.Label(root, text="Department:")
student_department_label.pack()
student_department_entry = tk.Entry(root)
student_department_entry.pack()

# Create a listbox to display available books
book_label = tk.Label(root, text="Available Books:")
book_label.pack()
book_listbox = tk.Listbox(root)
book_listbox.pack()

# Add pre-stored books to the listbox
for book in book_list:
    book_listbox.insert(tk.END, book)

# Create a button to select a book
select_book_button = tk.Button(root, text="Select Book", command=select_book)
select_book_button.pack()

# Function to submit student details
def submit_student_details():
    name = student_name_entry.get()
    rollno = student_rollno_entry.get()
    department = student_department_entry.get()

    selected_index = book_listbox.curselection()
    if selected_index:
        selected_book = book_list[selected_index[0]]
    else:
        selected_book = "No book selected"

    if name and rollno and department:
        # Create a text file to store student details
        with open("student_details.txt", "a") as file:
            file.write(f"Name: {name}, Roll Number: {rollno}, Department: {department}, Book: {selected_book}\n")
        messagebox.showinfo("Student Details", f"Name: {name}\nRoll Number: {rollno}\nDepartment: {department}\nSelected Book: {selected_book}")
    else:
        messagebox.showwarning("Incomplete Details", "Please fill in all fields.")

# Create a button to submit student details
submit_button = tk.Button(root, text="Submit Student Details", command=submit_student_details)
submit_button.pack()

# Function to view the saved student details
def view_student_details():
    try:
        with open("student_details.txt", "r") as file:
            student_details = file.read()
            messagebox.showinfo("Student Details", student_details)
    except FileNotFoundError:
        messagebox.showinfo("No Data", "No student details have been saved yet.")

# Create a button to view the saved student details
view_button = tk.Button(root, text="View Student Details", command=view_student_details)
view_button.pack()

root.mainloop()
