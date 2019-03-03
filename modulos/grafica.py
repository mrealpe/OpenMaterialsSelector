#!/usr/bin/env python
"""
Provides funtions for plotting chart of "DENSITY vs MODULUS OF E" for Ashby Methodology.
"""

import matplotlib.pyplot as plt
import numpy as np

__author__ = "Bruno Paucar, Giovanny Chunga and Miguel Realpe"
__credits__ = ["Bruno Paucar", "Giovanny Chunga", "Miguel Realpe",
                    "Clotario Tapia"]
__license__ = "GNU GPL"
__version__ = "1.0.1"
__maintainer__ = "Miguel Realpe"
__email__ = "mrealpe@fiec.espol.edu.ec"
__status__ = "Prototype"

def recta1(n):
    x= np.linspace(0.0001,1000)
    y = n * x
    plt.loglog(x,y,'-', label='E/ρ,{}'.format(n))

def recta2(n):
    x = np.linspace(0.0001,1000)
    y = (n * x)**2
    plt.loglog(x, y, '-', label='E^(1/2)/ρ,{}'.format(n))

def recta3(n):
    x = np.linspace(0.0001,1000)
    y = (n * x) ** 3
    plt.loglog(x, y, '-', label='E^(1/3)/ρ,{}'.format(n))

def densidadVertical(densidad,maximoD):
    plt.loglog([densidad,densidad],[0,maximoD],'c')

def ModuloHorizontal(modulo,maximoModulo):
    plt.loglog([0,maximoModulo],[modulo,modulo], 'c')

def grafica(diccionario,listaDensidad,listaModulo,listaMaterialesFiltrada,listaDensidadFiltrada,listaModuloFiltrada,densidad,modulo,rigidez,pendiente):
    leyendaFamilias={'Glass':'m.',
                     'Ceramic': 'c.',
                     'Carbon': 'k+',
                     'Metal':'r.',
                     'Wood and Natural Products': 'g+',
                     'Polymer':'y.',
                     'Fluid':'b.',
                     'Pure Element':'r+',
                     'Other Engineering Material':'c^'}
    #gráfico 1
    plt.figure('Gráfico 1')
    plt.title('Grafico de Ashby')
    tipos = []
    for claves, datos in diccionario.items():
        familia = datos['Family']
        density = datos['Density']
        modulus = datos['Modulus of Elasticity']
        signo=leyendaFamilias.get(familia,'bX')
        plt.plot(density, modulus, signo)
        if familia not in tipos:
            tipos.append(familia)
            plt.plot(density, modulus, signo,label=familia)
    if pendiente == 1:
        recta1(rigidez)
    elif pendiente == 2:
        recta2(rigidez)
    elif pendiente == 3:
        recta3(rigidez)
    densidadVertical(densidad, max(listaModulo))
    ModuloHorizontal(modulo, max(listaDensidad))
    plt.xlabel('Density')
    plt.ylabel('Modulus of Elasticity')
    plt.legend(loc='upper left')

    #grafico 2
    plt.figure('Gráfico 2')
    plt.title('Materiales Filtrados')
    tipos = []
    for indiceFiltrada in range(len(listaMaterialesFiltrada)):
        familia = diccionario[listaMaterialesFiltrada[indiceFiltrada]]['Family']
        density = listaDensidadFiltrada[indiceFiltrada]
        modulus = listaModuloFiltrada[indiceFiltrada]
        signo=leyendaFamilias.get(familia,'bX')
        plt.plot(density, modulus, signo)
        #plt.text(density, modulus, '{}'.format(listaMaterialesFiltrada[indiceFiltrada]))
        if familia not in tipos:
            tipos.append(familia)
            plt.plot(density, modulus, signo,label=familia)
    if pendiente == 1:
        recta1(rigidez)
    elif pendiente == 2:
        recta2(rigidez)
    elif pendiente == 3:
        recta3(rigidez)
    densidadVertical(densidad, max(listaModulo))
    ModuloHorizontal(modulo, max(listaDensidad))
    plt.xlabel('Density')
    plt.ylabel('Modulus of Elasticity')
    plt.legend(loc='upper left')