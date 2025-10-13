import sqlite3
from tkinter import *
from tkinter import messagebox

# ------------------ Database Setup ------------------
conn = sqlite3.connect("students_gui.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    course TEXT NOT NULL
)
"""
)
conn.commit()
conn.close()


# ------------------ Tkinter GUI ------------------
root = Tk()
root.title("Student Data Entry")
root.geometry("400x450")

# Title
top = Label(root, text="Enter Student Details", font=("Arial", 22, "bold"))
top.pack(pady=15)

# First Name
firstNameLabel = Label(root, text="First Name", font=("Arial", 16))
firstNameLabel.pack()
box1 = Entry(root, font=("Arial", 14))
box1.pack(pady=5)

# Last Name
lastNameLabel = Label(root, text="Last Name", font=("Arial", 16))
lastNameLabel.pack()
box2 = Entry(root, font=("Arial", 14))
box2.pack(pady=5)

# Gender
genderLabel = Label(root, text="Gender", font=("Arial", 16))
genderLabel.pack(pady=5)

gender = StringVar(value="None")
maleButton = Radiobutton(
    root, text="Male", variable=gender, value="Male", font=("Arial", 14)
)
femaleButton = Radiobutton(
    root, text="Female", variable=gender, value="Female", font=("Arial", 14)
)
maleButton.pack()
femaleButton.pack()

# Course
courseLabel = Label(root, text="Course", font=("Arial", 16))
courseLabel.pack(pady=5)

course_var = StringVar(value="Select Course")
courseMenu = OptionMenu(root, course_var, "MCA", "MTECH", "BTECH", "MBA")
courseMenu.config(font=("Arial", 14))
courseMenu.pack(pady=5)


# ------------------ Function to Insert Data ------------------
def submit_data():
    first_name = box1.get().strip()
    last_name = box2.get().strip()
    gender_value = gender.get()
    course_value = course_var.get()

    if (
        first_name == ""
        or last_name == ""
        or gender_value == "None"
        or course_value == "Select Course"
    ):
        messagebox.showwarning("Incomplete Data", "Please fill all fields!")
        return

    # Insert into SQLite database
    conn = sqlite3.connect("students_gui.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (first_name, last_name, gender, course) VALUES (?, ?, ?, ?)",
        (first_name, last_name, gender_value, course_value),
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student data saved successfully!")

    # Clear input fields
    box1.delete(0, END)
    box2.delete(0, END)
    gender.set("None")
    course_var.set("Select Course")


# Submit Button
submitButton = Button(
    root, text="Submit", font=("Arial", 16), width=15, command=submit_data
)
submitButton.pack(pady=20)

# Exit Button
exitButton = Button(
    root, text="Exit", font=("Arial", 14), width=10, command=root.destroy
)
exitButton.pack(pady=10)

root.mainloop()
