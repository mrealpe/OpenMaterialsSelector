#!/usr/bin/env python
"""
Software for materials selection using Ashby Methodology
chart:  DENSITY vs MODULUS OF E
dataset: datos.csv
"""

import matplotlib.pyplot as plt
import modulos.interfaz as interfaz
import modulos.extraerInformacion as extraerInformacion
import modulos.filtrar as filtrar
import modulos.grafica as grafica

__author__ = "Bruno Paucar, Giovanny Chunga and Miguel Realpe"
__credits__ = ["Bruno Paucar", "Giovanny Chunga", "Miguel Realpe",
                    "Clotario Tapia"]
__license__ = "GNU GPL"
__version__ = "1.0.1"
__maintainer__ = "Miguel Realpe"
__email__ = "mrealpe@fiec.espol.edu.ec"
__status__ = "Prototype"

print('----------SOFTWARE "DENSITY vs MODULUS OF E" CHART----------')

print('Loading Dataset...')
#Cargar materiales de la base de datos
diccionario = extraerInformacion.leerArchivo("datos.csv")

#Extraer los datos de los materiales en listas
listaMateriales,listaTipos,listaDensidad,listaModulo = extraerInformacion.obtenerModuloDensidad(diccionario)
print('Dataset Loaded')

#Obtener todas las variables ingresadas en la interfaz grafica
pendiente,familia,slope_mayor,slope_menor,rigidez,densidad,modulo,densi_mayor,densi_menor,modu_mayor,modu_menor = interfaz.interfaz()

#Filtrar datos por Familia, Modulo, Densidad y Pendiente
listaMaterialesFinal,listaDensidadFinal,listaModuloFinal = filtrar.filtrar(listaMateriales,listaTipos,listaDensidad,listaModulo,familia,densidad,densi_mayor,modulo, modu_mayor,pendiente,rigidez,slope_mayor)

#Si la cantidad de materiales filtrados supera los 500, es preferible utilizar arreglos (procesamiento mas rapido)
#listaMaterialesFinal,listaDensidadFinal,listaModuloFinal = filtrar.filtrarArreglos(listaMateriales,listaTipos,listaDensidad,listaModulo,familia,densidad,densi_mayor,modulo, modu_mayor)

#Graficar valores
g = grafica.grafica(diccionario,listaDensidad,listaModulo,listaMaterialesFinal,listaDensidadFinal,listaModuloFinal,densidad,modulo,rigidez,pendiente)

#reportar resultados
print("Filtrated materials are: ",listaMaterialesFinal)
print("The densities respectives: ",listaDensidadFinal)
print("The modulus respectives: ",listaModuloFinal)
plt.show(g)