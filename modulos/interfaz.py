"""
def Provides interface for Ashby Methodology
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

__author__ = "Bruno Paucar, Giovanny Chunga and Miguel Realpe"
__credits__ = ["Bruno Paucar", "Giovanny Chunga", "Miguel Realpe",
                    "Clotario Tapia"]
__license__ = "GNU GPL"
__version__ = "1.0.1"
__maintainer__ = "Miguel Realpe"
__email__ = "mrealpe@fiec.espol.edu.ec"
__status__ = "Prototype"



def interfaz():

    def closeProgram():
        exit()

    interfaz = tk.Tk()
    interfaz.title("Density vs Yougn's Modulus Charts")
    interfaz.geometry('360x380')
    interfaz.protocol('WM_DELETE_WINDOW', closeProgram)

    # firts linea
    title = ttk.Label(interfaz, text='Select the options to optimize the values').place(x=70, y=0)
    # slope
    pendiente = ttk.Label(interfaz, text='Slope').place(x=20, y=40)


    combo_slope = ttk.Combobox(interfaz, width=9, state='readonly')
    combo_slope.place(x=80, y=40)
    combo_slope['values'] = (1, 2, 3)
    combo_slope.set(1)
    # family
    familia = ttk.Label(interfaz, text='Family').place(x=20, y=70)
    combo_family = ttk.Combobox(interfaz, width=22, state='readonly')
    combo_family.place(x=80, y=70)
    combo_family['values'] = ("Carbon","Ceramic", "Glass", "Fluid", "Metal", "Other Engineering Material", "Polymer","Pure Element", "Wood and Natural Products")
    combo_family.current(4)
    # stiffness info
    stifness_name = ttk.Label(interfaz, text='Stiffness').place(x=20, y=100)
    stif_entry = ttk.Entry(interfaz, width=12)
    stif_entry.place(x=80, y=100)
    stif_entry.insert(0, 0.0)
    check_value5 = tk.IntVar()
    slope_mayor5 = ttk.Radiobutton(interfaz, text='Higher values',value=1,variable=check_value5).place(x=25, y=130)
    slope_menor6 = ttk.Radiobutton(interfaz, text='Lower values', value=0,variable=check_value5).place(x=150, y=130)
    # Density info
    second_title = ttk.Label(interfaz, text='General property ').place(x=15, y=155)
    density_name = ttk.Label(interfaz, text='Density').place(x=20, y=180)
    density_entry = ttk.Entry(interfaz, width=12)
    density_entry.place(x=80, y=180)
    density_entry.insert(0, 0.0)
    densityDimensional = ttk.Label(interfaz, text='kg/m^3').place(x=170, y=180)

    check_value1 = tk.IntVar()
    density_mayor1 = ttk.Radiobutton(interfaz, text='Higher values', value = 1,variable = check_value1).place(x=25, y=210)
    density_menor2 = ttk.Radiobutton(interfaz, text='Lower values', value = 0 ,variable = check_value1).place(x=150, y=210)
    # Modulus info
    thrid_title = ttk.Label(interfaz, text='Mechanical property').place(x=15, y=240)
    modulus_name = ttk.Label(interfaz, text='Modulus of Elasticity').place(x=15, y=265)
    modulus_entry = ttk.Entry(interfaz, width=12)
    modulus_entry.place(x=150, y=265)
    modulus_entry.insert(0, 0.0)
    modulusDimensional = ttk.Label(interfaz, text='GPa').place(x=238, y=265)

    check_value3 = tk.IntVar()
    modulus_mayor3 = ttk.Radiobutton(interfaz, text='Higher values', value=1,variable=check_value3).place(x=25, y=290)
    modulus_menor4 = ttk.Radiobutton(interfaz, text='Lower values', value=0 ,variable=check_value3).place(x=150, y=290)

    # buttons
    def action():
        messagebox.showinfo('PAY ATTENTION',"There are many ways to select the options, if you let the box empty ('') it will plot a predeterminated value, if you let '0.0' means no straight plot.")
        print(
            'Has chosen an index of ' + '"' + combo_slope.get() + '"' + ' to optimize stiffness  with  a value ' + '"' + stif_entry.get() + '"' + ', to optimize density with ' + '"' + density_entry.get() + '"' + ' and modulus of elasticity with ' + '"' + modulus_entry.get() + '"' + ', with higher, lower or both values.')
        print('The material belongs to the family of ' + '"' + combo_family.get() + '".')

    boton1 = ttk.Button(interfaz, text='Submit', command=action)
    boton1.place(x=20, y=330)

    boton2 = ttk.Button(interfaz, text='Continue', command=interfaz.quit)
    boton2.place(x=270, y=330)

    def call():
        messagebox.showinfo('IMPORTANT','''You're able to  select at most 3 options(stiffness-density-modulus) with a different slope for each one, choose a family of material, enter only numbers, and select higher or lower values.''')

    boton3 = ttk.Button(interfaz, text='Info', command=call)
    boton3.place(x=270, y=40)

    interfaz.mainloop()
    pendiente = int(combo_slope.get())
    familia = str(combo_family.get())
    slope_valor = bool(check_value5.get())
    rigidez = float(stif_entry.get())
    densidad = float(density_entry.get())
    modulo = float(modulus_entry.get())
    densi_valor = bool(check_value1.get())
    modu_valor= bool(check_value3.get())
    interfaz.destroy()

    return pendiente,familia,slope_valor,0,rigidez,densidad,modulo,densi_valor,0,modu_valor,0