#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

vNum = []

Num=(int)(input("Dime un número"))
vNum.append(Num)

Num=(int)(input("Dime el segundo número"))
vNum.append(Num)

Num=(int)(input("Dime tercer número"))
vNum.append(Num)

vNum.sort()
print(vNum)


print("El mayor es",vNum[2])
print("El menor es ",vNum[0])

ultimo = len (vNum)
print("El mayor es ",vNum[ultimo-1])

