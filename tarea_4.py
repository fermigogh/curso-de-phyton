nombre =[""]
apellido =[""]
email =[""]
edad =[]



x = 1

usuario_NR = int

x=int(input("DESEA INSERTAR DATOS? 1 PARA SI, 2 PARA NO: "))
while  x == 1:
    
    while True:
        
            nombre.append(input("Por favor, ingresa tu nombre: "))
            if len(nombre[-1]) < 3:
                print("DENEGADO: El nombre debe tener al menos 3 caracteres.")
            
                # Validación: verificar si hay números en la cadena
            elif any(char.isdigit() for char in nombre[-1]):
                    # Generar error si incluye números
                    print("DENEGADO: El nombre o el apellido no debe contener números.")
                
            elif not nombre[-1].isalpha():
                    print("DENEGADO: El nombre o el apellido no debe contener caracteres especiales.")
            else:# Si no hay números, el nombre es válido
                    print(f"VALIDADO: {nombre[-1]}")
                    break
    while True:
        
            apellido.append(input("Por favor, ingresa tu apellido: "))
            if len(apellido[-1]) < 3:
                print("DENEGADO: El apellido debe tener al menos 3 caracteres.")
                # Validación: verificar si hay números en la cadena
            elif any(char.isdigit() for char in apellido[-1]):
                    # Generar error si incluye números
                    print("DENEGADO: El apellido no debe contener números.")
                
            elif not apellido[-1].isalpha():
                    print("DENEGADO: El apellido no debe contener caracteres especiales.")
            else:# Si no hay números, el nombre es válido
                    print(f"VALIDADO: {apellido[-1]}") # apellido[-1] accede al último apellido agregado
                    break
    while True:
        
            edad.append(input("Por favor, ingresa tu edad: "))
                
                    # Validación: verificar si hay números en la cadena
            if not edad[-1].isdigit():
                        # Generar error si incluye números
                    print(f"DENEGADO: aprende que solo son numeros en edad")
            elif int(edad[-1]) <=0 or int(edad[-1]) >=120:
                    print("Error: Edad no valida. Ingresa una edad entre 0 y 120.")
                       
            elif int(edad[-1]) < 18:
                    diferencia = 18 - int(edad[-1])
                    print(f"Error: Debes ser mayor de edad para registrarte. te faltan {diferencia} años")
            elif int(edad[-1]) == 18:
                    print(f"VALIDADO: {edad[-1]} apenas llegaste a la mayoria de edad")
                    break
            else:# Si no hay letras, la edad  es válido
                    diferencia= int(edad[-1]) - 18 
                    print(f"VALIDADO: {edad[-1]} eres mayor de edad superaste la mayoria de edad por {diferencia} años")
                    break
    while True:
        
            email.append(input("Por favor, ingresa tu email (gmail, hotmail, yahoo): "))

                # verificar si hay '@' en la cadena
            if "@" not in email[-1] or "." not in email[-1]:
                    #error si no incluye '@'
                    print("DENEGADO: El email debe contener '@' y un dominio válido.")
                
            else:# Si incluye '@', el email es válido
                    
                    if email[-1].count('@') == 1 and email[-1].endswith(('.com', '.com.mx', '.mx')):
                        partes = email[-1].split('@')
                        antes_arroba = partes[0]
                        despues_arroba = partes[1]
                        if len(antes_arroba) > 2 and any(despues_arroba.startswith(dominio) for dominio in ['gmail', 'hotmail', 'yahoo']):
                            print("Email aceptado.")
                            break
                        else:
                            print("DENEGADO: formato de email incorrecto intenta con .com, .com.mx o .mx.")
                    else:
                        print("DENEGADO: ya deberias ser capaz de hacer un email estudie. intente con .com, .com.mx o .mx.")
                        

    x=int(input("DESEA INSERTAR DATOS? 1 PARA SI, 2 PARA NO"))

while True:
    val_verusuario = input("DESEA VER USUARIOS? SI o NO ")
    if val_verusuario.lower()=="si":
        usuario_NR=int(input("que usuario desdea mostrar?"))
        usuario_NR=usuario_NR-1
        usuario_NR = int(input("ingresa el numero de usuario que deseas mostrar: "))
        print(f"usuario: {nombre[usuario_NR]} {apellido[usuario_NR]}")
        print(f"Edad: {edad[usuario_NR]}")
        print(f"Email: {email[usuario_NR]}")
    elif val_verusuario.lower()=="no":
        print("gracias pero pa cuando la salida al ramen")
        break
    else:
        print("respuesta no valida, por favor ingresa SI o NO")