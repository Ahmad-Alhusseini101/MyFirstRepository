import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def retrieve():
    accept = termsvar.get()

    if accept == "Accepted":


        name = first_name_entry.get()
        last_name = second_name_entry.get()
        if name and last_name:
            title = nouns.get()
            age = age_spin.get()
            nationality = nationality_spin.get()

            numb_sems = numsemesters_spinbox.get()

            something = num_courses_spin.get()

            registration1 = registrationvar.get()

            



            print("First name: ", name, "Last name: ", last_name)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", something, "# Semesters", numb_sems)
            print("Registration Status", registration1)
            print("----------------------------------------------------------")
        else: 
            tk.messagebox.showwarning(title = "Error", message = "Please Enter Your First and Last Name")
    else:
        tk.messagebox.showwarning(title = "Error", message = "Please Accept the Terms and Conditions")





window = tk.Tk()
window.title("Hello")
frame = tk.Frame(window)
frame.pack()

user_info = tk.LabelFrame(frame, text = "User Information")
user_info.grid(row = 0, column = 0, padx = 20, pady = 20)

first_name = tk.Label(user_info, text = "First Name")
first_name.grid(row = 0, column = 0)
second_name = tk.Label(user_info, text = "Last Name")
second_name.grid(row = 0, column = 1)


first_name_entry = tk.Entry(user_info)
first_name_entry.grid(row = 1, column = 0)
second_name_entry = tk.Entry(user_info)
second_name_entry.grid(row = 1, column = 1)

noun = tk.Label(user_info, text = "Choose your Character")
noun.grid(row = 0, column = 2)
nouns = ttk.Combobox(user_info, values = ["Optimus Prime", "Sigma Boy", "Giga Chad", "Mogger"])
nouns.grid(row = 1, column = 2)

age = tk.Label(user_info, text = "Age")
age.grid(row = 2, column = 0)

age_spin = tk.Spinbox(user_info, from_= 18, to = 100)
age_spin.grid(row = 3, column = 0)

nationality_label = tk.Label(user_info, text = "Nationality")
nationality_label.grid(row = 2, column = 1)

nationality_spin = ttk.Combobox(user_info, values = ["USA", "Mercury", "Ohio", "Nigeria"])
nationality_spin.grid(row = 3, column = 1)

for widget in user_info.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

courses_info = tk.LabelFrame(frame, text = "Courses Information")
courses_info.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

registration = tk.Label(courses_info, text = "Registration Status")
registration.grid(row = 0, column = 0)

registrationvar = tk.StringVar(value = "Not Registered")
registration_check = tk.Checkbutton(courses_info, text = "Currently Regitered", variable = registrationvar, onvalue = "Registered", offvalue = "Not Registered")

registration_check.grid(row = 1, column = 0)

numb_courses = tk.Label(courses_info, text = "Number of Courses")
numb_courses.grid(row = 0, column = 1)

num_courses_spin = tk.Spinbox(courses_info, from_ = 0, to = "infinity")
num_courses_spin.grid(row = 1, column = 1)

numsemesters_label = tk.Label(courses_info, text="Number of Semesters")
numsemesters_spinbox = tk.Spinbox(courses_info, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)



for widget in courses_info.winfo_children():
    widget.grid(padx = 10, pady = 5)


# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

termsvar = tk.StringVar(value = "Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable = termsvar, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row=0, column=0)


button = tk.Button(frame, text="Enter data", command = retrieve)
button.grid(row=3, column=0, sticky = "news", padx = 10, pady = 10)




window.mainloop()