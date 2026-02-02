CostosueldoIng=120
CostosueldoArquitecto=150
CostosueldoCapataz=100
CostosueldoObrero=25
sueldo_mensual: float

nombre = input("ingrese su nombre")
ID = input("ingrese su ID")
profesion = input("ingrese su profesion (ingeniero, arquitecto, capataz, obrero")

horas= input("ingrese la cantidad de horas trabajadas en el mes")
if profesion == "ingeniero":
    print("tu sueldo mensual es de: ", CostosueldoIng * int(horas))
elif profesion == "arquitecto":
    print("tu sueldo mensual es de: ", CostosueldoArquitecto * int(horas))
elif profesion == "capataz":
    print("tu sueldo mensual es de: ", CostosueldoCapataz * int(horas))
elif profesion == "obrero":
    print("tu sueldo mensual es de: ", CostosueldoObrero * int(horas))