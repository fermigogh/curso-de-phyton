X = 0
basesujeto = []
sujeto1 = []
sujeto2 = []
sujeto3 = []

codigo = 0
print("bienvenido ahora vamos a intentar asignar a 10 sujetos luego preguntaremos por ellos en datos")
while X < 3:
    X += 1
    nombre=str(input("ingrese el nombre asignar el siguiente sujeto  "))
    apellido=str(input("ingrese el apellido del sujeto  "))
    edad=int(input("ingrese la edad del sujeto  "))
    codigo=codigo + 1
    if sujeto1 == basesujeto:
        sujeto1.append(codigo)
        sujeto1.append(nombre)
        sujeto1.append(apellido)
        sujeto1.append(edad)
    elif sujeto2 == basesujeto:
        sujeto2.append(codigo)
        sujeto2.append(nombre)
        sujeto2.append(apellido)
        sujeto2.append(edad)
    elif sujeto3 == basesujeto:
        sujeto3.append(codigo)
        sujeto3.append(nombre)
        sujeto3.append(apellido)
        sujeto3.append(edad)
for codigo in range (1,4):
    if codigo == 1:
        print("sujeto numero: ", sujeto1[0])
        print("nombre: ", sujeto1[1])
        print("apellido: ", sujeto1[2])
        print("edad: ", sujeto1[3])
    elif codigo == 2:
        print("sujeto numero: ", sujeto2[0])
        print("nombre: ", sujeto2[1])
        print("apellido: ", sujeto2[2])
        print("edad: ", sujeto2[3])
    elif codigo == 3:
        print("sujeto numero: ", sujeto3[0])
        print("nombre: ", sujeto3[1])
        print("apellido: ", sujeto3[2])
        print("edad: ", sujeto3[3])
print("ahora probaremos mostrar los datos del q usted seleccione")
quest=bool(input("desea buscar un sujeto por su codigo? (True/False)"))
if quest == True:
    while quest == True:
        codigo=int(input("ingrese el codigo del sujeto que desea buscar (1-3)"))
        print ("sujeto numero: ", codigo)
        print ("nombre: ", nombre)  
        print ("apellido: ", apellido)
        print ("edad: ", edad)
        quest=bool(input("desea buscar un sujeto por su codigo? (True/False)"))
else:
    print("gracias por usar el programa")