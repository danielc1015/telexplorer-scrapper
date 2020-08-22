import excel
import telexplorer

def resumen(listado):
    sinTelefono = 0

    for telefono in listado:
        if telefono == '-':
            sinTelefono += 1
    
    print('\n\n\n ************* RESUMEN *************')
    print('Direcciones analizadas: ' + str(len(listado)))
    print('>>>>>> Con telefono: ' + str(len(listado) - sinTelefono))
    print('>>>>>> Sin telefono:' + str(sinTelefono))



def mostrarMenu():
    opcion: int
    print ('1. Buscar una hoja')
    print ('2. Buscar todas las hojas')
    opcion = input('Opcion:  ')
    return opcion
    


def iniciarBusqueda(opcion):
    if opcion == '1':
        hoja = input("Ingrese el nombre de la hoja: ")
        sheet = excel.leerUnaHoja(hoja)
        listado = telexplorer.buscar(sheet)
        excel.guardarDatos(listado, hoja)

    if opcion == '2':
        sheets = excel.obtenerNombresSheets()
        for hoja in sheets:
            sheet = excel.leerUnaHoja(hoja)
            listado = telexplorer.buscar(sheet)
            excel.guardarDatos(listado, hoja)





opcion = mostrarMenu()
iniciarBusqueda(opcion)
# resumen(listado)
print(' ========= EJECUCIÓN FINALIZADA ==========')



