import random
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from collections import defaultdict
import csv

# Define shifts
SHIFTS = ['Morning', 'Afternoon', 'Evening']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Employee data storage
class Employee:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences  # List of preferred shifts
        self.assigned_shifts = set()  # Store as a set to prevent duplicate day assignments
        self.days_worked = 0

# Initialize schedule
schedule = {day: {shift: [] for shift in SHIFTS} for day in DAYS}
employees = []

def assign_shifts():
    random.shuffle(employees)  # Shuffle for fairness
    assigned_days = {emp.name: 0 for emp in employees}
    shift_rotation = {shift: [] for shift in SHIFTS}
    
    for emp in employees:
        for shift in emp.preferences:
            shift_rotation[shift].append(emp)
    
    # Assign employees to weekend shifts first before filling weekdays
    for day in ['Saturday', 'Sunday']:
        available_employees = [emp for emp in employees if emp.days_worked < 5]
        assigned_today = set()
        
        for shift in SHIFTS:
            assigned = []
            preferred = [emp for emp in shift_rotation[shift] if emp in available_employees and emp.name not in assigned_today]
            
            while len(assigned) < 2 and available_employees:
                if preferred:
                    emp = preferred.pop(0)
                else:
                    emp = random.choice(available_employees) if available_employees else None
                
                if emp and emp.name not in assigned_today and emp.days_worked < 5 and assigned_days[emp.name] < 5:
                    assigned.append(emp)
                    emp.assigned_shifts.add(day)
                    emp.days_worked += 1
                    assigned_days[emp.name] += 1
                    assigned_today.add(emp.name)
                    available_employees.remove(emp)
            
            schedule[day][shift] = [emp.name for emp in assigned]
    
    # Assign shifts for Monday–Friday with proper rotation
    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):
        available_employees = [emp for emp in employees if emp.days_worked < 5]
        assigned_today = set()
        
        for shift in SHIFTS:
            assigned = []
            preferred = [emp for emp in shift_rotation[shift] if emp in available_employees and emp.name not in assigned_today]
            
            while len(assigned) < 2 and available_employees:
                if preferred:
                    emp = preferred.pop(i % len(preferred)) if preferred else None
                else:
                    emp = random.choice(available_employees) if available_employees else None
                
                if emp and emp.name not in assigned_today and emp.days_worked < 5 and assigned_days[emp.name] < 5:
                    assigned.append(emp)
                    emp.assigned_shifts.add(day)
                    emp.days_worked += 1
                    assigned_days[emp.name] += 1
                    assigned_today.add(emp.name)
                    available_employees.remove(emp)
            
            schedule[day][shift] = [emp.name for emp in assigned]
    
    fill_underfilled_shifts()
    debug_check_schedule()

def fill_underfilled_shifts():
    for day, shifts in schedule.items():
        for shift, assigned in shifts.items():
            if len(assigned) < 2:
                available_employees = [emp for emp in employees if emp.days_worked < 5 and emp.name not in assigned]
                while len(assigned) < 2 and available_employees:
                    emp = random.choice(available_employees)
                    assigned.append(emp.name)
                    emp.assigned_shifts.add(day)
                    emp.days_worked += 1
                    available_employees.remove(emp)

def debug_check_schedule():
    missing_shifts = []
    for day, shifts in schedule.items():
        for shift, employees in shifts.items():
            if len(employees) < 2:
                missing_shifts.append(f"{day} - {shift}: {', '.join(employees) if employees else 'No employees assigned'}")
    
    if missing_shifts:
        print("\nDEBUG: Unfilled Shifts Detected")
        for shift in missing_shifts:
            print(shift)
    else:
        print("\nDEBUG: All shifts are properly filled!")

def add_employee():
    name = name_entry.get()
    pref1 = shift_var1.get()
    pref2 = shift_var2.get()
    if not name or not pref1 or not pref2:
        messagebox.showerror("Error", "Please enter a name and select two shift preferences.")
        return
    if any(emp.name == name for emp in employees):
        messagebox.showerror("Error", "Employee already exists!")
        return
    preferences = [pref1, pref2] if pref1 != pref2 else [pref1]
    employees.append(Employee(name, preferences))
    update_employee_list()
    name_entry.delete(0, tk.END)
    shift_var1.set("")
    shift_var2.set("")

def update_employee_list():
    employee_listbox.delete(0, tk.END)
    for emp in employees:
        employee_listbox.insert(tk.END, f"{emp.name}: {', '.join(emp.preferences)}")

def gui_generate_schedule():
    assign_shifts()
    print_schedule()

def print_schedule():
    schedule_text.delete(1.0, tk.END)
    for day, shifts in schedule.items():
        schedule_text.insert(tk.END, f"{day}:\n")
        for shift, employees in shifts.items():
            schedule_text.insert(tk.END, f"  {shift}: {', '.join(employees) if employees else 'No employees assigned'}\n")
        schedule_text.insert(tk.END, "-\n")

def save_schedule():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for day, shifts in schedule.items():
                file.write(f"{day}:\n")
                for shift, employees in shifts.items():
                    file.write(f"  {shift}: {', '.join(employees) if employees else 'No employees assigned'}\n")
                file.write("-\n")
        messagebox.showinfo("Save Success", f"Schedule saved as {file_path}")

# GUI Setup
root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("1000x650")

# Main Container
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Left Section (Inputs & Employee List)
left_frame = tk.Frame(main_frame, padx=20, pady=20)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tk.Label(left_frame, text="Employee Name:").pack()
name_entry = tk.Entry(left_frame)
name_entry.pack()

tk.Label(left_frame, text="Preferred Shift 1:").pack()
shift_var1 = tk.StringVar()
shift_dropdown1 = ttk.Combobox(left_frame, textvariable=shift_var1, values=SHIFTS)
shift_dropdown1.pack()

tk.Label(left_frame, text="Preferred Shift 2:").pack()
shift_var2 = tk.StringVar()
shift_dropdown2 = ttk.Combobox(left_frame, textvariable=shift_var2, values=SHIFTS)
shift_dropdown2.pack()

tk.Button(left_frame, text="Add Employee", command=add_employee).pack(pady=5)

tk.Label(left_frame, text="Employee List:").pack()
employee_listbox = tk.Listbox(left_frame, height=10, width=40)
employee_listbox.pack()

tk.Button(left_frame, text="Generate Schedule", command=gui_generate_schedule).pack(pady=10)

# Right Section (Schedule Output)
right_frame = tk.Frame(main_frame, padx=20, pady=20)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(right_frame, text="Generated Schedule:").pack()
schedule_text = tk.Text(right_frame, height=37, width=60)
schedule_text.pack()

tk.Button(right_frame, text="Save Schedule", command=save_schedule).pack(pady=10)

root.mainloop()
