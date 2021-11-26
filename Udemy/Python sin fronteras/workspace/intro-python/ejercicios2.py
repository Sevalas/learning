import math

# 1. multiplicar dos números sin usar el símbolo de multiplicación

def ejecicio1():
    num1 = int(input('Esta función retorna la multiplicación de 2 números enteros sin usar el operador "*"\nIngresa el primer número: '))
    num2 = int(input('Ingresa el segundo número: '))
    result = 0
    for x in range(num2):
        result += num1

    print(str(num1)+' * '+str(num2)+' = '+str(result))

# 2. ingresar nombre y apellido e imprimirlo al reves

def ejecicio2():
    print('Esta función retorna un string invertirdo (ABCDE -> EDCBA)')
    name = input('Ingrese su nombre y apellido(s)')
    invertedName = ''
    nameLen = len(name)
    # Ya existe una función que te permite invertir los strings, esta es [::]
    # Para este caso concreto se puede usar como invertedName[::-1]
    for x in enumerate(name):
        nameLen -= 1
        invertedName += name[nameLen]
    print(invertedName)

# 3. escribir una función que encuentre el elemento menor de una lista

def ejecicio3():
    print('Esta función retorna el número entero menor de una lista')
    inputStr = input('Ingrese una lista de números separados por comas ","\nejemplo (33,22,19): ')
    list1 = [int(e) if e.isdigit() else e for e in inputStr.split(',')]
    minor = list1[0]
    for num in list1:
        if num < minor: minor = num
    print(minor)

# 4. escribir una función que devuelva el volumen de una esfera por su radio

def ejecicio4():
    print('Esta función retorna el volumen de una esfera por su radio')
    num = input('Ingrese el valor del radio de la esfera: ')
    result = 4 / 3 * math.pi * float(num)**3
    print('El volumen de una esfera con un radio de ' + num + ' es: '+ str(result))

# 5. escribir una función que indique si el usuario es mayor de edad

def ejecicio5():
    print('Esta función retorna una indicación que valida si el usuario es mayor de edad')
    edad = input('Ingrese la edad del usuario: ')
    print('El usuario es mayor de edad') if int(edad) > 17 else print('El usuario no es mayor de edad')

# 6. escribir una función que indique si un número es par o impar

def ejecicio6():
    print('Esta función valida si un número es par y retorna el resultado de la validación')
    num = input('Ingrese un número entero: ')
    print(num+' es un número par') if int(num) % 2 == 0 else print(num+' es un número impar')


# 7. escribir una función que indique cuantas vocales tiene una palabra

def ejecicio7():
    print('Esta función retorna la cantidad de vocales de en texto ingresado')
    text = input('Ingrese un texto cualquiera a continuación: ')
    vocales = ['a','e','i','o','u']
    count = 0
    for x in text:
        if x.lower() in vocales:
            count += 1
    print('El texto "'+text+'"\nTiene un total de '+ str(count) +' vocales')

# 8. escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados

def ejecicio8():
    print('Esta función retorna la suma de una cantidad de números infinitos')
    numList = []
    while True:
        userInput = input('Ingrese el '+str(len(numList) + 1)+'° número (Ingrese "basta" para realizar la suma): ')
        if (userInput == 'basta'): break
        else: numList.append(float(userInput))
    print(sum(numList))


# 9. escribir una función que reciba nombre y apellido y los vaya agregando a un archivo

def ejecicio9():
    file = open('names.txt', 'a')
    print('Esta función inserta en el archivo names.txt un nombre ingresado')
    name = input('Ingrese un nombre: ')
    file.write(name)
    file.write('\n')
    print('se ha insertado el nombre '+name)
    file.close()

print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
print('Lista de Ejercicios:')
print('1. Multiplicador de números sin operador multiplicativo')
print('2. Inversor de nombre')
print('3. Validador de número menor en lista')
print('4. Volumen de esfera por radio')
print('5. Detector de usuario mayor de edad')
print('6. Identificador de numero par/impar')
print('7. Contador de vocales en texto')
print('8. Sumador de lista de números infinita')
print('9. Insertor de nombre en archivo')
print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
def switchEjercicio(numEjercicio):
    switch = {
        '1': 'ejecicio1()',
        '2': 'ejecicio2()',
        '3': 'ejecicio3()',
        '4': 'ejecicio4()',
        '5': 'ejecicio5()',
        '6': 'ejecicio6()',
        '7': 'ejecicio7()',
        '8': 'ejecicio8()',
        '9': 'ejecicio9()'
    }
    print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    try:
        if numEjercicio in switch: eval(switch.get(numEjercicio))
        else: print('El valor ingresado es invalido')
    except Exception:
        print('Error de ejecución')
        print(Exception)

switchEjercicio(input('Ingresa el número del ejercicio: '))