a=int(input("enter the value for a="))
b=int(input("enter the value for b="))
c=int(input("enter the value for c="))
d=int(input("enter the value for d="))
e=int(input("enter the value for e="))

t=a+b+c+d+e
print("sum=",t)

avg=t/5
print("avg marks=",avg)


if avg>=70:
    print("Grade=A")

elif avg>=60:
    print("Grade=B")

elif avg>=50:
    print("Grade=C")

elif avg>=35:
    print("Grade=D")

else:
    print("Fail")