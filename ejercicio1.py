#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1 = 0
num2 = 0

num1=(int)(input("Dime un número "))
num2=(int)(input("Dime otro número "))

if(num1<num2):
    print(num1,"es menor que ",num2)
else:
    print(num1, "es mayor que ",num2)