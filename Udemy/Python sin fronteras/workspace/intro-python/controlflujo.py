# a == b
# a != b
# a < b
# a <= b
# a > b
# a >= b

a = 2
b = 5

if b == b:
    print(str(b) + ' es igual a ' + str(b))
if a < b:
    print(str(a) + ' es menor que ' + str(b))
if b > a:
    print(str(b) + ' es mayor que ' + str(a))
if b != a:
    print(str(a) + ' es diferente a ' + str(b))

print('---------------------------------------')

if 2 > 5:
    print('ejecución de if')
elif 3 != 3:
    print('ejecución de elif')
else:
    print('ejecución de else')

if 3 == 3: print('3 es igual a 3')

print('la operación ternaria es true') if 9 != 6 else print('operación ternaria es false')
print(':D') if 9 != 9 else print('D:')

if 8 == 8 and 3 >= 3:
    print('Ambas son verdaderas')

if 1 < 0 or 1 > 0:
    print('alguna es verdadera')