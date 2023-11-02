
from tkinter import *
from tkinter import messagebox

def submit_feedback():

    # Get the values from the entries
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    branch = branch_entry.get()
    year = year_entry.get()
    comments = comments_text.get()

    # Get the values from the radio buttons
    radio_var_1 = radio_value_1.get()
    radio_var_2 = radio_value_2.get()
    radio_var_3 = radio_value_3.get()
    radio_var_4 = radio_value_4.get()
    radio_var_5 = radio_value_5.get()


    
    # Save the values to a file or database for analysis
    with open("feedback.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Roll No.: {roll_no}\n")
        f.write(f"Branch: {branch}\n")
        f.write(f"Year: {year}\n")
        f.write(f"Anirban Bhowal: {radio_var_1}\n")
        f.write(f"Ramakrishna Bandi: {radio_var_2}\n")
        f.write(f"Rohit Chaurasiya: {radio_var_3}\n")
        f.write(f"Debanjan Das: {radio_var_4}\n")
        f.write(f"Kavita Jaiswal: {radio_var_5}\n")
        f.write(f"Comments: {comments}\n")

    # Show a message box to confirm the feedback has been submitted
    messagebox.showinfo("Feedback", "Thank you for submitting your feedback!")



    

# Create the main window
root = Tk()
root.title("Academic Feedback System")

# Create labels and entries for the student details
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)

name_entry = Entry(root)
name_entry.grid(row=0, column=1)

roll_no_label = Label(root, text="Roll No.:")
roll_no_label.grid(row=1, column=0)

roll_no_entry = Entry(root)
roll_no_entry.grid(row=1, column=1)

branch_label = Label(root, text="Branch:")
branch_label.grid(row=2, column=0)

branch_entry = Entry(root)
branch_entry.grid(row=2, column=1)

year_label = Label(root, text="Year:")
year_label.grid(row=3, column=0)

year_entry = Entry(root)
year_entry.grid(row=3, column=1)

# Create variables to store the selected radio button values
radio_value_1 = StringVar()
radio_value_2 = StringVar()
radio_value_3 = StringVar()
radio_value_4 = StringVar()
radio_value_5 = StringVar()

# Create labels for the faculty names
faculty_label_1 = Label(root, text="Anirban Bhowal:")
faculty_label_1.grid(row=4, column=0)

faculty_label_2 = Label(root, text="Ramakrishna Bandi:")
faculty_label_2.grid(row=5, column=0)

faculty_label_3 = Label(root, text="Rohit Chaurasiya:")
faculty_label_3.grid(row=6, column=0)

faculty_label_4 = Label(root, text="Debanjan Das:")
faculty_label_4.grid(row=7,column=0)

faculty_label_5 = Label(root, text="Kavita Jaiswal")
faculty_label_5.grid(row=8,column=0)

# Create radio buttons to rate the faculty
rating_1_1 = Radiobutton(root, text="Very Poor", variable=radio_value_1, value="Very Poor")
rating_1_1.grid(row=4, column=2)

rating_1_2 = Radiobutton(root, text="Poor", variable=radio_value_1, value="Poor")
rating_1_2.grid(row=4, column=3)

rating_1_3 = Radiobutton(root, text="Average", variable=radio_value_1, value="Average")
rating_1_3.grid(row=4, column=4)

rating_1_4 = Radiobutton(root, text="Good", variable=radio_value_1, value="Good")
rating_1_4.grid(row=4, column=5)

rating_1_5 = Radiobutton(root, text="Excellent", variable=radio_value_1, value="Excellent")
rating_1_5.grid(row=4, column=6)

rating_2_1 = Radiobutton(root, text="Very Poor", variable=radio_value_2, value="Very Poor")
rating_2_1.grid(row=5, column=2)

rating_2_2 = Radiobutton(root, text="Poor", variable=radio_value_2, value="Poor")
rating_2_2.grid(row=5, column=3)

rating_2_3 = Radiobutton(root, text="Average", variable=radio_value_2, value="Average")
rating_2_3.grid(row=5, column=4)

rating_2_4 = Radiobutton(root, text="Good", variable=radio_value_2, value="Good")
rating_2_4.grid(row=5, column=5)

rating_2_5 = Radiobutton(root, text="Excellent", variable=radio_value_2, value="Excellent")
rating_2_5.grid(row=5, column=6)

rating_3_1 = Radiobutton(root, text="Very Poor", variable=radio_value_3, value="Very Poor")
rating_3_1.grid(row=6, column=2)

rating_3_2 = Radiobutton(root, text="Poor", variable=radio_value_3, value="Poor")
rating_3_2.grid(row=6, column=3)

rating_3_3 = Radiobutton(root, text="Average", variable=radio_value_3, value="Average")
rating_3_3.grid(row=6, column=4)

rating_3_4 = Radiobutton(root, text="Good", variable=radio_value_3, value="Good")
rating_3_4.grid(row=6, column=5)

rating_3_5 = Radiobutton(root, text="Excellent", variable=radio_value_3, value="Excellent")
rating_3_5.grid(row=6, column=6)

rating_4_1 = Radiobutton(root, text="Very poor", variable=radio_value_4, value="Very Poor")
rating_4_1.grid(row=7, column=2)

rating_4_2 = Radiobutton(root, text="Poor", variable=radio_value_4, value="Poor")
rating_4_2.grid(row=7, column=3)

rating_4_3 = Radiobutton(root, text="Average", variable=radio_value_4, value="Average")
rating_4_3.grid(row=7, column=4)

rating_4_4 = Radiobutton(root, text="Good", variable=radio_value_4, value="Good")
rating_4_4.grid(row=7, column=5)

rating_4_5 = Radiobutton(root, text="Excellent", variable=radio_value_4, value="Excellent")
rating_4_5.grid(row=7, column=6)

rating_5_1 = Radiobutton(root, text="Very Poor", variable=radio_value_5, value="Very Poor")
rating_5_1.grid(row=8, column=2)

rating_5_2 = Radiobutton(root, text="Poor", variable=radio_value_5, value="Poor")
rating_5_2.grid(row=8, column=3)

rating_5_3 = Radiobutton(root, text="Average", variable=radio_value_5, value="Average")
rating_5_3.grid(row=8, column=4)

rating_5_4 = Radiobutton(root, text="Good", variable=radio_value_5, value="Good")
rating_5_4.grid(row=8, column=5)

rating_5_5 = Radiobutton(root, text="Excellent", variable=radio_value_5, value="Excellent")
rating_5_5.grid(row=8, column=6)

comment_label = Label(root, text = "Comments")
comment_label.grid(row = 10, column = 0)

comments_text = Entry(root)
comments_text.grid(row=10, column=1)


# Create submit button
submit_button = Button(root, text="Submit", command = submit_feedback)
submit_button.grid(row=12, column=2)


root.mainloop()