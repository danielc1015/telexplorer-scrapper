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
    print ('1. Buscar todas las hojas')
    print ('2. Buscar una hoja')
    opcion = input('Opcion:  ')
    


mostrarMenu()

hoja = input("Ingrese el nombre de la hoja: ")
sheet = excel.leerUnaHoja(hoja)
listado = telexplorer.buscar(sheet)
excel.guardarDatos(listado, hoja)
resumen(listado)



print(' ========= EJECUCIÓN FINALIZADA ==========')



