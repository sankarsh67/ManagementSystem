from getpass4 import getpass
from dotenv import load_dotenv
import os
from services.auth import AdminAuthentication
from repositories.employee_repo import EmployeeDB

emp_db = EmployeeDB()
admin_auth = AdminAuthentication(emp_db)

load_dotenv()

def adminMenu():
    print('welcome back Admin')

def adminLogin():
    password = getpass("enter your password:") 
    if password == os.getenv('ADMIN_PW'):
        adminMainMenu()
    else:
        print('Password is incorrect try to login again')
        adminLogin()

def adminMainMenu():
    print('Welcome back ADMIN')
    choice = int(input('''
____________________________________________________
|Press 1 for all employee data                      |                            
|Press 2 for all manager data                       |
|Press 3 for promote employee to manager            |
|Press 4 for assign project to manager              |
|Press 5 for see the manager request for employee   |
|Press 6 for assign employee to manager             |
|Press 7 for check the update of the porject        |
|Press 8 for logout                                 |

enter your choice :'''))
    
    if choice == 1 :
        emp_datas = admin_auth.db.getAllEmp()
        for emp_data in emp_datas:
            print(f'''
___________________________________
employee id : {emp_data[0]}
employee name : {emp_data[1]}
employee email : {emp_data[2]}
employee manager id : {emp_data[4]}
___________________________________''')
            
    elif choice == 2:
        pass
    elif choice == 3:
        id = int(input('Enter the emplooyee id to promote to manager :'))
        if id in [i[0] for i in admin_auth.db.getAllEmp()]:
            admin_auth.db.modifyEmptoMgr()
        else :
            print(f'employee with id {id} is not present')
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    else:
        print('Enter correct Option !')
        adminMainMenu()
            