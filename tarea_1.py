EDAD : int
NOMBRE : str 
APELLIDO : str

print( "bienvenido sucio y fetido humano vienes por el curso?")
NOMBRE = input("anuncia tu nombre simple mortal: ")
print("bienvenido a este mundo cruel:", NOMBRE , "deberas entregar tu alma para sobrevivir a las lecciones" )
APELLIDO = input("pero antes como te apellidas? ente repugnante: ")
print("entonces eres :", NOMBRE , APELLIDO , "nombre digno de un esclavo buajajaja")
EDAD = int(input("cuanto tiempo has estado en el mundo?"))

if EDAD < 18:
    Y = 18 - EDAD
    print("eres un infante, no mereces estar en este curso te faltan" , Y , "años para ser un verdadero esclavo")
else :
    X = EDAD - 18
    if X == 0:
        print("prepárate para ser esclavizado este curso solo aprueban los que siguen las ordenes", NOMBRE , APELLIDO ,"este ciclo de estaciones lograste alcanzar la mayoria de edad")
    else:  
        print("prepárate para ser esclavizado este curso solo aprueban los que siguen las ordenes", NOMBRE , APELLIDO ,"ya tienes" , X , "ciclos superados desde que alcanzaste la mayoria de edad")
    
    

