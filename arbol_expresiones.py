from pila import *
from arbol import *

dictionary = {
    }

def updateDict(let, val):    
    dictionary[let.valor] = val
    print let.valor+' = '+str(dictionary[let.valor])

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":           
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
    if arbol.valor == "=":        
        return updateDict(arbol.der, evaluar(arbol.izq))
    if arbol.valor.isalpha():
        return dictionary[arbol.valor]
    return int(arbol.valor)

entrada = open("expresiones.in","r")

exp = entrada.readlines()

pila = Pila()

for i in range(0, len(exp)):        
    pp = exp[i]
    str1 = ''.join(pp.strip('\n'))        
    exp2 = str1.split(" ")   
    convertir(exp2, pila)
    

entrada.close()

entrada = open("expresiones.out","w")

while pila.es_vacia() != True:    
    res = evaluar(pila.desapilar())
    str(res)
    entrada.write(str(res))
    if res!= None:
        print res


entrada.close()
"""3 5 *
1 2 + 5 6 - *"""
