n=int(input("How many customer data u want to insert?"))

class customer:

    def read(self):
        self.sname=(input("Enter customer name:"))
    
        self.product=(input("Enter product name :"))
        self.price=int(input("Enter product price :"))
        self.qty=int(input("Enter product QTY :"))
        self.total=self.price*self.qty
    def read2(self):
        if self.total>=1500:
            self.di=self.total*.15
    
        elif self.total>=1000:
            self.di=self.total*.10
    
        elif self.total>=500:
            self.di=self.total*.5
    
        elif self.total<500:
            self.di=self.total*0
    
        ne=self.total-self.di
        
        self.ne=self.total-self.di

        
    def show(self):
        print(str(self.sname)+"\t"+str(self.product)+"\t"+str(self.price)+"\t"+str(self.qty)+"\t"+str(self.total)+"\t"+str(self.di)+"\t"+str(self.ne) )

    


stdlist=[]

for i in range(n):
    stdlist.append(customer())


for dr in stdlist:
    dr.read();
    dr.read2();
    


print("cname  product  price  QTY     total   di    net")

for ds in stdlist:
    ds.show()