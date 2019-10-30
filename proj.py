class Employee:
    empCount = 0

    def __init__  (self,name):
        self.name= name
        Employee.empCount +=1

    def displayCount(self):
        print("Total employee %d" %Employee.empCount)

    def displayEmployee(self):
        print("name",self.name)

emp1=Employee("xin",23898989)
emp1.displayCount()
emp1.displayEmployee()