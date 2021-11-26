# -*- coding: utf-8 -*-
import cx_Oracle
import random
import configparser
import getExcelValues

configParser = configparser.ConfigParser(); configParser.read('connections.properties')
connections = dict(configParser.items('connections'))
sps = dict(configParser.items('sps'))

connection = cx_Oracle.connect(connections['user'],connections['pass'],connections['host'])
cursor = connection.cursor()

out_val_int = cursor.var(int)
out_val_str = cursor.var(str)

user = input('ingrese nombre de usuario (50 caracteres max): ')
if user == '' or len(user) > 50: user = 'default'
listOfValues = getExcelValues.getExcelValues(user)
print('user: '+user)

print('------------------------------------------------------')
while True:
    inputSp = input('ingrese 1 para insertar registro vigente\ningrese 2 para insertar registro historico\n:')
    if inputSp == '1':
        sp = sps['vigentes']
        break
    if inputSp == '2':
        sp = sps['historicos']
        break
print('------------------------------------------------------')

insertsCount = 0;
for idx,values in enumerate(listOfValues):
    index = 0;
    while index != len(listOfValues[idx]['in_rut_deudor']):
        cursor.callproc(sp,
        [
        listOfValues[idx]['in_rut_deudor'][index],
        listOfValues[idx]['in_nombre_deudor'][index],
        random.randint(0, 1),
        random.randint(0, 1),
        random.randint(0, 1),
        listOfValues[idx]['in_nombre_publicacion'][index],
        listOfValues[idx]['in_procedimiento_descripcion'][index],
        listOfValues[idx]['in_tribunal_descripcion'][index],
        listOfValues[idx]['in_rol'][index],
        listOfValues[idx]['in_veedor'][index],
        listOfValues[idx]['in_fecha_publicacion'],
        listOfValues[idx]['in_fecha_actualizacion'],
        listOfValues[idx]['in_usuario'],
        out_val_int,
        out_val_str
        ]
        )
        if out_val_int.getvalue() == 0:
            index += 1
        else:
            break
    insertsCount += index
    if(out_val_int.getvalue() == 1):
        break
if(out_val_int.getvalue() == 0):
    print('se ha(n) insertado '+str(insertsCount)+' registro(s)')
    print('------------------------------------------------------')
    if input('para realizar commit ingrese 1 o ingrese cualquier otro dato para realizar rollback\n:') == '1':
        connection.commit()
        print('commit exitoso')
        connection.close()
    else:
        connection.rollback()
        print('rollback exitoso')
        connection.close()
else:
    print('error en la ejecución del sp')
    connection.close()