n=int(input("How many omployee data u want to insert?"))

class employee:

    def read(self):
        self.sname=(input("Enter employee name:"))
        self.salary=int(input("Enter Salary:"))
        self.hra=self.salary*10/100
        self.da=self.salary*5/100
        self.net=self.salary+self.hra+self.da
        
    def show(self):
        print(str(self.sname)+"\t"+str(self.salary)+"\t"+str(self.hra)+"\t"+str(self.da)+"\t"+str(self.net) )

    


stdlist=[]

for i in range(n):
    stdlist.append(employee())


for dr in stdlist:
    dr.read();

print("name\tsalary\t hra\t da \t net")

for ds in stdlist:
    ds.show()