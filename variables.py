#ESTO ES UN COMENENTARIO DE UNA SOLA LINEA
"""ESTO ES UN COMENTARIO DE 
VARIAS LINEAS """

#iniciando varriables
Nombre= "Danna Sofia Peñaloza Perez"
Edad= 12
Estado= True
Nota= 5.0

#Mostrar el contenido de las variables print()
print(Nombre)
print(Nota) 
print(Estado)
print(Edad)

#Que tipo de dato tiene cada variable
print(type(Nombre))
print(type(Edad))
print(type(Estado))
print(type(Nota))   

#vamos a utilizar la funcion input para recoger datos por medio de teclado 
Nombre= input("¿como te llamas? ")
Edad= input("¿cuantos años tienes? ")
Estado= input("¿en que estado te encuentras? ")
Nota= input("¿cual es tu nota? ")

#para visual9izar que guardamos en las variables anteriosres 
print("hola,",Nombre, "un gusto conocerte")
print("tu edad es",Edad)
print("tu estado es",Estado)
print("tu nota es",Nota)    