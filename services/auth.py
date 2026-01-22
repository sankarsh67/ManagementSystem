#module for login and signup for employee and admin

class AdminAuthentication:
    def adminLogin(self):
        pass

class EmployeeAuthentication:
    def __init__(self,db):
        self.db = db
        
    def creationEmployee(self,e_name,e_email,password):
        self.e_name = e_name
        self.e_email = e_email
        self.password = password
        self.db.createEmp(self.e_name,self.e_email,self.password)