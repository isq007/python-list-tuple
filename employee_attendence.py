employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]

attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

def mark_attendance(employee_id, date, status):
    """Marks attendance for an employee."""
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")

def search_attendance(employee_id):
    """Searches for attendance records by employee ID."""
    print(f"Searching Attendance for Employee ID {employee_id}:")
    for record in attendance_records:
        if record[0] == employee_id:
            print(f"Date: {record[1]}, Status: {record[2]}")

def attendance_summary():
    """Displays the summary of attendance percentages for all employees."""
    attendance_count = {emp[0]: {'Present': 0, 'Total': 0} for emp in employees}
    
    for record in attendance_records:
        emp_id, _, status = record
        attendance_count[emp_id]['Total'] += 1
        if status == "Present":
            attendance_count[emp_id]['Present'] += 1
    
    print("\nAttendance Summary:")
    for emp_id, stats in attendance_count.items():
        name = next(emp[1] for emp in employees if emp[0] == emp_id)
        percentage = (stats['Present'] / stats['Total']) * 100 if stats['Total'] > 0 else 0
        print(f"{name}: {percentage:.2f}% Present")

# Example usage
mark_attendance(102, "2025-03-02", "Present")
mark_attendance(103, "2025-03-02", "Absent")
search_attendance(102)
attendance_summary()
