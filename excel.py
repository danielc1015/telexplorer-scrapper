from openpyxl import load_workbook


def leerUnaHoja(hoja):
    sheet = ''
    try:
        workbook = load_workbook('datos.xlsx', read_only=False)
        sheet = workbook[hoja]
        return sheet
    except:
        print('Nombre de hoja incorrecto. \n==== EJECUCIÓN FINALIZADA ====')
        exit()

def guardarDatos(numeros, hoja):
    i = 0
    workbook = load_workbook('datos.xlsx', read_only=False)
    sheet = workbook[hoja]
    for tel in numeros:
        i += 1
        celda = sheet.cell(row = i, column = 3)
        celda.value = tel

    workbook.save('datos.xlsx')