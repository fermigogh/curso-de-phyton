
x = 1

while x == 1:
    nombre = input("como te llamas? ")
    apellido = input("cual es tu apellido? ")

   
    if nombre.isalpha() == False or apellido.isalpha() == False:
        print("error en el nombre o apellido no se permiten numeros"),
    else:
        print("bienvenido", nombre, apellido)
        x = x+1

