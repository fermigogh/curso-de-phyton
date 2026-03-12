nombre_list=[]
apellido_list=[]
edad_list = []


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