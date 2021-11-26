def myFunction():
    print('mi first function')

# myFunction()

#Argumento son las variables de entrada que se instancian desde la función
def printData(name,lastname):
    print("the complete name is:",name,lastname)

#Parametro son los variables de entrada que se ingresan en el llamado de una función
printData("happy","piglet")

def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

# Se pueden ingresar los parametros en otro orden especificando el nombre del parametro
nombreCompleto(nombre='michael',apellido='jackson')

# * para esperar una lista indeterminada como argumentos
def listOfArguments(*list):
    print(list)

listOfArguments('hi','hello','what\'s up')

# * para esperar un objeto como argumentos
def objectOfArguments (**kwargs):
    print(("El nombre es {}, el apellido {} y tiene una edad de: {}").format(kwargs['nombre'],kwargs['apellido'],kwargs['edad']))

objectOfArguments(nombre='susana',apellido='apellido',edad=22)

def miFunction2(argument='defaultArgument'):
    print(argument)

miFunction2('mi function2 with param')
miFunction2()

def listFunction(list):
    for element in list:
        print(element)

listFunction(['this is a list',1,2,3,4,'end of the list'])

def concatName(list):
    i = ''
    for element in list:
        i += element+' '
    return i

print(concatName(['Edward','Elric']))

def recursively(i):
    if i < 1:
        return i
    else:
        print(i)
    recursively(i-1)

print(recursively(6))
