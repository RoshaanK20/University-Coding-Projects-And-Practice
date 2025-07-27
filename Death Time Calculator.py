import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birth_date_str = birth_entry.get()
    death_date_str = death_entry.get()

    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
        death_date = datetime.strptime(death_date_str, "%d-%m-%Y")
        age = death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))

        days_lived = (death_date - birth_date).days
        hours_lived = days_lived * 24

        age_label.config(text=f"Age: {age}")
        days_label.config(text=f"Days Lived: {days_lived}")
        hours_label.config(text=f"Hours Lived: {hours_lived}")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use DD-MM-YYY.")

# Create the main window
window = tk.Tk()
window.title("Age Calculator")
window.geometry('400x300')
window.resizable (False,False)

# Create labels and entries for birth and death dates
birth_label = tk.Label(window, text="Enter Birth Date (DD-MM-YYY):")
birth_label.pack()
birth_entry = tk.Entry(window)
birth_entry.pack()

death_label = tk.Label(window, text="Enter Death Date (DD-MM-YYY):")
death_label.pack()
death_entry = tk.Entry(window)
death_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_age)
calculate_button.pack()

# Labels to display the calculated age, days lived, and hours lived
age_label = tk.Label(window, text="Age:")
age_label.pack()

days_label = tk.Label(window, text="Days Lived:")
days_label.pack()

hours_label = tk.Label(window, text="Hours Lived:")
hours_label.pack()

window.mainloop()
