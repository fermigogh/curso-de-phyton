


nombre_list=[]
apellido_list=[]
edad_list = []
email_list=[]
edad_mayor : int = 0
edad_menor : int = 0
may_men_lista = []
edad:str
contador: int
x=1


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
    
print(f'mayores de edad: {edad_mayor}')
print(f'menores de edad: {edad_menor}')