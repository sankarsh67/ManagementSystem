from db_pool.connection import connect, cursor

class EmployeeDB:
    def createEmp(self,name,email,password):
        query = 'insert into user(user_name,user_email,password) value(%s,%s,%s)'
        values = (name,email,password)
        cursor.execute(query,values)
        connect.commit()
        print('Employee created sucessfully')
        
    def searchEmp(self, email):
        query = "SELECT password FROM user WHERE user_email = %s"
        values = email,
        cursor.execute(query, values)   
        data = cursor.fetchone()
        if data is not None :
            return data[0]
        else:
            return
        
    def getAllEmp(self):
        query = 'select *from user where is_employee = %s'
        cursor.execute(query,(1,))
        datas = cursor.fetchall()
        return datas
    
    def modifyEmptoMgr(self):
        query = 'update user set is_manager = %s where id = %s'
        values = (1,id)
        cursor.execute(query,values)
        connect.commit()
        print(f'Employee id with {id} promoted to MANAGER.')