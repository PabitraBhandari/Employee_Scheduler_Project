import java.util.*;

class Employee {
    String name;
    List<String> preferences;
    Set<String> assignedDays;
    int workDays;

    public Employee(String name, List<String> preferences) {
        this.name = name;
        this.preferences = preferences;
        this.assignedDays = new HashSet<>();
        this.workDays = 0;
    }
}

public class ShiftScheduler {
    private static final String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    private static final Map<String, String> SHIFT_MAP = Map.of("M", "Morning", "Af", "Afternoon", "Ev", "Evening");
    private static final String[] SHIFTS = {"M", "Af", "Ev"};
    private static final Map<String, Map<String, List<String>>> schedule = new HashMap<>();
    private static final List<Employee> employees = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        for (String day : DAYS) {
            schedule.put(day, new HashMap<>());
            for (String shift : SHIFTS) {
                schedule.get(day).put(shift, new ArrayList<>());
            }
        }
        
        System.out.println("Enter the number of employees:");
        int numEmployees = scanner.nextInt();
        scanner.nextLine();
        
        for (int i = 0; i < numEmployees; i++) {
            System.out.println("Enter employee name:");
            String name = scanner.nextLine();
            
            System.out.println("Enter preferred shifts (comma separated: M for Morning, Af for Afternoon, Ev for Evening):");
            String[] shiftPreferences = scanner.nextLine().toUpperCase().split(",");
            
            employees.add(new Employee(name, Arrays.asList(shiftPreferences)));
        }
        
        assignShifts();
        fillUnfilledShifts();
        displaySchedule();
        scanner.close();
    }

    private static void assignShifts() {
        Collections.shuffle(employees);
        Map<String, Integer> workCount = new HashMap<>();
        for (Employee emp : employees) {
            workCount.put(emp.name, 0);
        }
        
        for (int i = 0; i < DAYS.length; i++) {
            String day = DAYS[i];
            Set<String> assignedToday = new HashSet<>();
            
            for (String shift : SHIFTS) {
                List<String> assigned = new ArrayList<>();
                List<Employee> firstChoice = new ArrayList<>();
                List<Employee> secondChoice = new ArrayList<>();
                List<Employee> available = new ArrayList<>();
                
                for (Employee emp : employees) {
                    if (workCount.get(emp.name) < 5 && !emp.assignedDays.contains(day)) {
                        if (emp.preferences.get(0).equals(shift)) {
                            firstChoice.add(emp);
                        } else if (emp.preferences.contains(shift)) {
                            secondChoice.add(emp);
                        } else {
                            available.add(emp);
                        }
                    }
                }
                
                Collections.shuffle(firstChoice);
                Collections.shuffle(secondChoice);
                Collections.shuffle(available);
                
                while (assigned.size() < 2 && !firstChoice.isEmpty()) {
                    Employee emp = firstChoice.remove(0);
                    assigned.add(emp.name);
                    emp.assignedDays.add(day);
                    workCount.put(emp.name, workCount.get(emp.name) + 1);
                }
                
                while (assigned.size() < 2 && !secondChoice.isEmpty()) {
                    Employee emp = secondChoice.remove(0);
                    assigned.add(emp.name);
                    emp.assignedDays.add(day);
                    workCount.put(emp.name, workCount.get(emp.name) + 1);
                }
                
                while (assigned.size() < 2 && !available.isEmpty()) {
                    Employee emp = available.remove(0);
                    assigned.add(emp.name);
                    emp.assignedDays.add(day);
                    workCount.put(emp.name, workCount.get(emp.name) + 1);
                }
                
                schedule.get(day).put(shift, assigned);
            }
        }
    }
    
    private static void fillUnfilledShifts() {
        for (String day : DAYS) {
            for (String shift : SHIFTS) {
                if (schedule.get(day).get(shift).size() < 2) {
                    List<Employee> availableEmployees = new ArrayList<>();
                    for (Employee emp : employees) {
                        if (emp.workDays < 5 && !emp.assignedDays.contains(day)) {
                            availableEmployees.add(emp);
                        }
                    }
                    
                    availableEmployees.removeIf(emp -> emp.workDays >= 5);
                    Collections.shuffle(availableEmployees);
                    
                    while (schedule.get(day).get(shift).size() < 2 && !availableEmployees.isEmpty()) {
                        Employee emp = availableEmployees.remove(0);
                        schedule.get(day).get(shift).add(emp.name);
                        emp.assignedDays.add(day);
                        emp.workDays++;
                    }
                }
            }
        }
    }
    
    private static void displaySchedule() {
        boolean hasUnfilledShifts = false;
        System.out.println("\nFinal Employee Schedule:");
        for (String day : DAYS) {
            System.out.println(day + ":");
            for (String shift : SHIFTS) {
                String fullShiftName = SHIFT_MAP.get(shift);
                if (schedule.get(day).get(shift).isEmpty()) {
                    System.out.println("  " + fullShiftName + ": No employees assigned");
                    hasUnfilledShifts = true;
                } else {
                    System.out.println("  " + fullShiftName + ": " + String.join(", ", schedule.get(day).get(shift)));
                }
            }
            System.out.println("-");
        }
        if (hasUnfilledShifts) {
            System.out.println("\n⚠ Warning: Not enough employees to fill all shifts!");
        }
    }
}
