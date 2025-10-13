from tkinter import *

root = Tk()
root.title("1st GUI with Tkinter")

top = Label(root, text="Please enter your Data", font=("Arial", 25))
firstNameLabel = Label(root, text="First Name", font=("Arial", 20))
box1 = Entry(root)
lastNameLabel = Label(root, text="Last Name", font=("Arial", 20))
box2 = Entry(root)
genderLabel = Label(root, text="Gender", font=("Arial", 20))

gender = IntVar()
maleButton = Radiobutton(
    root, text="Male", variable=gender, value=1, font=("Arial", 20)
)
femaleButton = Radiobutton(
    root, text="Female", variable=gender, value=2, font=("Arial", 20)
)

submitButton = Button(root, text="Submit", width=20, command=root.destroy)

top.pack()
firstNameLabel.pack()
box1.pack()
lastNameLabel.pack()
box2.pack()
genderLabel.pack()
maleButton.pack()
femaleButton.pack()
submitButton.pack()

root.mainloop()
