nombre: str
apellido: str
email: str
edad: int
usuario: int
menu = 0 
mayores=0
menores=0
contador = 0
count = 0
lista_nombre =[]
lista_apellido =[]
lista_email =[]
lista_edad =[]

x = 1
x2 = 1


x=int(input("DESEA INSERTAR DATOS? 1 PARA SI, 2 PARA NO: "))
while  x == 1:
    
    while True:
        
            nombre = input("Por favor, ingresa tu nombre: ")
            if len(nombre) < 3:
                print("DENEGADO: El nombre debe tener al menos 3 caracteres.")
            
                # Validación: verificar si hay números en la cadena
            elif any(char.isdigit() for char in nombre):
                    # Generar error si incluye números
                    print("DENEGADO: El nombre o el apellido no debe contener números.")
                
            elif nombre.isalpha() == False:
                    print("DENEGADO: El nombre o el apellido no debe contener caracteres especiales.")
            else:# Si no hay números, el nombre es válido
                    print(f"VALIDADO: {nombre}")
                    nombre = nombre.lower()  # Convertir a minúsculas
                    nombre = nombre.capitalize()  # Convertir la primera letra a mayúscula
                    lista_nombre.append(nombre)
                    break
    while True:
        
            apellido = input("Por favor, ingresa tu apellido: ")
            if len(apellido) < 3:
                print("DENEGADO: El apellido debe tener al menos 3 caracteres.")
                # Validación: verificar si hay números en la cadena
            elif any(char.isdigit() for char in apellido):
                    # Generar error si incluye números
                    print("DENEGADO: El apellido no debe contener números.")
                
            elif apellido.isalpha() == False:
                    print("DENEGADO: El apellido no debe contener caracteres especiales.")
            else:# Si no hay números, el nombre es válido
                    print(f"VALIDADO: {apellido}")
                    apellido = apellido.lower()  # Convertir a minúsculas 
                    apellido = apellido.capitalize()  # Convertir la primera letra a mayúscula
                    lista_apellido.append(apellido)
                    break
    while True:
       
           
                edad =input("Por favor, ingresa tu edad: ")
                
                    # Validación: verificar si hay números en la cadena
                if not edad.isdigit():
                        # Generar error si incluye números
                        print(f"DENEGADO: aprende que solo son numeros en edad")
                elif int(edad) <=0 or int(edad) >=120:
                        print("Error: Edad no valida. Ingresa una edad entre 0 y 120.")
                       
                elif int(edad) < 18:
                        diferencia = 18 - int(edad)
                        menores = menores + 1
                        print(f" te faltan {diferencia} años PARA SER MAYOR DE EDAD")
                        break
                elif int(edad) == 18:
                        print(f"VALIDADO: {edad} apenas llegaste a la mayoria de edad")
                        break
                else:# Si no hay letras, la edad  es válido
                        diferencia= int(edad) - 18 
                        mayores = mayores + 1
                        print(f"VALIDADO: {edad} eres mayor de edad superaste la mayoria de edad por {diferencia} años")
                        lista_edad.append(edad)
                        break
    while True:
        
            email = input("Por favor, ingresa tu email (gmail, hotmail, yahoo): ")

                # verificar si hay '@' en la cadena
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
                            lista_email.append(email)
                            contador =contador + 1
                            break
                        else:
                            print("DENEGADO: formato de email incorrecto intenta con .com, .com.mx o .mx.")
                    else:
                        print("DENEGADO: ya deberias ser capaz de hacer un email estudie. intente con .com, .com.mx o .mx.")
                        

    x=int(input("DESEA INSERTAR DATOS? 1 PARA SI, 2 PARA NO"))



while True:
        print("==========================================================================")
        print("SI DESEA BUSCAR UN USUARIO RESIONE 1 PARA SI, " )
        print("SI DESEA VER TODOS LOS USUARIOS PRESIONE 2")
        print("SI DESEA VER LAS ESTADISTICAS PRESIONE 3")
        print("SI DESEA SALIR PRESIONE 4")
        menu=input("Nro: ")
        if menu == "1":
                print("==========================================================================")
                print("que usuario desea ver .poseemos: ", contador, "usuarios registrados: ")
                usuario = int(input("ingrese un numero entro los dichos"))
                print("==USUARIO SELECCIONADO==", usuario)
                usuario = usuario - 1
                print("Nombres ingresados:", lista_nombre[usuario])
                print("Apellidos ingresados:", lista_apellido[usuario])
                print("Emails ingresados:", lista_email[usuario])
                print("Edades ingresadas:", lista_edad[usuario])
                x2 = int(input("DESEA volver al menu o salir presione 1 para si y 2 para no: "))
                if x2 == 1:
                        continue
                elif x2 == 2:
                        print("Gracias por usar el programa, hasta luego")
                        break
                else:
                        print("Opcion no valida, por favor ingrese una opcion del menu")
                
        elif menu == "2":
                count = contador
                
                for i in range(count):
                        nro = i
                        nro2 = nro + 1
                        print("==========================================================================")
                        print("==USUARIOS REGISTRADOS==")
                        print("USUARIO nro: -", nro2, lista_nombre[nro], lista_apellido[nro], "(", lista_edad[nro] , ")", "-", lista_email[nro])


                        
        elif menu == "3":
                print("==========================================================================")
                print("==ESTADISTICAS DE USUARIOS==")
                print("la cantidad de usuarios registrados es: ", contador)
                print("la cantidad de usuarios mayores de edad es: ", mayores)
                print("la cantidad de usuarios menores de edad es: ", menores)
                x2 = int(input("DESEA volver al menu o salir presione 1 para si y 2 para no: "))
                if x2 == 1:
                        continue
                elif x2 == 2:
                        print("Gracias por usar el programa, hasta luego")
                        break
                else:
                        print("Opcion no valida, por favor ingrese una opcion del menu")

        elif menu == "4":
                break
        else:
                print("Opcion no valida, por favor ingrese una opcion del menu")
print("trabajo 4 terminado")
