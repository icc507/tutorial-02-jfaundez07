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
t1 = list(input().split())
t2 = list(input().split())

def verificarInt(lista):
    for i in lista:
        try:
            lista[lista.index(i)] = int(i)
        except:
            pass
    return lista

verificarInt(t1)
verificarInt(t2)

output = tuple(t2+t1+t2)

print(output)