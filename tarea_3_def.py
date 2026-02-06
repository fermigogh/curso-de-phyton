x = 1
edad = 0

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
                        print(f"Error: Debes ser mayor de edad para registrarte. te faltan {diferencia} años")
                elif int(edad) == 18:
                        print(f"VALIDADO: {edad} apenas llegaste a la mayoria de edad")
                        break
                else:# Si no hay letras, la edad  es válido
                        diferencia= int(edad) - 18 
                        print(f"VALIDADO: {edad} eres mayor de edad superaste la mayoria de edad por {diferencia} años")
                        break
    while True:
        
            email = input("Por favor, ingresa tu email (gmail, hotmail, yahoo): ")

                # verificar si hay '@' en la cadena
            if "@" not in email or "." not in email:
                    #error si no incluye '@'
                    print("DENEGADO: El email debe contener '@' y un dominio válido.")
                
            else:# Si incluye '@', el email es válido
                    print(f"VALIDADO: {email}")
                    if email.count('@') == 1 and email.endswith(('.com', '.com.mx', '.mx')):
                        partes = email.split('@')
                        antes_arroba = partes[0]
                        despues_arroba = partes[1]
                        if len(antes_arroba) > 2 and any(despues_arroba.startswith(dominio) for dominio in ['gmail', 'hotmail', 'yahoo']):
                            print("Email aceptado.")
                            break
                        else:
                            print("DENEGADO: formato de email incorrecto intenta con .com, .com.mx o .mx.")
                    else:
                        print("DENEGADO: ya deberias ser capaz de hacer un email estudie. intente con .com, .com.mx o .mx.")
                        
    print(f"usuario: {nombre} {apellido}")
    print(f"Edad: {edad}")
    print(f"Email: {email}")
    x=int(input("DESEA INSERTAR DATOS? 1 PARA SI, 2 PARA NO"))
print("gracias pero pa cuando la salida al ramen")
