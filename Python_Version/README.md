# Employee Shift Scheduler (Python GUI)

## 📌 Project Overview
This is a **Graphical User Interface (GUI) application** for managing employee shift schedules. Employees can choose their preferred shifts, and the system will assign shifts while ensuring:
- **No employee works more than one shift per day.**
- **Each employee can work a maximum of 5 days per week.**
- **Every shift must have at least 2 employees.**
- **Conflicts are resolved if shifts are full.**

This implementation is done using **Python (Tkinter)**.

---

## 🛠️ Installation & Setup
### **1️⃣ Requirements**
Ensure you have **Python 3.x** installed. You can check your version with:
```bash
python --version
```

### **2️⃣ Install Dependencies**
Install required dependencies using:
```bash
pip install tk
```

---

## 🚀 Running the Application
Navigate to the project folder and run:
```bash
python3 EmployeeScheduler.py
```
This will launch the GUI where you can:
- **Enter employee names and preferred shifts**
- **View and generate shift schedules**
- **Export or print the final schedule**

---

## 🔹 Features Implemented
✅ **GUI-based employee entry**  
✅ **Shift preferences selection using dropdowns**  
✅ **Dynamic schedule generation with conflict resolution**  
✅ **Save functionality for exporting schedules**  
✅ **Error handling & alerts for incorrect inputs**

---

## 📌 How It Works
1. **User enters employee name and selects two preferred shifts (Morning, Afternoon, or Evening).**
2. **System ensures employees are assigned based on their preferences while following the scheduling rules.**
3. **Final schedule is displayed, ensuring fairness in work distribution.**
4. **Users can export or print the generated schedule.**

---

## 🔹 Known Limitations
- The GUI does not currently support **editing employee preferences after entry.**
- If there are **too few employees**, some shifts may remain unfilled.
