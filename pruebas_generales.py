
# Pruebas generales
# nro 1 fueron pruebas de la logica de isalpha, 
'''
x = 1
z : str = 'hola'
nombrePrueba: str = 'fernando9'

z = nombrePrueba.isalpha()

print(z)
'''
'''
while x == 1:
    Nombre = input("como te llamas? ")
    Apellido = input("cual es tu apellido? ")
    if type(Nombre) == ():
        print("bienvenido", Nombre, Apellido)
        x = x+1
    else:
        print("error en el nombre o apellido no se permiten numeros"),
'''
        
#esta son pruebas de la logica de ocurrencias mias para tarea 5
nombre = []
apellido = []
edad = []
email = []


def funcion_str(denominacion): #def luego el nombre de la funcion y entre parentesis el parametro que va a recibir
    
    
         #limpia la consola cada vez que se ejecuta la funcion
        if len (denominacion) < 3:
            print("DENEGADO: NO DEBE SER MENOR A 4 CARACTERES")
            denominacion =('')
            return denominacion

                
        elif any(char.isdigit() for char in denominacion):
            print('DENEGADO: NO DEBES INGRESAR NUMEROS')
            denominacion =('')
            return denominacion
        elif denominacion.isalpha()==False:
            print("DENEGADO: NO DEBES INGRESAR CARACTERES ESPECIALES")
            denominacion =('')           
            return denominacion
        else:            
            print(f"VALIDADO: {denominacion}")
            denominacion = denominacion.lower() 
            denominacion = denominacion.capitalize()  
            return denominacion
        
nombre=(funcion_str(input("ingresa tu nombre: ")))
apellido=(funcion_str(input("ingresa tu apellido: ")))

print(nombre, apellido)
'''
def funcion_repetir():
    global denominacion
    while BUCLE == 1:
        if denominacion != None:
            print('deseas continuar insertando datos si o no : ')
            validador = input("ingresa tu respuesta: ")
            validador = validador.lower()
            if validador == 'si':
                BUCLE = 1
            elif validador == 'no':
                BUCLE = 2
            else:
                while validador != 'si' and validador != 'no':
                    validador = input("respuesta no valida, ingresa 'si' o 'no': ")
                    validador = validador.lower()
                if validador == 'si':
                    BUCLE = 1
                else:
                    BUCLE = 2
        else:
            denominacion.remove(None)
funcion_repetir()
nombre.append(funcion_str(input("ingresa tu nombre: ")))
print(nombre)
'''

'''
while BUCLE == 1:
    nombre.append(funcion_str(input("ingresa tu nombre: ")))
    if nombre[-1] != None:
        print('deseas continuar insertando datos si o no : ')
        validador = input("ingresa tu respuesta: ")
        validador = validador.lower()
        if validador == 'si':
            BUCLE = 1
        elif validador == 'no':
            BUCLE = 2
        else:
            while validador != 'si' and validador != 'no':
                validador = input("respuesta no valida, ingresa 'si' o 'no': ")
                validador = validador.lower()
            if validador == 'si':
                BUCLE = 1
            else:
                BUCLE = 2
    else:
        nombre.remove(None)
print (nombre)
'''

  

