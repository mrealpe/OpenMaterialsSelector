#!/usr/bin/env python
"""
Provides funtions for loading data from a csv with the format:
    Name,Category,url,Density,Modulus of Elasticity
"""

import csv

__author__ = "Bruno Paucar, Giovanny Chunga and Miguel Realpe"
__credits__ = ["Bruno Paucar", "Giovanny Chunga", "Miguel Realpe",
                    "Clotario Tapia"]
__license__ = "GNU GPL"
__version__ = "1.0.1"
__maintainer__ = "Miguel Realpe"
__email__ = "mrealpe@fiec.espol.edu.ec"
__status__ = "Prototype"


def leerArchivo(archivoCsv):
    archivo = open(archivoCsv,'r',newline = '\n')
    reader = csv.reader(archivo,delimiter = ",", quotechar = '"')
    cabecera = next(reader)
    nombres = []
    tipos = []
    urls = []
    densidades = []
    modulosElasticidad = []
    d1 = {}
    nombresNoValor = []
    for linea in reader:
        nombre,categoria,url,densidad,modulo = linea
        categoria = categoria.split(';')
        if len(categoria) > 1:
            if categoria[0] == 'Ceramic' and categoria[1] == ' Glass':
                tipo = categoria[1][1:]
            else:
                tipo = categoria[0]
        else:
            tipo = categoria[0]
        if densidad == '0' or modulo == '0' or densidad == '' or modulo =='':
            nombresNoValor.append(nombre)
        else:
            nombres.append(nombre)
            tipos.append(tipo)
            urls.append(url)
            densidades.append(float(densidad))
            modulosElasticidad.append(float(modulo))
    for i in range(len(nombres)):
        d2 = {}
        d2["Family"] = tipos[i]
        d2["Density"] = densidades[i]
        d2["Modulus of Elasticity"] = modulosElasticidad[i]
        d2["Url"] = urls[i]
        d1[nombres[i]] = d2
    archivo.close()
    return(d1)

def obtenerModuloDensidad(dic):
    listaM = []
    listaDensidad = []
    listaModulo = []
    listaTipo = []
    for clave,valor in dic.items():
        listaM = list(dic.keys())
        listaDensidad.append(dic[clave]["Density"])
        listaModulo.append(dic[clave]["Modulus of Elasticity"])
        listaTipo.append(dic[clave]["Family"])
    return listaM,listaTipo,listaDensidad,listaModulo