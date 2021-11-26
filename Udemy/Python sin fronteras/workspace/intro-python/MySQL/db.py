import mysql.connector

myDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='udemy'
)

cursor = myDb.cursor()

def getDataTable(*args):
    table = args[0]
    query = 'select * from '+table
    if len(args) > 1:
        query = 'select * from '+table+' limit ' + args[1]
    cursor.execute(query)
    return cursor.fetchall()

def getTableDef(table):
    query = 'show create table '+table
    cursor.execute(query)
    return(cursor.fetchall())

def insertDataTable(table, objectOfValues):
    tableFields = ', '.join(str(x) for x in objectOfValues.keys())
    valuesInputNum = ', '.join('%s' for x in objectOfValues)
    query = 'insert into '+table+' ('+tableFields+') values ('+valuesInputNum+')'
    cursor.execute(query,tuple(objectOfValues.values()))
    myDb.commit()
    return(cursor.rowcount, "records inserted.")

def updateDataTable(table, setObject, whereObject):
    setField = list(setObject.keys())[0]
    setValue = list(setObject.values())[0]
    whereField = list(whereObject.keys())[0]
    whereValue = list(whereObject.values())[0]
    query = 'update '+table+' set '+setField+' = %s where '+whereField+' = %s'
    cursor.execute(query,(setValue,whereValue))
    myDb.commit()
    return(cursor.rowcount, "records updated.")

def deleteDataTable(table, whereObject):
    whereField = list(whereObject.keys())[0]
    whereValue = list(whereObject.values())[0]
    query = 'delete from '+table+' where '+whereField+' = %s'
    cursor.execute(query,(whereValue,))
    myDb.commit()
    return(cursor.rowcount, "removed records.")