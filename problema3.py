#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
#Árbol trinario con listas

t = list(input().split())

for i in t:
    try:
        t[t.index(i)] = int(i)
    except:
        pass

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        return [numero, [], [], []]
    elif numero < arbol[0]:
        arbol[1] = insertaEnArbolTrinario(arbol[1], numero)
    elif numero == arbol[0]:
        arbol[2] =insertaEnArbolTrinario(arbol[2], numero)
    else:
        arbol[3] = insertaEnArbolTrinario(arbol[3], numero)
    return arbol

arbol = []

for i in t:
    arbol = insertaEnArbolTrinario(arbol, i)

print(arbol)