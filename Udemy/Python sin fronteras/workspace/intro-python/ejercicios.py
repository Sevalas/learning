# lista = ['hello','word','happy','pig','dragons']

# while True:
#     dato = input('ingrese el dato: ')

#     if lista.count(dato) > 0:
#         print('El dato existe en la lista', dato)
#         break
#     else:
#         print('El dato no existe en la lista', dato)

print('Calculadora basica de numeros enteros')
print('Para conseguir el resultado ingrese "="')
print('Para finalizar la calculadora ingrese "end"')

dictionary = {
    'labels': {
        'number': 'ingrese el entero #{number}: ',
        'operator': 'Ingrese un simbolo operacional'
    },
    'errors': {
        'invalidNum': 'error, ingrese un numero entero valido',
        'invalidSymbol': 'error, ingrese uno de los siguientes simbolos (+, -, /, *): ',
    },
    'symbolOp': ['+','-','/','*'],
    'flow': {
        'list': ['=','clear','end'],
        'result': '=',
        'clear': 'clear',
        'end': 'end',
        'continue': 'continue'
    }
}

values = []
operators = []

def input_set_value():
    while True:
        value = input(dictionary['labels']['number'].replace('{number}',str(len(values)+1)))
        try:
            values.append(value) if value in dictionary['flow']['list'] else values.append(int(value))
            break
        except:
            print(dictionary['errors']['invalidNum'])

def operator_set_value():
    while True:
        operator = input(dictionary['labels']['operator'] + ' ' + str(dictionary['symbolOp']) + ': ')
        if operator in dictionary['symbolOp'] + dictionary['flow']['list']:
            operators.append(operator)
            break
        else:
            print(dictionary['errors']['invalidSymbol'])

def flow_handler(callback,list):
    callback()
    if (dictionary['flow']['result'] == list[-1]):
        return dictionary['flow']['result']
    elif (dictionary['flow']['end'] == list[-1]):
        return dictionary['flow']['end']
    else:
        return dictionary['flow']['continue']

def operation_check(operator,value1,value2):
    if operator == dictionary['symbolOp'][0]: return value1 + value2
    if operator == dictionary['symbolOp'][1]: return value1 - value2
    if operator == dictionary['symbolOp'][2]: return value1 / value2
    if operator == dictionary['symbolOp'][3]: return value1 * value2

def operation_handler(list):
    if list[-1] == dictionary['flow']['result']:
        list.remove(dictionary['flow']['result'])
        result = 0;
        if len(values) != 0:
            if len(operators) == 0 or len(values) == 1: result = values[0]
            else:
                result = values[0]
                for index, operator in enumerate(operators):
                    result = operation_check(operator,result,values[index+1])
        print(result)
    if list[-1] == dictionary['flow']['end']:
            print('gracias por usar la calculadora')
            exit()

def operation():
    while True:
        while True:
            value_flow = flow_handler(input_set_value,values)
            if value_flow != dictionary['flow']['result']:
                break;
            operation_handler(values)
        while True:
            operation_flow = flow_handler(operator_set_value,operators)
            if operation_flow != dictionary['flow']['result']:
                break;
            operation_handler(operators)

operation()