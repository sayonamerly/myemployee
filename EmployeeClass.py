########### Employee class with attributes and GetEmployee Function###############


class Employee:                     
    def __init__(self,EmployeeId,EmployeeName,EmployeeLocation,EmployeeSalary): ############# Constructor of the class
        self.EmployeeId = EmployeeId
        self.EmployeeName = EmployeeName
        self.EmployeeLocation = EmployeeLocation
        self.EmployeeSalary = EmployeeSalary

    def GetEmployee(self):           ########## Method to get employee details
        print("--------------Employee Details----------")
        print("Employee ID :", self.EmployeeId)
        print("Employee Name :",self.EmployeeName)
        print("Employee Location :",self.EmployeeLocation)
        print("Employee Salary :",self.EmployeeSalary)