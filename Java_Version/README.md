# Employee Shift Scheduler (Java Terminal)

## 📌 Project Overview
This is a **terminal-based employee shift scheduling program** implemented in **Java**. Employees choose their preferred shifts, and the system automatically assigns them while ensuring:
- **No employee works more than one shift per day.**
- **Each employee can work a maximum of 5 days per week.**
- **Every shift must have at least 2 employees.**
- **Conflicts are resolved if shifts are full.**

---

## 🛠️ Installation & Setup
### **1️⃣ Requirements**
Ensure you have **Java 17+ or OpenJDK installed**. You can check your version with:
```bash
java --version
```
If Java is not installed, install it via Homebrew (Mac) or package managers like `apt` (Linux) or download from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html).

### **2️⃣ Compile the Java Program**
Navigate to the project folder and compile the code:
```bash
javac ShiftScheduler.java
```

### **3️⃣ Run the Program**
After compiling, execute the program:
```bash
java ShiftScheduler
```

---

## 📌 Features Implemented
✅ **Text-based employee entry**  
✅ **Shift preferences selection**  
✅ **Automated shift assignment with fairness**  
✅ **Dynamic conflict resolution**  
✅ **Warning system for unfilled shifts**  

---

## 🚀 How It Works
1. **User enters the number of employees.**
2. **For each employee, they provide their name and two preferred shifts (Morning, Afternoon, or Evening).**
3. **The system schedules shifts while following work limits and resolving conflicts.**
4. **The final weekly schedule is printed in an easy-to-read format.**

---

## 📸 Sample Output
```
Enter the number of employees:
6
Enter employee name:
Alice
Enter preferred shifts (comma separated: M for Morning, Af for Afternoon, Ev for Evening):
M, Af
...

Final Employee Schedule:
Monday:
  Morning: Alice, Henry
  Afternoon: Ivy, Bob
  Evening: Charlie, David
-
Tuesday:
  Morning: Alice, Emma
  Afternoon: Bob, Grace
  Evening: David, Frank
-
```

---

## 🔹 Known Limitations
- Currently, shift preferences **cannot be changed after entry.**
- If **too few employees are available**, some shifts may remain unfilled.
- Does not include **GUI or database storage** (text-based output only).
