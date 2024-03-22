#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = list(input("t1: ").split())
t2 = list(input("t2: ").split())

for a,b in t1,t2:
    try:
        t1[t1.index(a)] = int(a)
        t2[t2.index(b)] = int(b)
    except:
        pass



print(tuple(t2+t1+t2))