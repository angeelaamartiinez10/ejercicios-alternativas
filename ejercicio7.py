'''Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y
el exponente. Pueden ocurrir tres cosas:
 El exponente sea positivo, sólo tienes que imprimir la potencia.
 El exponente sea 0, el resultado es 1.
 El exponente sea negativo, el resultado es 1/potencia con el exponente
positivo.
'''

base = 0
exponente = 0

base=(int)(input("Dime la base "))
exponente=(int)(input("Dime el exponenten "))

if (exponente>=0):
    print("La potencia es igual: ",base**exponente,)
elif (exponente==0):
    print("El resultado de la potencia es igual a 1")
elif(exponente<=0):
    print("La potencia es igual: ",1/(base**exponente),)
