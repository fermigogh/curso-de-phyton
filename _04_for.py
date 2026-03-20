from encodings.punycode import T


lista_numeros=[]


while True:
    num = input('ingrese un numero: ')
    if not num.isdigit():
        print('no puedes ingresar letras')
    elif num.isalpha() == True:
        print('no puedes ingresar caracteres especiales')
    else:
        lista_numeros.append(num)
        print('VALIDO')
        
    print('desea continuar?  si o no')
    bucle= input()
    bucle = bucle.lower()
    bucle = bucle.capitalize()
    if bucle == 'No':
        break
    elif bucle == 'Si':
        continue
    else:
        print('no es una opcion valida, se continuara con el programa')
        continue
print(lista_numeros)


for numero in lista_numeros:
    print(numero)
    if int(numero) < 18:
         print('menor de edad')
    elif int(numero) == 18:
        print('encontrado')
    else:         
        print('mayor de edad')
    
