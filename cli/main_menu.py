from cli.employee_menu import employeeSignup

def menu():
    while True:
        print('''Welcome
Press 1 for admin login 
Press 2 for employee signup
Press 3 for employee login''')
        choice = int(input('Enter your option :'))
        if choice == 1:
            pass
        elif choice == 2:
            employeeSignup()
        elif choice == 3:
            pass
        else:
            print('Enter a valid number!!')
        