x = 1
edad = 0

while x == 1:
    try:
        nombre = input("Por favor, ingresa tu nombre: ")
        apellido = input("Por favor, ingresa tu apellido: ")
        edad = input("Por favor, ingresa tu edad: ")
        email = input("Por favor, ingresa tu email: ")
            
            # Validación: verificar si hay números en la cadena
        if any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
                # Generar error si incluye números
                raise ValueError("Error: El nombre o el apellido no debe contener números.")
            
        elif nombre.isalpha() == False or apellido.isalpha() == False:
                raise ValueError("Error: El nombre o el apellido no debe contener caracteres especiales.")
        elif edad.isdigit() == False:
                raise ValueError("Error: La edad debe ser un número válido.")
        elif int(edad) < 18:
                raise ValueError("Error: Debes ser mayor de edad para registrarte.")
        
        else:# Si no hay números, el nombre es válido
                print(f"bienvenido: {nombre} {apellido}")
                print(f"Email aceptado: {email}")
                print(f"Edad aceptada: {edad}")
                x = int(input("desea continuar? (1 para si, 2 para no) "))        
            
    except ValueError as e:
            print(e) # Imprime el mensaje de error personalizado

any(char.isdigit() for char in nombre)