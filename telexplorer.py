from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome import getChromeDriver

import datos


def buscar(sheet, mitad):
    listaTelefonos = []
    comunaActual = datos.comunaActual

    driver = getChromeDriver()
    driver.get('https://www.telexplorer.cl/')
    for row in sheet:
        actionChains = ActionChains(driver)

        cargada = False

        while not cargada:
            if driver.execute_script('return document.readyState;') == 'complete':
                cargada = True

        direccion = driver.find_element_by_xpath(".//a[text()='Dirección']")

        actionChains.double_click(direccion).perform()


        buscar = driver.find_element_by_id('boton_buscar_3')
        calle = driver.find_element_by_id('calle')
        altura = driver.find_element_by_id('altura')
        provincia = Select(driver.find_element_by_id('provincia2'))

        waitd = WebDriverWait(driver, 15)
        elementd = waitd.until(EC.visibility_of(calle))

        calle.send_keys(row[0].value)
        altura.send_keys(row[1].value)
        provincia.select_by_value('10')
        buscar.click()

        try:
            # localidad = Select(driver.find_element_by_id('localidad'))
            # localidad.select_by_value(comunaActual['codigo'])

            listaTelefonos.append(driver.find_element_by_class_name('resultado_telefono').text)
            print(' > ' + row[0].value + ' ' + str(row[1].value) + ': Teléfono encontrado\n')
        except:
            listaTelefonos.append('-')
            print(' > ' + row[0].value + ' ' + str(row[1].value) + ': Direccion sin teléfono\n')

        driver.get('https://www.telexplorer.cl/')

    driver.close()

    if mitad == 1:
        datos.listado1 = listaTelefonos
    
    if mitad == 2:
        datos.listado2 = listaTelefonos