from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#this object of employee repo
emp_db = EmployeeDB()
#thi
emp_auth = EmployeeAuthentication(emp_db)

#this functiobn for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('Enter your name :')
    email = input('Enter your email :')
    password = input('Enter your password :')
    emp_auth.creationEmployee(name,email,password)
    
def employeeLogin():
    print('Employee Login')
