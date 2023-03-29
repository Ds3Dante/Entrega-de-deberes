print("EJERCICIO 1")
print("CURSO DE FUNDAMENTOS DE PYTHON")
print("DANNY PINEDA\n")


a=int(input("Diguite un numero: "))
b=int(input("Diguite un numero: "))

respuesta=a==b
print("Opcion 1 para presentar Datos")
print("los numeros: "+str(a)+" y "+str(b)+" son iguales: "+str(respuesta))

print("Opcion 2 para presentar Datos" )
print(f"Los numeros: {a} y {b} son iguales: {respuesta}")

print("Opcion 3 para presentar Datos")
print("Los numeros: {} y {} son iguales: {}".format(a,b,respuesta))

print("Opcion 4 para presentar Datos")
print("Los numeros:",a,"y",b,"son iguales:",respuesta,"\n")

respuesta_2=a!=b
print("Opcion 1 para presentar Datos")
print("los numeros: "+str(a)+" y "+str(b)+" son diferentes: "+str(respuesta_2))

print("Opcion 2 para presentar Datos" )
print(f"Los numeros: {a} y {b} son diferentes: {respuesta_2}")

print("Opcion 3 para presentar Datos")
print("Los numeros: {} y {} son diferentes: {}".format(a,b,respuesta_2))

print("Opcion 4 para presentar Datos")
print("Los numeros:",a,"y",b,"son diferentes:",respuesta_2,"\n")

respuesta_3=a>b
print("Opcion 1 para presentar Datos")
print("El numero: "+str(a)+" es mayor que "+str(b)+": "+str(respuesta_3))

print("Opcion 2 para presentar Datos" )
print(f"El numero: {a} es mayor que {b}: {respuesta_3}")

print("Opcion 3 para presentar Datos")
print("El numero: {} es mayor que {}: {}".format(a,b,respuesta_3))

print("Opcion 4 para presentar Datos")
print("El numero:",a,"es mayor que",b,":",respuesta_3,"\n")

respuesta_4=a>=b
print("Opcion 1 para presentar Datos")
print("El numero: "+str(a)+" es mayor igual que "+str(b)+": "+str(respuesta_4))

print("Opcion 2 para presentar Datos" )
print(f"El numero: {a} es mayor igual que {b}: {respuesta_4}")

print("Opcion 3 para presentar Datos")
print("El numero: {} es mayor igual que {}: {}".format(a,b,respuesta_4))

print("Opcion 4 para presentar Datos")
print("El numero:",a,"es mayor igual que",b,":",respuesta_4,"\n")
