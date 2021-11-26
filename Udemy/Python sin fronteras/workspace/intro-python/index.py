# Comentario lineal de prueba
# if 5 > 3: # Comentario lineal en linea de codigo
    # print("5 es mayor a 3")

if 3 > 5:
    print("Esto no se va a imprimir")

x = 5
y = 'i griega'

print(x, y)

email = 'i@griega.com'
print(email)

_mi_var = 'i_griega'
miVar = 'iGriega'
a, b, c = 'iAlemana', 'iBrasileña', 'iCanadience'

print(a,b,c)

varA = varB = varC = 'iContenta'

print(varA,varB,varC)

varInicial = 'i'
varFinal = 'Griega'

print(varInicial + varFinal)

#Tipo de Datos
word = 'I Griega' #String
word2 = "I Griega \"\"" #String

#Numeros
entero = 20 # integer
decimal = 30.2 # float
complejo = 93939j # complex

print(word,word2,entero,decimal,complejo)

emptyList = [] # list
list1 = [1,2,3,4,5] # list
list2 = list1.copy()
# list.clear()
list1.append(entero)

print(emptyList)
print(list1)
print(list2)
print(list2.count(5))
print(len(list2),len(list1))

largoList = len(list1)
largoList2 = len(list2)
print(largoList+largoList2)
print(list1[1])
list1.pop()
list1.pop()
print(list1)
list1.remove(2)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
del list1[0]
print(list1)

tupla = ('i','griega','en','tupla') # tupla
print(tupla)
listaDeTupla = list(tupla)
print(listaDeTupla)

rango = range(6)
print(rango)

diccionario = {
   'modelo': 'fat',
   'memoria': '1gb',
   'serie': 3001
}
print(diccionario)
print(diccionario['modelo'])
print(diccionario.get('serie'))
diccionario['modelo'] = 'slim'
print(diccionario)
diccionario['color'] = 'orange'
copiaDiccionario = diccionario.copy()
copiaDiccionario2 = dict(diccionario)
print(diccionario)
diccionario.pop('serie')
print(diccionario)
diccionario.popitem()
print(diccionario)
print(copiaDiccionario)
del diccionario['memoria']
print(diccionario)
print(copiaDiccionario2)
diccionario.clear()
print(diccionario)

psp1000 = {
    'alias': 'fat',
    'peso(g)': 280
}
psp3000 = {
    'alias': 'slim',
    'peso(g)': 189
}
psp = {
    1000: psp1000,
    3000: psp3000
}
print(psp)
perritos = dict(nombre='happy chanchito',edad=666)
print(perritos)

booleanoT = True
booleanoF = False
print(booleanoT,booleanoF)