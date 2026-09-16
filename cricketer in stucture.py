n=int(input("How many omployee data u want to insert?"))

class cricketer:

    def read(self):
        self.sname=(input("Enter cricketer name:"))
        self.age=int(input("Enter age:"))
        self.country=(input("Enter country:"))
        self.type=(input("Enter type of player:"))
        self.run=int(input("Enter total run:"))
        self.matches=int(input("Enter total matches:"))
                
    def show(self):
        print(str(self.sname)+"\t"+str(self.age)+"\t"+str(self.country)+"\t"+str(self.country)+"\t"+str(self.type)+"\t"+str(self.run)+"\t"+str(self.matches) )

    


stdlist=[]

for i in range(n):
    stdlist.append(cricketer())


for dr in stdlist:
    dr.read();

print("name\tage\t country\t type  \t run \t matches")

for ds in stdlist:
    ds.show()