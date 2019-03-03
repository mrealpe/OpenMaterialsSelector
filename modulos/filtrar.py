#!/usr/bin/env python
"""
Provides filter funtions for Ashby Methodology
"""

import numpy as np

__author__ = "Bruno Paucar, Giovanny Chunga and Miguel Realpe"
__credits__ = ["Bruno Paucar", "Giovanny Chunga", "Miguel Realpe",
                    "Clotario Tapia"]
__license__ = "GNU GPL"
__version__ = "1.0.1"
__maintainer__ = "Miguel Realpe"
__email__ = "mrealpe@fiec.espol.edu.ec"
__status__ = "Prototype"


def filtrarTipo(listaMateriales,listaTipos,listaDensidades,listaModulos,tipo):
    listaM = []
    listaDensidad = []
    listaModulo = []
    for i in range(len(listaMateriales)):
        if listaTipos[i] == tipo :
            listaM.append(listaMateriales[i])
            listaDensidad.append(listaDensidades[i])
            listaModulo.append(listaModulos[i])
    return listaM,listaDensidad,listaModulo

def filtradoDensidad(listaMateriales,listaDensidad,listaModulo,densidad,densi_mayor):
    listaMateriales1 = []
    listaDensidad1 = []
    listaModulos1 = []
    for i in range(len(listaDensidad)):
        if densi_mayor and listaDensidad[i] > densidad:
                listaDensidad1.append(listaDensidad[i])
                listaMateriales1.append(listaMateriales[i])
                listaModulos1.append(listaModulo[i])
        elif not densi_mayor and listaDensidad[i] < densidad:
                listaDensidad1.append(listaDensidad[i])
                listaMateriales1.append(listaMateriales[i])
                listaModulos1.append(listaModulo[i])
    return listaMateriales1,listaDensidad1,listaModulos1

def filtradoModulo(listaMateriales,listaDensidad,listaModulo,modulo,modu_mayor):
    listaMateriales1 = []
    listaDensidad1 = []
    listaModulos1 = []
    for i in range(len(listaDensidad)):
        if modu_mayor and listaDensidad[i] > modulo:
                listaDensidad1.append(listaDensidad[i])
                listaMateriales1.append(listaMateriales[i])
                listaModulos1.append(listaModulo[i])
        elif not modu_mayor and listaDensidad[i] < modulo:
                listaDensidad1.append(listaDensidad[i])
                listaMateriales1.append(listaMateriales[i])
                listaModulos1.append(listaModulo[i])
    return listaMateriales1,listaDensidad1,listaModulos1

def filtradoModulo(listaMateriales,listaDensidad,listaModulo,modulo,modu_mayor):
    listaMateriales2 = []
    listaDensidad2 = []
    listaModulos2 = []
    if modu_mayor:
        for i in range(len(listaModulo)):
            if listaModulo[i] > modulo:
                listaDensidad2.append(listaDensidad[i])
                listaMateriales2.append(listaMateriales[i])
                listaModulos2.append(listaModulo[i])
    else:
        for i in range(len(listaModulo)):
            if listaModulo[i] < modulo:
                listaDensidad2.append(listaDensidad[i])
                listaMateriales2.append(listaMateriales[i])
                listaModulos2.append(listaModulo[i])
    return listaMateriales2,listaDensidad2,listaModulos2

def filtrarMateriales(listaMateriales,listaDensidad,listaModulo,pendiente,valor,slope_mayor):
    listaM2, listaD2, listaMod2 = [], [], []
    if pendiente == 1:
        if slope_mayor:
            for i in range(len(listaMateriales)):
                if listaModulo[i] > valor * listaDensidad[i]:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
        else:
            for i in range(len(listaMateriales)):
                if listaModulo[i] < valor * listaDensidad[i]:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
    elif pendiente == 2:
        if slope_mayor:
            for i in range(len(listaMateriales)):
                if listaModulo[i] > (valor * listaDensidad[i])**2:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
        else:
            for i in range(len(listaMateriales)):
                if listaModulo[i] < (valor * listaDensidad[i])**2:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
    elif pendiente == 3:
        if slope_mayor:
            for i in range(len(listaMateriales)):
                if listaModulo[i] > (valor * listaDensidad[i])**3:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
        else:
            for i in range(len(listaMateriales)):
                if listaModulo[i] < (valor * listaDensidad[i])**3:
                    listaM2.append(listaMateriales[i])
                    listaD2.append(listaDensidad[i])
                    listaMod2.append(listaModulo[i])
    return listaM2, listaD2, listaMod2


def filtrar(listaMateriales,listaTipos,listaDensidades,listaModulos,tipo,densidad,densi_mayor,modulo, modu_mayor,pendiente, rigidez,slope_mayor):
    listaMateriales2, listaDensidad2, listaModulo2 = filtrarTipo(listaMateriales, listaTipos, listaDensidades,listaModulos, tipo)
    listaMateriales3, listaDensidad3, listaModulo3 = filtradoDensidad(listaMateriales2, listaDensidad2,listaModulo2, densidad, densi_mayor)
    listaMateriales4, listaDensidad4, listaModulo4 = filtradoModulo(listaMateriales3, listaDensidad3,listaModulo3, modulo, modu_mayor)
    listaMaterialesFinal,listaDensidadFinal,listaModuloFinal  = filtrarMateriales(listaMateriales4,listaDensidad4, listaModulo4,pendiente, rigidez,slope_mayor)
    return listaMaterialesFinal,listaDensidadFinal,listaModuloFinal


#Cuando se tienen mas de 10k materiales en total o se esperan mas de 500 filtrados es preferible utilizar el filtro por arreglos
def filtrarArreglos(listaMateriales,listaTipos,listaDensidades,listaModulos,tipo,densidad,densi_mayor,modulo, modu_mayor):
    arregloMateriales = np.array(listaMateriales)
    arregloTipos = np.array(listaTipos)
    arregloDensidades = np.array(listaDensidades)
    arregloModulos = np.array(listaModulos)
    condicion1=arregloTipos==tipo
    if densi_mayor:
        condicion2 = arregloDensidades > densidad
    else:
        condicion2 = arregloDensidades < densidad
    if modu_mayor:
        condicion3 = arregloModulos > modulo
    else:
        condicion3 = arregloModulos < modulo
    return arregloMateriales[(condicion1)&(condicion2)&(condicion3)],\
           arregloDensidades[(condicion1)&(condicion2)&(condicion3)],\
           arregloModulos[(condicion1)&(condicion2)&(condicion3)]
