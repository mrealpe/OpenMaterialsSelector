#!/usr/bin/env python
"""
Provides funtions for writing a file named with the type of filtered material(slope #) with the format:
    Value for Stiffness,Value for Density,Value for Modulus of Elasticity
    if they are higher or lower respect the value choice; example: higher,lower,higher
    Name,Density,Modulus of Elasticity (for all filtered material)
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

def escribirArchivos(listaMaterialesFinal,listaDensidadFinal,listaModuloFinal,familia,rigidez,densidad,modulo,slope_valor,densi_valor,modu_valor,pendiente):
    stiffness_ = ""
    densi_ = ""
    modu_ = ""
    if slope_valor == 1:
        stiffness_ += "Higher values for stiffness"
    else:
        stiffness_ += "Lower values for stiffness"
    if densi_valor == 1:
        densi_ += "Higher values for density"
    else:
        densi_ += "Lower values for density"
    if modu_valor == 1:
        modu_ += "Higher values for modulus of elasticity"
    else:
        modu_ += "Lower values for modulus of elasticity"
    nombre = "{}(slope {},stiffnees {},density {},modulus of elasticity {}).csv".format(familia, pendiente, rigidez,
                                                                                        densidad, modulo)

    archivo = open(nombre, 'w', newline="\n")
    writer = csv.writer(archivo, delimiter=',', quotechar='"')

    writer.writerow(["---- Descripcion ----"])
    writer.writerow(["Value for stiffness: {} --- Value for Density: {} ---- Value for Modulus of Elasticity: {}".format(rigidez,densidad,modulo)])
    writer.writerow(["{} --- {} ---- {}".format(stiffness_, densi_, modu_)])
    #archivoF.write("{}\t{}\t{}\n".format(stiffness_,densi_,modu_))
    writer.writerow(["---- Datos ----"])
    writer.writerow(["name","density","modulus of elasticity"])
    for contador in range(len(listaMaterialesFinal)):
        lista = [listaMaterialesFinal[contador],listaDensidadFinal[contador],listaModuloFinal[contador]]
        writer.writerow(lista)
    archivo.close()