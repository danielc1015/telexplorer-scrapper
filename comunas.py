import os
import json


def cargarArchivo():
    if not os.path.isdir('datos'):
        os.mkdir('datos')
    if os.path.isfile('appdata/comunas.json'):
        print('***********    Bienvenido de Nuevo!    ***********\n')
    else:
        print('***********    Bienvenido!    ***********\n')
        print(' > Creando los archivos necesarios\n')
        crearArchivoNuevo()

    return leerComunaActual()

def crearArchivoNuevo():
    data = {}
    data['comunas'] = []
    data['comunas'].append({
        'id': '1',
        'codigo': '1060418',
        'nombre': 'La Granja'
    })
    data['comunas'].append({
        'id': '2',
        'codigo': '1060419',
        'nombre': 'La Florida'
    })
    
    data['comunaActual'] = {
        'id': '1',
        'codigo': '1060418',
        'nombre': 'La Granja'
    }

    with open('appdata/comunas.json', 'w') as file:
        json.dump(data, file, indent=4)

def leerComunaActual():
    f = open("appdata/comunas.json", "r")
    contenido = f.read()
    jsondecoded = json.loads(contenido)
    return jsondecoded['comunaActual']
    

def agregarComuna():
    print('\n\n\n\n\n\n\n')
    nombre = input(' >> Nombre:  ')
    codigo = input(' >> Codigo:  ')
    f = open("appdata/comunas.json", "r")
    contenido = f.read()
    data = json.loads(contenido)
    ultima = data['comunas'][-1]
    nuevoId = str(int(ultima['id']) + 1)
    nueva = {
        'id': nuevoId,
        'codigo': codigo,
        'nombre': nombre
    }
    data['comunas'].append(nueva)

    with open('appdata/comunas.json', 'w') as file:
        json.dump(data, file, indent=4)
    print('\n ** COMUNA GUARDADA CORRECTAMENTE ** \n\n')

def obtenerListadoComunas():
    f = open("appdata/comunas.json", "r")
    contenido = f.read()
    jsondecoded = json.loads(contenido)
    comunas = jsondecoded['comunas']

    print('\n\n\n\n > Seleccione una comuna \n')
    for comuna in comunas:
        print(comuna['id'] + '. ' + comuna['nombre'])

    return comunas


def cambiarComunaActual(listado, id):
    comunaSeleccionada = {}
    for comuna in listado:
        if comuna['id'] == id:
            comunaSeleccionada = comuna
            break

    f = open("appdata/comunas.json", "r")
    contenido = f.read()
    data = json.loads(contenido)
    data['comunaActual'] = comunaSeleccionada

    with open('appdata/comunas.json', 'w') as file:
        json.dump(data, file, indent=4)

    return comunaSeleccionada




    


