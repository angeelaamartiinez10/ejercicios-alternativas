#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, 
#o un mensaje de aviso en caso contrario.

num1=0
num2=0

num1=(int)(input("Dime un número "))
num2=(int)(input("Dime otro número "))

if num2!=0:
    print("El resultado de la división es:",num1/num2,)
else:
    print("El denominador es 0, no se puede hacer la división")