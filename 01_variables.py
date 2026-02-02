'''
variables siempre en minusculas
'''
my_vareable_string = 'este es mi vareable'
my_vareable_int = 10
my_vareable_float = 10.5
my_vareable_bool = True


print (my_vareable_string)
print (my_vareable_int)
print (my_vareable_float)
print (my_vareable_bool)

# imprimir todas las variables en una sola linea con comas
print (my_vareable_string, my_vareable_int, my_vareable_float, my_vareable_bool)

print(type(print (my_vareable_string, my_vareable_int, my_vareable_float, my_vareable_bool)))#no llega a decir los tipos de las variables

print(type(print (my_vareable_string)))
#no importa si es en cadena o singular siempre aparece none type 

#funciones precargadas de python
print(len(my_vareable_string)) 
#len cuenta los caracteres de la cadena cuenta


#concatenacion de cadenas de texto y variables
print("este es el valor de mi variable booleana:", my_vareable_bool)

nombre, apellido , edad , alias , estado_fiscal = "fernando", "miranda", 28, "fermi", True

#imprimir todas las variables en una sola linea con comas y informacion adicional pero ala practicidad es malo dificil localizar errores
print("el nombre del sujeto es:", nombre, apellido, "tiene", edad, "años", "su alias es:", alias, "y su estado fiscal de casamiento es:", estado_fiscal)
#el print no imprimer si ponemos'' solo si lleva "" muesrta en pantalla

#input
"""
funciona pero es molesto para seguir corriendo

apellido
nombre = input("anuncia tu nombre simple mortal")
print("bienvenido a este mundo cruel:", nombre)
print("aqui deberas entregarte para sobrevivir a las lecciones" )
apellido = input("como te apellidas? ente repugnante")
print("entonces eres :", nombre, apellido, "nombre digno de un esclavo buajajaja")
print("prepárate para ser esclavizado este curso solo aprueban los que siguen las ordenes", nombre, apellido)
"""

#cambiemos el tipo
nombre = 10
apellido = 15

# se podra forzar el tipo de variable
name :str = "ferna" 
subname:str = "miranda"



print("el nombre del sujeto es:", name, subname, "ahora pero")

name = input("como desea llamarse ahora")
subname = input("como desea apellidarte ahora")
print("entonces seras :", name, subname, "nombre interesante")

name = 100

print(type(nombre))

""" 
si se puede cambiar el tipo de variable aun cuando se le haya forzado un tipo si ingresas otro diferente , pero parece
que si ingresas otro diferente al forzado te lo toma como el tipo forzado si se usa input
"""