import excel
import telexplorer
import threading
import telefonos

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
    


def evaluarOpcion(opcion):
    if opcion == '1':
        hoja = input("Ingrese el nombre de la hoja: ")
        iniciarBusqueda(hoja)

    if opcion == '2':
        sheets = excel.obtenerNombresSheets()
        for hoja in sheets:
            iniciarBusqueda(hoja)



def iniciarBusqueda(hoja):
    print('\n\n\n\n\n\n\n\n')
    print('*********************************************')
    print( ' >>  HOJA: ' + hoja)
    print('*********************************************')

    sheet = excel.leerUnaHoja(hoja)
    largo = len(sheet)
    mitad = int (largo / 2)

    sheetMitad1 = sheet[0:(mitad)]
    sheetMitad2 = sheet[mitad:(largo)]

    thread1 = threading.Thread(target=telexplorer.buscar, args=(sheetMitad1, 1))
    thread2 = threading.Thread(target=telexplorer.buscar, args=(sheetMitad2, 2))
    thread1.start()
    thread2.start()

    telefonosParte1 = thread1.join()
    telefonosParte2 = thread2.join()

    listado = telefonos.listado1 + telefonos.listado2

    excel.guardarDatos(listado, hoja)




opcion = mostrarMenu()
evaluarOpcion(opcion)
# resumen(listado)
print(' ========= EJECUCIÓN FINALIZADA ==========')



