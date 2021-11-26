# -*- coding: utf-8 -*-
import xlrd
import datetime
import sys,os

def getExcelValues(user):

    def getRelativePath():
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(__file__)

    def getDate(sheet):
        return datetime.datetime.strptime(sheet.cell_value(0, 0)[sheet.cell_value(0, 0).find('/')-2:len(sheet.cell_value(0, 0))],'%d/%m/%Y')

    def getCellPostionByValue(sheet,value):
        for row_idx in range(0, sheet.nrows):
            for col_idx in range(0, sheet.ncols):
                if sheet.cell_value(row_idx, col_idx) == value:
                    return {'row':row_idx,'col':col_idx}

    def getListOfValuesByColumn(sheet,columnValue):
        pos = getCellPostionByValue(sheet,columnValue)
        null_string = 'N/A'
        list = []
        for row_idx in range(pos['row']+1, sheet.nrows):
            if sheet.cell_value(row_idx, pos['col']) == None or sheet.cell_value(row_idx, 0) == '':
                list.append(null_string)
            else:
                list.append(sheet.cell_value(row_idx, pos['col']))
        return list

    def getListOfSheets(relativeFolder):
        listOfFileNames = os.listdir(getRelativePath()+'/'+relativeFolder)
        listOfSheets = []
        for fileName in listOfFileNames:
            sheetCursor = xlrd.open_workbook(relativeFolder+'/'+fileName)
            sheet_names = sheetCursor.sheet_names()
            actual_sheet = sheetCursor.sheet_by_name(sheet_names[0])
            listOfSheets.append(actual_sheet)
        return listOfSheets

    listOfSheets = getListOfSheets('xls')
    listOfParseSheets = []

    for sheet in listOfSheets:
        objectOfValues = {
            'in_rut_deudor': getListOfValuesByColumn(sheet,'RUT'),
            'in_nombre_deudor': getListOfValuesByColumn(sheet,'Deudor'),
            'in_nombre_publicacion': getListOfValuesByColumn(sheet,'Nombre publicación'),
            'in_procedimiento_descripcion': getListOfValuesByColumn(sheet,'Procedimiento concursal'),
            'in_tribunal_descripcion': getListOfValuesByColumn(sheet,'Tribunal'),
            'in_rol': getListOfValuesByColumn(sheet,'Rol'),
            'in_veedor': getListOfValuesByColumn(sheet,'Veedor/Liquidador titular'),
            'in_fecha_publicacion': getDate(sheet),
            'in_fecha_actualizacion': datetime.datetime.today(),
            'in_usuario': user,
        }
        listOfParseSheets.append(objectOfValues)
    return listOfParseSheets