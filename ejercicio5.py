#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
# introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un
# error.

nombre=""
contraseña=""

nombre=(input("Dime un nombre se  ususario "))
contraseña=(input("Dime una contraseña "))

if (nombre=="pepe" and contraseña=="asdasd" ):
    print("ENHORABUENA, has entrado en el programa")
else:
    print("ERROR, no has entrado en el programa")