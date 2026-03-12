
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


nombre_list = []
apellido_list = []
edad_list = []
email_list = []
edad_mayor : int = 0
edad_menor : int = 0
may_men_lista = []
edad:str
contador: int
x=1
bucle = 'si'

def validar_nombre(tipo_nombre):
    while True:
        nombre_input=(input(f'ingrese {tipo_nombre} '))
        if any(char.isdigit() for char in nombre_input):
            print('no puedes ingresar numeros en', nombre_input)
        elif not nombre_input.isalpha() :
            print ('no puedes ingresar caracteres especiales')
        elif len(nombre_input)<3 and len(nombre_input) > 20:
            print('no cumples con la longitud de caracteres')
        else:
            print('VALIDO')
            nombre_input.lower()
            nombre_input.capitalize()
            return nombre_input

def validar_edad(edad_numero):
    while True:
        edad_input=input('ingrese su edad: ')
        if not edad_input.isdigit():
            print('no debes llevar letras en edad')
        elif int(edad_input)<0 or int(edad_input)>120:
            print('no estas e el rango permitido')
        else:
            print (f'{edad_numero} {edad_input} VALIDADA')
            return edad_input
'''
def es_mayor(edad_numero):
    if int(edad_numero) > 17:
        global mayorDeEdad
        mayorDeEdad = mayorDeEdad + 1
        return
    else:
        global menorDeEdad
        menorDeEdad = menorDeEdad + 1
        return 
   no me esta funcionando la funcion duda de no saber error
   ''' 
'''
def es_mayor(edad_numero):
    if 18 <=(edad_numero):
        x='M'
        return x
    else:
        x='m'
        return x 
sigue sin funcionar, no se si es por el tipo de dato o que, pero no me esta sumando a las variables globales, no se si es por el orden de las funciones o que, pero no me esta funcionando la funcion, duda de no saber error
'''
def es_mayor():
    global edad_list
    global edad_mayor
    global edad_menor
    global may_men_lista
    
    for numero in edad_list:
        print(numero)
        if int(numero) < 18:
            may_men_lista.append('menor de edad')
            edad_menor= 1 +int(edad_menor)

        elif int(numero) == 18:
            may_men_lista.append('justo mayor')
            edad_mayor= 1+int(edad_mayor)
        else:         
           may_men_lista.append('mayor de edad')
           edad_mayor= 1 + int(edad_mayor)
    return  
    
def validar_email(email):
    while True:
        email = input("Por favor, ingresa tu email: ")
        if "@" not in email or "." not in email:
                    #error si no incluye '@'
                    print("DENEGADO: El email debe contener '@' y un dominio válido.")
                
        else:# Si incluye '@', el email es válido
            if email.count('@') == 1 and email.endswith(('.com', '.com.mx', '.mx')):
                partes = email.split('@')
                antes_arroba = partes[0]
                despues_arroba = partes[1]
                if len(antes_arroba) > 2 and any(despues_arroba.startswith(dominio) for dominio in ['gmail', 'hotmail', 'yahoo']):
                    print("Email aceptado.")
                    return email
                else:
                    print("DENEGADO: formato de email incorrecto intenta con .com, .com.mx o .mx.")
            else:
                print("DENEGADO: ya deberias ser capaz de hacer un email estudie. intente con .com, .com.mx o .mx.")

def mostrar_usuario():
    global nombre_list
    global apellido_list
    global edad_list
    global email_list
    global bucle
    while True:
        print("==========================================================================")
        print("1. cargar usuario")
        print("2. Ver usuario por nombre")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            bucle = 'si'
            return 
        elif opcion == '2':
            nombre_buscar = input("Ingresa el nombre del usuario a buscar: ")
            if nombre_buscar in nombre_list:
                index = nombre_list.index(nombre_buscar)
                print(f"Usuario encontrado: {nombre_list[index]} {apellido_list[index]}, Edad: {edad_list[index]}, Email: {email_list[index]}")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == '3':
            for i in range(len(nombre_list)):
                print(f"{nombre_list[i]} {apellido_list[i]}, Edad: {edad_list[i]}, Email: {email_list[i]}")
        
        elif opcion == '4':
            break
        
        else:
            print("Opción no válida, por favor selecciona 1, 2 o 3.")

while bucle == 'si':
    nombre_validado = validar_nombre('nombre')
    apellido_validado = validar_nombre('apellido')
    edad_validado = validar_edad('edad')
    edad_validado=int(edad_validado)
    email_validado = validar_email('email')
    nombre_list.append(nombre_validado)
    apellido_list.append(apellido_validado)
    edad_list.append(edad_validado)
    email_list.append(email_validado)
    es_mayor()
    mostrar_usuario()
    print(f'mayores de edad: {edad_mayor}')
    print(f'menores de edad: {edad_menor}')

'''
validar_nombre(tipo)
Recibe como parámetro si es "nombre" o "apellido"
Pide el dato al usuario
Valida:
Que no tenga números
Que no tenga caracteres especiales
Que cumpla con longitud mínima/máxima
Devuelve el nombre/apellido válido usando return
'''



# mostrar usuario si se selecciona en el menu
#Menu
# 1 agregar usuario
# 2 o si ver usuario
# 3 o mostrar todos los usuarios
# 4 salir

# ---------------------------------------------



# Ciclo principal

## funcion_str()
        



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

  

