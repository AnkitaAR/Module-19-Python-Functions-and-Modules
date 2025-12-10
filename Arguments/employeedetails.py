def display_employee_details(employee):
    """
    Displays the details of an employee.

    Args:
        employee (dict): A dictionary containing employee details with keys
                         'name', 'id', 'position', and 'department'.
    """
    print("Employee Details:")
    print(f"Name: {employee.get('name', 'N/A')}")
    print(f"ID: {employee.get('id', 'N/A')}")
    print(f"Position: {employee.get('position', 'N/A')}")
    print(f"Department: {employee.get('department', 'N/A')}")
empname=input("Enter employee name:")
empid=input("Enter employee id:")
emppos=input("Enter employee position:")
empdept=input("Enter employee department:")
employee_info = {
    'name': empname,
    'id': empid,
    'position': emppos,
    'department': empdept
}
display_employee_details(employee_info)
