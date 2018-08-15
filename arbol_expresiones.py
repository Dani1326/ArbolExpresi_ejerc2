from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


entrada = open("expresiones.in","r")

exp = entrada.readline()

str1 = ''.join(exp)

#exp3 = str1.split("\n")
print str1
#for i in exp3:
#    print exp3[i]
    

entrada.close()
exp2 = str1.split(" ")




pila = Pila()

convertir(exp2, pila)
entrada = open("expresiones.out","w")

res = evaluar(pila.desapilar())
print res
str(res)
entrada.write(str(res))

entrada.close()
"""3 5 *
1 2 + 5 6 - *"""
