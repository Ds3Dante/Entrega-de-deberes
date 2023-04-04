print("FUNDAMENTOS DE PYTHON")
print("31/03/2023")
print("DANNY PINEDA\n")
nombre=input("Ingrese su Nombre: ")
print("Diguite 1 si pertenece al Departamento de atencion al cliente")
print("Diguite 2 si pertenece al Departamento de Logistica")
print("Diguite 3 si pertenece al Departamento de Gerencia")
departamento=int(input("Diguite a que departamento pertenece: "))
años=int(input("Ingrese los años de servicio: "))
if departamento==1:
    if años==1:
        print("Hola",nombre,"por tu",años,"año de trabajo, obtendras 6 Días de Vacaciones.")
    if años>=2 and años<=6:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 12 Días de Vacaciones.")
    if años>7:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 20 Días de Vacaciones.")
if departamento==2:
    if años==1:
        print("Hola",nombre,"por tu",años,"año de trabajo, obtendras 7 Días de Vacaciones.")
    if años>=2 and años<=6:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 14 Días de Vacaciones.")
    if años>7:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 22 Días de Vacaciones.")
if departamento==3:
    if años==1:
        print("Hola",nombre,"por tu",años,"año de trabajo, obtendras 10 Días de Vacaciones.")
    if años>=2 and años<=6:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 20 Días de Vacaciones.")
    if años>7:
        print("Hola",nombre,"por tus",años,"años de trabajo, obtendras 30 Días de Vacaciones.")
        