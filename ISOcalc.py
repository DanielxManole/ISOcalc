import tkinter as interfata
from tkinter import ttk as tema_interfata
from tkinter import messagebox as casuta_dialog
import math
import numpy

def update_zona_toleranta(event):
    selectie = tip_dinGUI.curselection()
    if selectie:
        tip_ales.set(tip_dinGUI.get(selectie[0]))
        if tip_ales.get() == "Alezaj":
            zona_dinGUI['values'] = ("A", "B", "C", "CD", "D", "E", "EF", "F", "FG", "G", "H", "JS", "J", "K", "M", "N", "P", "R", "S", "T", "U", "V", "X", "Y", "Z", "ZA", "ZB", "ZC")
        elif tip_ales.get() == "Arbore":
            zona_dinGUI['values'] = ("a", "b", "c", "cd", "d", "e", "ef", "f", "fg", "g", "h", "js", "j", "k", "m", "n", "p", "r", "s", "t", "u", "v", "x", "y", "z", "za", "zb", "zc")
        zona_dinGUI.current(10)
        if not clasa_dinGUI.get():
            clasa_dinGUI.current(8)

def reset():
    dnom_dinGUI.delete(0, 'end')
    dnom_dinGUI.insert(0, '10')

    tip_dinGUI.selection_clear(0, 'end')
    
    zona_dinGUI.set('')
    
    clasa_dinGUI.set('')
    
    toldim_dinGUI.config(state="normal")
    toldim_dinGUI.delete(0, 'end')
    toldim_dinGUI.config(state="readonly")
    
    abateresup_dinGUI.config(state="normal")
    abateresup_dinGUI.delete(0, 'end')
    abateresup_dinGUI.config(state="readonly")
    
    abatereinf_dinGUI.config(state="normal")
    abatereinf_dinGUI.delete(0, 'end')
    abatereinf_dinGUI.config(state="readonly")

def calculare():
    try:
        dimensiune = float(dnom_dinGUI.get())
        tip = tip_ales.get()
        zona = zona_dinGUI.get()
        clasa = clasa_dinGUI.get()

        abaterea_superioara = float("NaN")
        abaterea_inferioara = float("NaN")

        print(dimensiune, tip, zona, clasa)

        if dimensiune <= 0 or dimensiune>3500:
            casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!", 
                                    "Dimensiunea nominală trebuie să fie un număr pozitiv de maxim 3150 mm!")
            return
        if dimensiune <= 1 and int(clasa) in range(14, 19):
            casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                    "Treptele de toleranțe de la IT14 până la IT18, inclusiv, nu trebuie utilizate pentru dimensiuni nominale mai mici sau egale cu 1 mm!")
            return
        if not clasa:
            casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!", 
                                    "Trebuie selectată clasa de precizie pentru a continua!")
            return
        if not tip:
            casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                    "Alegeți tipul dimensiunii! (Alezaj / Arbore)")
            return
        
        if dimensiune >0 and dimensiune <=3:
            if clasa == "01":
                toleranta_dimensionala = 0.0003
            elif clasa == "0":
                toleranta_dimensionala = 0.0005
            elif clasa == "1":
                toleranta_dimensionala = 0.0008
            elif clasa == "2":
                toleranta_dimensionala = 0.0012
            elif clasa == "3":
                toleranta_dimensionala = 0.002
            elif clasa == "4":
                toleranta_dimensionala = 0.003
            elif clasa == "5":
                toleranta_dimensionala = 0.004
            elif clasa == "6":
                toleranta_dimensionala = 0.006
            elif clasa == "7":
                toleranta_dimensionala = 0.01
            elif clasa == "8":
                toleranta_dimensionala = 0.014
            elif clasa == "9":
                toleranta_dimensionala = 0.025
            elif clasa == "10":
                toleranta_dimensionala = 0.04
            elif clasa == "11":
                toleranta_dimensionala = 0.06
            elif clasa == "12":
                toleranta_dimensionala = 0.1
            elif clasa == "13":
                toleranta_dimensionala = 0.14
            elif clasa == "14":
                toleranta_dimensionala = 0.25
            elif clasa == "15":
                toleranta_dimensionala = 0.4
            elif clasa == "16":
                toleranta_dimensionala = 0.6
            elif clasa == "17":
                toleranta_dimensionala = 1
            elif clasa == "18":
                toleranta_dimensionala = 1.4
            if dimensiune <= 1 and (zona == "a" or zona == "A" or zona == "b" or zona == "B"):
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Abaterile fundamentale a și b, respectiv A și B nu trebuie utilizate pentru dimensiuni nominale mai mici sau egale cu 1 mm!")
                return
            if dimensiune <= 1 and (zona == "N" and int(clasa) >8):
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Abaterea fundamentală N pentru trepte de toleranțe peste IT8 nu trebuie utilizată pentru dimensiuni nominale mai mici sau egale cu 1 mm!")
                return
            if tip == "Alezaj":
                if zona == "A":
                    abaterea_inferioara = 0.27
                elif zona == "B":
                    abaterea_inferioara = 0.14
                elif zona == "C":
                    abaterea_inferioara = 0.06
                elif zona == "CD":
                    abaterea_inferioara = 0.034
                elif zona == "D":
                    abaterea_inferioara = 0.02
                elif zona == "E":
                    abaterea_inferioara = 0.014
                elif zona == "EF":
                    abaterea_inferioara = 0.01
                elif zona == "F":
                    abaterea_inferioara = 0.006
                elif zona == "FG":
                    abaterea_inferioara = 0.004
                elif zona == "G":
                    abaterea_inferioara = 0.002
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.002
                    elif clasa == "7":
                        abaterea_superioara = 0.004
                    elif clasa == "8":
                        abaterea_superioara = 0.006
                elif zona == "K":
                    abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.002
                elif zona == "N":
                    if int(clasa) <= 8:
                        abaterea_superioara = -0.004
                    else:
                        abaterea_superioara = 0
                elif zona == "P":
                    abaterea_superioara = -0.006
                elif zona == "R":
                    abaterea_superioara = -0.01
                elif zona == "S":
                    abaterea_superioara = -0.014
                elif zona == "U":
                    abaterea_superioara = -0.018
                elif zona == "X":
                    abaterea_superioara = -0.02
                elif zona == "Z":
                    abaterea_superioara = -0.026
                elif zona == "ZA":
                    abaterea_superioara = -0.032
                elif zona == "ZB":
                    abaterea_superioara = -0.04
                elif zona == "ZC":
                    abaterea_superioara = -0.06
            elif tip == "Arbore":
                if zona == "a":
                    abaterea_superioara = -0.27
                elif zona == "b":
                    abaterea_superioara = -0.14
                elif zona == "c":
                    abaterea_superioara = -0.06
                elif zona == "cd":
                    abaterea_superioara = -0.034
                elif zona == "d":
                    abaterea_superioara = -0.02
                elif zona == "e":
                    abaterea_superioara = -0.014
                elif zona == "ef":
                    abaterea_superioara = -0.01
                elif zona == "f":
                    abaterea_superioara = -0.006
                elif zona == "fg":
                    abaterea_superioara = -0.004
                elif zona == "g":
                    abaterea_superioara = -0.002
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.002
                    elif clasa == "7":
                        abaterea_inferioara = -0.004
                    elif clasa == "8":
                        abaterea_inferioara = -0.006
                elif zona == "k":
                    abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.002
                elif zona == "n":
                    abaterea_inferioara = 0.004
                elif zona == "p":
                    abaterea_inferioara = 0.006
                elif zona == "r":
                    abaterea_inferioara = 0.01
                elif zona == "s":
                    abaterea_inferioara = 0.014
                elif zona == "u":
                    abaterea_inferioara = 0.018
                elif zona == "x":
                    abaterea_inferioara = 0.02
                elif zona == "z":
                    abaterea_inferioara = 0.026
                elif zona == "za":
                    abaterea_inferioara = 0.032
                elif zona == "zb":
                    abaterea_inferioara = 0.04
                elif zona == "zc":
                    abaterea_inferioara = 0.06
        elif dimensiune >3 and dimensiune <=6:
            if clasa == "01":
                toleranta_dimensionala = 0.0004
            elif clasa == "0":
                toleranta_dimensionala = 0.0006
            elif clasa == "1":
                toleranta_dimensionala = 0.001
            elif clasa == "2":
                toleranta_dimensionala = 0.0015
            elif clasa == "3":
                toleranta_dimensionala = 0.0025
            elif clasa == "4":
                toleranta_dimensionala = 0.004
            elif clasa == "5":
                toleranta_dimensionala = 0.005
            elif clasa == "6":
                toleranta_dimensionala = 0.008
            elif clasa == "7":
                toleranta_dimensionala = 0.012
            elif clasa == "8":
                toleranta_dimensionala = 0.018
            elif clasa == "9":
                toleranta_dimensionala = 0.03
            elif clasa == "10":
                toleranta_dimensionala = 0.048
            elif clasa == "11":
                toleranta_dimensionala = 0.075
            elif clasa == "12":
                toleranta_dimensionala = 0.12
            elif clasa == "13":
                toleranta_dimensionala = 0.18
            elif clasa == "14":
                toleranta_dimensionala = 0.3
            elif clasa == "15":
                toleranta_dimensionala = 0.48
            elif clasa == "16":
                toleranta_dimensionala = 0.75
            elif clasa == "17":
                toleranta_dimensionala = 1.2
            elif clasa == "18":
                toleranta_dimensionala = 1.8
            if tip == "Alezaj":
                if zona == "A":
                    abaterea_inferioara = 0.27
                elif zona == "B":
                    abaterea_inferioara = 0.14
                elif zona == "C":
                    abaterea_inferioara = 0.07
                elif zona == "CD":
                    abaterea_inferioara = 0.046
                elif zona == "D":
                    abaterea_inferioara = 0.03
                elif zona == "E":
                    abaterea_inferioara = 0.02
                elif zona == "EF":
                    abaterea_inferioara = 0.014
                elif zona == "F":
                    abaterea_inferioara = 0.01
                elif zona == "FG":
                    abaterea_inferioara = 0.006
                elif zona == "G":
                    abaterea_inferioara = 0.004
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.005
                    elif clasa == "7":
                        abaterea_superioara = 0.006
                    elif clasa == "8":
                        abaterea_superioara = 0.01
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.001
                    elif clasa == "3":
                        abaterea_superioara = -0.001 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.001 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.001 + 0.001
                    elif clasa == "6":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.001 + 0.004
                    elif clasa == "8":
                        abaterea_superioara = -0.001 + 0.006
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.004
                    elif clasa == "3":
                        abaterea_superioara = -0.004 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.004 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.004 + 0.001
                    elif clasa == "6":
                        abaterea_superioara = -0.004 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "8":
                        abaterea_superioara = -0.004 + 0.006
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.008
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.008 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.008 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.008 + 0.001
                    elif clasa == "6":
                        abaterea_superioara = -0.008 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.008 + 0.004
                    elif clasa == "8":
                        abaterea_superioara = -0.008 + 0.006
                elif zona == "P":
                    abaterea_superioara = -0.012
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "R":
                    abaterea_superioara = -0.015
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "S":
                    abaterea_superioara = -0.019
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "U":
                    abaterea_superioara = -0.023
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "X":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "Z":
                    abaterea_superioara = -0.035
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "ZA":
                    abaterea_superioara = -0.042
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "ZB":
                    abaterea_superioara = -0.05
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
                elif zona == "ZC":
                    abaterea_superioara = -0.08
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.001
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.004
                    if clasa == "8":
                        abaterea_superioara += 0.006
            elif tip == "Arbore":
                if zona == "a":
                    abaterea_superioara = -0.27
                elif zona == "b":
                    abaterea_superioara = -0.14
                elif zona == "c":
                    abaterea_superioara = -0.07
                elif zona == "cd":
                    abaterea_superioara = -0.046
                elif zona == "d":
                    abaterea_superioara = -0.03
                elif zona == "e":
                    abaterea_superioara = -0.02
                elif zona == "ef":
                    abaterea_superioara = -0.014
                elif zona == "f":
                    abaterea_superioara = -0.01
                elif zona == "fg":
                    abaterea_superioara = -0.006
                elif zona == "g":
                    abaterea_superioara = -0.004
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.002
                    elif clasa == "7":
                        abaterea_inferioara = -0.004
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.001
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.004
                elif zona == "n":
                    abaterea_inferioara = 0.008
                elif zona == "p":
                    abaterea_inferioara = 0.012
                elif zona == "r":
                    abaterea_inferioara = 0.015
                elif zona == "s":
                    abaterea_inferioara = 0.019
                elif zona == "u":
                    abaterea_inferioara = 0.023
                elif zona == "x":
                    abaterea_inferioara = 0.028
                elif zona == "z":
                    abaterea_inferioara = 0.035
                elif zona == "za":
                    abaterea_inferioara = 0.042
                elif zona == "zb":
                    abaterea_inferioara = 0.05
                elif zona == "zc":
                    abaterea_inferioara = 0.08
        elif dimensiune >6 and dimensiune <=10:
            if clasa == "01":
                toleranta_dimensionala = 0.0004
            elif clasa == "0":
                toleranta_dimensionala = 0.0006
            elif clasa == "1":
                toleranta_dimensionala = 0.001
            elif clasa == "2":
                toleranta_dimensionala = 0.0015
            elif clasa == "3":
                toleranta_dimensionala = 0.0025
            elif clasa == "4":
                toleranta_dimensionala = 0.004
            elif clasa == "5":
                toleranta_dimensionala = 0.006
            elif clasa == "6":
                toleranta_dimensionala = 0.009
            elif clasa == "7":
                toleranta_dimensionala = 0.015
            elif clasa == "8":
                toleranta_dimensionala = 0.022
            elif clasa == "9":
                toleranta_dimensionala = 0.036
            elif clasa == "10":
                toleranta_dimensionala = 0.058
            elif clasa == "11":
                toleranta_dimensionala = 0.09
            elif clasa == "12":
                toleranta_dimensionala = 0.15
            elif clasa == "13":
                toleranta_dimensionala = 0.22
            elif clasa == "14":
                toleranta_dimensionala = 0.36
            elif clasa == "15":
                toleranta_dimensionala = 0.58
            elif clasa == "16":
                toleranta_dimensionala = 0.9
            elif clasa == "17":
                toleranta_dimensionala = 1.5
            elif clasa == "18":
                toleranta_dimensionala = 2.2
            if tip == "Alezaj":
                if zona == "A":
                    abaterea_inferioara = 0.28
                elif zona == "B":
                    abaterea_inferioara = 0.15
                elif zona == "C":
                    abaterea_inferioara = 0.08
                elif zona == "CD":
                    abaterea_inferioara = 0.056
                elif zona == "D":
                    abaterea_inferioara = 0.04
                elif zona == "E":
                    abaterea_inferioara = 0.025
                elif zona == "EF":
                    abaterea_inferioara = 0.018
                elif zona == "F":
                    abaterea_inferioara = 0.013
                elif zona == "FG":
                    abaterea_inferioara = 0.008
                elif zona == "G":
                    abaterea_inferioara = 0.005
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.005
                    elif clasa == "7":
                        abaterea_superioara = 0.008
                    elif clasa == "8":
                        abaterea_superioara = 0.012
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.001
                    elif clasa == "3":
                        abaterea_superioara = -0.001 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.001 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.001 + 0.002
                    elif clasa == "6":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.001 + 0.006
                    elif clasa == "8":
                        abaterea_superioara = -0.001 + 0.007
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.006
                    elif clasa == "3":
                        abaterea_superioara = -0.006 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.006 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.006 + 0.002
                    elif clasa == "6":
                        abaterea_superioara = -0.006 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.006 + 0.006
                    elif clasa == "8":
                        abaterea_superioara = -0.006 + 0.007
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.01
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.01 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.01 + 0.0015
                    elif clasa == "5":
                        abaterea_superioara = -0.01 + 0.002
                    elif clasa == "6":
                        abaterea_superioara = -0.01 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.01 + 0.006
                    elif clasa == "8":
                        abaterea_superioara = -0.01 + 0.007
                elif zona == "P":
                    abaterea_superioara = -0.015
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "R":
                    abaterea_superioara = -0.019
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "S":
                    abaterea_superioara = -0.023
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "U":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "X":
                    abaterea_superioara = -0.034
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "Z":
                    abaterea_superioara = -0.042
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "ZA":
                    abaterea_superioara = -0.052
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "ZB":
                    abaterea_superioara = -0.067
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
                elif zona == "ZC":
                    abaterea_superioara = -0.097
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.0015
                    if clasa == "5":
                        abaterea_superioara += 0.002
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.006
                    if clasa == "8":
                        abaterea_superioara += 0.007
            elif tip == "Arbore":
                if zona == "a":
                    abaterea_superioara = -0.28
                elif zona == "b":
                    abaterea_superioara = -0.15
                elif zona == "c":
                    abaterea_superioara = -0.08
                elif zona == "cd":
                    abaterea_superioara = -0.056
                elif zona == "d":
                    abaterea_superioara = -0.04
                elif zona == "e":
                    abaterea_superioara = -0.025
                elif zona == "ef":
                    abaterea_superioara = -0.018
                elif zona == "f":
                    abaterea_superioara = -0.013
                elif zona == "fg":
                    abaterea_superioara = -0.008
                elif zona == "g":
                    abaterea_superioara = -0.005
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.002
                    elif clasa == "7":
                        abaterea_inferioara = -0.005
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.001
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.006
                elif zona == "n":
                    abaterea_inferioara = 0.01
                elif zona == "p":
                    abaterea_inferioara = 0.015
                elif zona == "r":
                    abaterea_inferioara = 0.019
                elif zona == "s":
                    abaterea_inferioara = 0.023
                elif zona == "u":
                    abaterea_inferioara = 0.028
                elif zona == "x":
                    abaterea_inferioara = 0.034
                elif zona == "z":
                    abaterea_inferioara = 0.042
                elif zona == "za":
                    abaterea_inferioara = 0.052
                elif zona == "zb":
                    abaterea_inferioara = 0.067
                elif zona == "zc":
                    abaterea_inferioara = 0.097
        elif dimensiune >10 and dimensiune <=18:
            if clasa == "01":
                toleranta_dimensionala = 0.0005
            elif clasa == "0":
                toleranta_dimensionala = 0.0008
            elif clasa == "1":
                toleranta_dimensionala = 0.0012
            elif clasa == "2":
                toleranta_dimensionala = 0.002
            elif clasa == "3":
                toleranta_dimensionala = 0.003
            elif clasa == "4":
                toleranta_dimensionala = 0.005
            elif clasa == "5":
                toleranta_dimensionala = 0.008
            elif clasa == "6":
                toleranta_dimensionala = 0.011
            elif clasa == "7":
                toleranta_dimensionala = 0.018
            elif clasa == "8":
                toleranta_dimensionala = 0.027
            elif clasa == "9":
                toleranta_dimensionala = 0.043
            elif clasa == "10":
                toleranta_dimensionala = 0.07
            elif clasa == "11":
                toleranta_dimensionala = 0.11
            elif clasa == "12":
                toleranta_dimensionala = 0.18
            elif clasa == "13":
                toleranta_dimensionala = 0.27
            elif clasa == "14":
                toleranta_dimensionala = 0.43
            elif clasa == "15":
                toleranta_dimensionala = 0.7
            elif clasa == "16":
                toleranta_dimensionala = 1.1
            elif clasa == "17":
                toleranta_dimensionala = 1.8
            elif clasa == "18":
                toleranta_dimensionala = 2.7
            if tip == "Alezaj" and dimensiune <=14:
                if zona == "A":
                    abaterea_inferioara = 0.29
                elif zona == "B":
                    abaterea_inferioara = 0.15
                elif zona == "C":
                    abaterea_inferioara = 0.095
                elif zona == "D":
                    abaterea_inferioara = 0.05
                elif zona == "E":
                    abaterea_inferioara = 0.032
                elif zona == "F":
                    abaterea_inferioara = 0.016
                elif zona == "G":
                    abaterea_inferioara = 0.006
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.006
                    elif clasa == "7":
                        abaterea_superioara = 0.01
                    elif clasa == "8":
                        abaterea_superioara = 0.015
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.001
                    elif clasa == "3":
                        abaterea_superioara = -0.001 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.001 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.001 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.001 + 0.009
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.007
                    elif clasa == "3":
                        abaterea_superioara = -0.007 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.007 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.007 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.007 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.007 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.007 + 0.009
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.012
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.012 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.012 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.012 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.012 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.012 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.012 + 0.009
                elif zona == "P":
                    abaterea_superioara = -0.018
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "R":
                    abaterea_superioara = -0.023
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "S":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "U":
                    abaterea_superioara = -0.033
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "X":
                    abaterea_superioara = -0.04
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "Z":
                    abaterea_superioara = -0.05
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZA":
                    abaterea_superioara = -0.064
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZB":
                    abaterea_superioara = -0.09
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZC":
                    abaterea_superioara = -0.13
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
            elif tip == "Alezaj" and dimensiune >14:
                if zona == "A":
                    abaterea_inferioara = 0.29
                elif zona == "B":
                    abaterea_inferioara = 0.15
                elif zona == "C":
                    abaterea_inferioara = 0.095
                elif zona == "D":
                    abaterea_inferioara = 0.05
                elif zona == "E":
                    abaterea_inferioara = 0.032
                elif zona == "F":
                    abaterea_inferioara = 0.016
                elif zona == "G":
                    abaterea_inferioara = 0.006
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.006
                    elif clasa == "7":
                        abaterea_superioara = 0.01
                    elif clasa == "8":
                        abaterea_superioara = 0.015
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.001
                    elif clasa == "3":
                        abaterea_superioara = -0.001 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.001 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.001 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.001 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.001 + 0.009
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.007
                    elif clasa == "3":
                        abaterea_superioara = -0.007 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.007 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.007 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.007 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.007 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.007 + 0.009
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.012
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.012 + 0.001
                    elif clasa == "4":
                        abaterea_superioara = -0.012 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.012 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.012 + 0.003
                    elif clasa == "7":
                        abaterea_superioara = -0.012 + 0.007
                    elif clasa == "8":
                        abaterea_superioara = -0.012 + 0.009
                elif zona == "P":
                    abaterea_superioara = -0.018
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "R":
                    abaterea_superioara = -0.023
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "S":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "U":
                    abaterea_superioara = -0.033
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "V":
                    abaterea_superioara = -0.039
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "X":
                    abaterea_superioara = -0.045
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "Z":
                    abaterea_superioara = -0.06
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZA":
                    abaterea_superioara = -0.077
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZB":
                    abaterea_superioara = -0.108
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
                elif zona == "ZC":
                    abaterea_superioara = -0.15
                    if clasa == "3":
                        abaterea_superioara += 0.001
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.003
                    if clasa == "7":
                        abaterea_superioara += 0.007
                    if clasa == "8":
                        abaterea_superioara += 0.009
            elif tip == "Arbore" and dimensiune <=14:
                if zona == "a":
                    abaterea_superioara = -0.29
                elif zona == "b":
                    abaterea_superioara = -0.15
                elif zona == "c":
                    abaterea_superioara = -0.095
                elif zona == "d":
                    abaterea_superioara = -0.05
                elif zona == "e":
                    abaterea_superioara = -0.032
                elif zona == "f":
                    abaterea_superioara = -0.016
                elif zona == "g":
                    abaterea_superioara = -0.006
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.003
                    elif clasa == "7":
                        abaterea_inferioara = -0.006
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.001
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.007
                elif zona == "n":
                    abaterea_inferioara = 0.012
                elif zona == "p":
                    abaterea_inferioara = 0.018
                elif zona == "r":
                    abaterea_inferioara = 0.023
                elif zona == "s":
                    abaterea_inferioara = 0.028
                elif zona == "u":
                    abaterea_inferioara = 0.033
                elif zona == "x":
                    abaterea_inferioara = 0.04
                elif zona == "z":
                    abaterea_inferioara = 0.05
                elif zona == "za":
                    abaterea_inferioara = 0.064
                elif zona == "zb":
                    abaterea_inferioara = 0.09
                elif zona == "zc":
                    abaterea_inferioara = 0.13
            elif tip == "Arbore" and dimensiune >14:
                if zona == "a":
                    abaterea_superioara = -0.29
                elif zona == "b":
                    abaterea_superioara = -0.15
                elif zona == "c":
                    abaterea_superioara = -0.095
                elif zona == "d":
                    abaterea_superioara = -0.05
                elif zona == "e":
                    abaterea_superioara = -0.032
                elif zona == "f":
                    abaterea_superioara = -0.016
                elif zona == "g":
                    abaterea_superioara = -0.006
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.003
                    elif clasa == "7":
                        abaterea_inferioara = -0.006
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.001
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.007
                elif zona == "n":
                    abaterea_inferioara = 0.012
                elif zona == "p":
                    abaterea_inferioara = 0.018
                elif zona == "r":
                    abaterea_inferioara = 0.023
                elif zona == "s":
                    abaterea_inferioara = 0.028
                elif zona == "u":
                    abaterea_inferioara = 0.033
                elif zona == "v":
                    abaterea_inferioara = 0.039
                elif zona == "x":
                    abaterea_inferioara = 0.045
                elif zona == "z":
                    abaterea_inferioara = 0.06
                elif zona == "za":
                    abaterea_inferioara = 0.077
                elif zona == "zb":
                    abaterea_inferioara = 0.108
                elif zona == "zc":
                    abaterea_inferioara = 0.15
        elif dimensiune >18 and dimensiune <=30:
            if clasa == "01":
                toleranta_dimensionala = 0.0006
            elif clasa == "0":
                toleranta_dimensionala = 0.001
            elif clasa == "1":
                toleranta_dimensionala = 0.0015
            elif clasa == "2":
                toleranta_dimensionala = 0.0025
            elif clasa == "3":
                toleranta_dimensionala = 0.004
            elif clasa == "4":
                toleranta_dimensionala = 0.006
            elif clasa == "5":
                toleranta_dimensionala = 0.009
            elif clasa == "6":
                toleranta_dimensionala = 0.013
            elif clasa == "7":
                toleranta_dimensionala = 0.021
            elif clasa == "8":
                toleranta_dimensionala = 0.033
            elif clasa == "9":
                toleranta_dimensionala = 0.052
            elif clasa == "10":
                toleranta_dimensionala = 0.084
            elif clasa == "11":
                toleranta_dimensionala = 0.13
            elif clasa == "12":
                toleranta_dimensionala = 0.21
            elif clasa == "13":
                toleranta_dimensionala = 0.33
            elif clasa == "14":
                toleranta_dimensionala = 0.52
            elif clasa == "15":
                toleranta_dimensionala = 0.84
            elif clasa == "16":
                toleranta_dimensionala = 1.3
            elif clasa == "17":
                toleranta_dimensionala = 2.1
            elif clasa == "18":
                toleranta_dimensionala = 3.3
            if tip == "Alezaj" and dimensiune <=24:
                if zona == "A":
                    abaterea_inferioara = 0.3
                elif zona == "B":
                    abaterea_inferioara = 0.16
                elif zona == "C":
                    abaterea_inferioara = 0.11
                elif zona == "D":
                    abaterea_inferioara = 0.065
                elif zona == "E":
                    abaterea_inferioara = 0.04
                elif zona == "F":
                    abaterea_inferioara = 0.02
                elif zona == "G":
                    abaterea_inferioara = 0.007
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.008
                    elif clasa == "7":
                        abaterea_superioara = 0.012
                    elif clasa == "8":
                        abaterea_superioara = 0.02
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.012
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.008
                    elif clasa == "3":
                        abaterea_superioara = -0.008 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.008 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.008 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.008 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.008 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.008 + 0.012
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.015
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.015 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.015 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.015 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.015 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.015 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.015 + 0.012
                elif zona == "P":
                    abaterea_superioara = -0.022
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "R":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "S":
                    abaterea_superioara = -0.035
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "U":
                    abaterea_superioara = -0.041
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "V":
                    abaterea_superioara = -0.047
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "X":
                    abaterea_superioara = -0.054
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "Y":
                    abaterea_superioara = -0.063
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "Z":
                    abaterea_superioara = -0.073
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZA":
                    abaterea_superioara = -0.098
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZB":
                    abaterea_superioara = -0.136
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZC":
                    abaterea_superioara = -0.188
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
            elif tip == "Alezaj" and dimensiune >24:
                if zona == "A":
                    abaterea_inferioara = 0.3
                elif zona == "B":
                    abaterea_inferioara = 0.16
                elif zona == "C":
                    abaterea_inferioara = 0.11
                elif zona == "D":
                    abaterea_inferioara = 0.065
                elif zona == "E":
                    abaterea_inferioara = 0.04
                elif zona == "F":
                    abaterea_inferioara = 0.02
                elif zona == "G":
                    abaterea_inferioara = 0.007
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.008
                    elif clasa == "7":
                        abaterea_superioara = 0.012
                    elif clasa == "8":
                        abaterea_superioara = 0.02
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.012
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.008
                    elif clasa == "3":
                        abaterea_superioara = -0.008 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.008 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.008 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.008 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.008 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.008 + 0.012
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.015
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.015 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.015 + 0.002
                    elif clasa == "5":
                        abaterea_superioara = -0.015 + 0.003
                    elif clasa == "6":
                        abaterea_superioara = -0.015 + 0.004
                    elif clasa == "7":
                        abaterea_superioara = -0.015 + 0.008
                    elif clasa == "8":
                        abaterea_superioara = -0.015 + 0.012
                elif zona == "P":
                    abaterea_superioara = -0.022
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "R":
                    abaterea_superioara = -0.028
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "S":
                    abaterea_superioara = -0.035
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "T":
                    abaterea_superioara = -0.041
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "U":
                    abaterea_superioara = -0.048
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "V":
                    abaterea_superioara = -0.055
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "X":
                    abaterea_superioara = -0.064
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "Y":
                    abaterea_superioara = -0.075
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "Z":
                    abaterea_superioara = -0.088
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZA":
                    abaterea_superioara = -0.118
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZB":
                    abaterea_superioara = -0.16
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
                elif zona == "ZC":
                    abaterea_superioara = -0.218
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.002
                    if clasa == "5":
                        abaterea_superioara += 0.003
                    if clasa == "6":
                        abaterea_superioara += 0.004
                    if clasa == "7":
                        abaterea_superioara += 0.008
                    if clasa == "8":
                        abaterea_superioara += 0.012
            elif tip == "Arbore" and dimensiune <=24:
                if zona == "a":
                    abaterea_superioara = -0.3
                elif zona == "b":
                    abaterea_superioara = -0.16
                elif zona == "c":
                    abaterea_superioara = -0.11
                elif zona == "d":
                    abaterea_superioara = -0.065
                elif zona == "e":
                    abaterea_superioara = -0.04
                elif zona == "f":
                    abaterea_superioara = -0.02
                elif zona == "g":
                    abaterea_superioara = -0.007
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.004
                    elif clasa == "7":
                        abaterea_inferioara = -0.008
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.008
                elif zona == "n":
                    abaterea_inferioara = 0.015
                elif zona == "p":
                    abaterea_inferioara = 0.022
                elif zona == "r":
                    abaterea_inferioara = 0.028
                elif zona == "s":
                    abaterea_inferioara = 0.035
                elif zona == "u":
                    abaterea_inferioara = 0.041
                elif zona == "v":
                    abaterea_inferioara = 0.047
                elif zona == "x":
                    abaterea_inferioara = 0.054
                elif zona == "y":
                    abaterea_inferioara = 0.063
                elif zona == "z":
                    abaterea_inferioara = 0.073
                elif zona == "za":
                    abaterea_inferioara = 0.098
                elif zona == "zb":
                    abaterea_inferioara = 0.136
                elif zona == "zc":
                    abaterea_inferioara = 0.188
            elif tip == "Arbore" and dimensiune >24:
                if zona == "a":
                    abaterea_superioara = -0.3
                elif zona == "b":
                    abaterea_superioara = -0.16
                elif zona == "c":
                    abaterea_superioara = -0.11
                elif zona == "d":
                    abaterea_superioara = -0.065
                elif zona == "e":
                    abaterea_superioara = -0.04
                elif zona == "f":
                    abaterea_superioara = -0.02
                elif zona == "g":
                    abaterea_superioara = -0.007
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.004
                    elif clasa == "7":
                        abaterea_inferioara = -0.008
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.008
                elif zona == "n":
                    abaterea_inferioara = 0.015
                elif zona == "p":
                    abaterea_inferioara = 0.022
                elif zona == "r":
                    abaterea_inferioara = 0.028
                elif zona == "s":
                    abaterea_inferioara = 0.035
                elif zona == "t":
                    abaterea_inferioara = 0.041
                elif zona == "u":
                    abaterea_inferioara = 0.048
                elif zona == "v":
                    abaterea_inferioara = 0.055
                elif zona == "x":
                    abaterea_inferioara = 0.064
                elif zona == "y":
                    abaterea_inferioara = 0.075
                elif zona == "z":
                    abaterea_inferioara = 0.088
                elif zona == "za":
                    abaterea_inferioara = 0.118
                elif zona == "zb":
                    abaterea_inferioara = 0.16
                elif zona == "zc":
                    abaterea_inferioara = 0.218
        elif dimensiune >30 and dimensiune <=50:
            if clasa == "01":
                toleranta_dimensionala = 0.0006
            elif clasa == "0":
                toleranta_dimensionala = 0.001
            elif clasa == "1":
                toleranta_dimensionala = 0.0015
            elif clasa == "2":
                toleranta_dimensionala = 0.0035
            elif clasa == "3":
                toleranta_dimensionala = 0.004
            elif clasa == "4":
                toleranta_dimensionala = 0.007
            elif clasa == "5":
                toleranta_dimensionala = 0.011
            elif clasa == "6":
                toleranta_dimensionala = 0.016
            elif clasa == "7":
                toleranta_dimensionala = 0.025
            elif clasa == "8":
                toleranta_dimensionala = 0.039
            elif clasa == "9":
                toleranta_dimensionala = 0.062
            elif clasa == "10":
                toleranta_dimensionala = 0.1
            elif clasa == "11":
                toleranta_dimensionala = 0.16
            elif clasa == "12":
                toleranta_dimensionala = 0.25
            elif clasa == "13":
                toleranta_dimensionala = 0.39
            elif clasa == "14":
                toleranta_dimensionala = 0.62
            elif clasa == "15":
                toleranta_dimensionala = 1
            elif clasa == "16":
                toleranta_dimensionala = 1.6
            elif clasa == "17":
                toleranta_dimensionala = 2.5
            elif clasa == "18":
                toleranta_dimensionala = 3.9
            if tip == "Alezaj" and dimensiune <=40:
                if zona == "A":
                    abaterea_inferioara = 0.31
                elif zona == "B":
                    abaterea_inferioara = 0.17
                elif zona == "C":
                    abaterea_inferioara = 0.12
                elif zona == "D":
                    abaterea_inferioara = 0.08
                elif zona == "E":
                    abaterea_inferioara = 0.05
                elif zona == "F":
                    abaterea_inferioara = 0.025
                elif zona == "G":
                    abaterea_inferioara = 0.009
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.01
                    elif clasa == "7":
                        abaterea_superioara = 0.014
                    elif clasa == "8":
                        abaterea_superioara = 0.024
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.014
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.009
                    elif clasa == "3":
                        abaterea_superioara = -0.009 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.009 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.009 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.009 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.009 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.009 + 0.014
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.017
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.017 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.017 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.017 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.017 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.017 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.017 + 0.014
                elif zona == "P":
                    abaterea_superioara = -0.026
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "R":
                    abaterea_superioara = -0.034
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "S":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "T":
                    abaterea_superioara = -0.048
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "U":
                    abaterea_superioara = -0.06
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "V":
                    abaterea_superioara = -0.068
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "X":
                    abaterea_superioara = -0.08
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "Y":
                    abaterea_superioara = -0.094
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "Z":
                    abaterea_superioara = -0.112
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZA":
                    abaterea_superioara = -0.148
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZB":
                    abaterea_superioara = -0.2
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZC":
                    abaterea_superioara = -0.274
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
            elif tip == "Alezaj" and dimensiune >40:
                if zona == "A":
                    abaterea_inferioara = 0.32
                elif zona == "B":
                    abaterea_inferioara = 0.18
                elif zona == "C":
                    abaterea_inferioara = 0.13
                elif zona == "D":
                    abaterea_inferioara = 0.08
                elif zona == "E":
                    abaterea_inferioara = 0.05
                elif zona == "F":
                    abaterea_inferioara = 0.025
                elif zona == "G":
                    abaterea_inferioara = 0.009
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.01
                    elif clasa == "7":
                        abaterea_superioara = 0.014
                    elif clasa == "8":
                        abaterea_superioara = 0.024
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.014
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.009
                    elif clasa == "3":
                        abaterea_superioara = -0.009 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.009 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.009 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.009 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.009 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.009 + 0.014
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.017
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.017 + 0.0015
                    elif clasa == "4":
                        abaterea_superioara = -0.017 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.017 + 0.004
                    elif clasa == "6":
                        abaterea_superioara = -0.017 + 0.005
                    elif clasa == "7":
                        abaterea_superioara = -0.017 + 0.009
                    elif clasa == "8":
                        abaterea_superioara = -0.017 + 0.014
                elif zona == "P":
                    abaterea_superioara = -0.026
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "R":
                    abaterea_superioara = -0.034
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "S":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "T":
                    abaterea_superioara = -0.054
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "U":
                    abaterea_superioara = -0.07
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "V":
                    abaterea_superioara = -0.081
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "X":
                    abaterea_superioara = -0.097
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "Y":
                    abaterea_superioara = -0.114
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "Z":
                    abaterea_superioara = -0.136
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZA":
                    abaterea_superioara = -0.18
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZB":
                    abaterea_superioara = -0.242
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
                elif zona == "ZC":
                    abaterea_superioara = -0.325
                    if clasa == "3":
                        abaterea_superioara += 0.0015
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.004
                    if clasa == "6":
                        abaterea_superioara += 0.005
                    if clasa == "7":
                        abaterea_superioara += 0.009
                    if clasa == "8":
                        abaterea_superioara += 0.014
            elif tip == "Arbore" and dimensiune <=40:
                if zona == "a":
                    abaterea_superioara = -0.31
                elif zona == "b":
                    abaterea_superioara = -0.17
                elif zona == "c":
                    abaterea_superioara = -0.12
                elif zona == "d":
                    abaterea_superioara = -0.08
                elif zona == "e":
                    abaterea_superioara = -0.05
                elif zona == "f":
                    abaterea_superioara = -0.025
                elif zona == "g":
                    abaterea_superioara = -0.009
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.005
                    elif clasa == "7":
                        abaterea_inferioara = -0.01
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.009
                elif zona == "n":
                    abaterea_inferioara = 0.017
                elif zona == "p":
                    abaterea_inferioara = 0.026
                elif zona == "r":
                    abaterea_inferioara = 0.034
                elif zona == "s":
                    abaterea_inferioara = 0.043
                elif zona == "t":
                    abaterea_inferioara = 0.048
                elif zona == "u":
                    abaterea_inferioara = 0.06
                elif zona == "v":
                    abaterea_inferioara = 0.068
                elif zona == "x":
                    abaterea_inferioara = 0.08
                elif zona == "y":
                    abaterea_inferioara = 0.094
                elif zona == "z":
                    abaterea_inferioara = 0.112
                elif zona == "za":
                    abaterea_inferioara = 0.148
                elif zona == "zb":
                    abaterea_inferioara = 0.2
                elif zona == "zc":
                    abaterea_inferioara = 0.274
            elif tip == "Arbore" and dimensiune >40:
                if zona == "a":
                    abaterea_superioara = -0.32
                elif zona == "b":
                    abaterea_superioara = -0.18
                elif zona == "c":
                    abaterea_superioara = -0.13
                elif zona == "d":
                    abaterea_superioara = -0.08
                elif zona == "e":
                    abaterea_superioara = -0.05
                elif zona == "f":
                    abaterea_superioara = -0.025
                elif zona == "g":
                    abaterea_superioara = -0.009
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.005
                    elif clasa == "7":
                        abaterea_inferioara = -0.01
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.009
                elif zona == "n":
                    abaterea_inferioara = 0.017
                elif zona == "p":
                    abaterea_inferioara = 0.026
                elif zona == "r":
                    abaterea_inferioara = 0.034
                elif zona == "s":
                    abaterea_inferioara = 0.043
                elif zona == "t":
                    abaterea_inferioara = 0.054
                elif zona == "u":
                    abaterea_inferioara = 0.07
                elif zona == "v":
                    abaterea_inferioara = 0.081
                elif zona == "x":
                    abaterea_inferioara = 0.097
                elif zona == "y":
                    abaterea_inferioara = 0.114
                elif zona == "z":
                    abaterea_inferioara = 0.136
                elif zona == "za":
                    abaterea_inferioara = 0.18
                elif zona == "zb":
                    abaterea_inferioara = 0.242
                elif zona == "zc":
                    abaterea_inferioara = 0.325
        elif dimensiune >50 and dimensiune <=80:    
            if clasa == "01":
                toleranta_dimensionala = 0.0008
            elif clasa == "0":
                toleranta_dimensionala = 0.0012
            elif clasa == "1":
                toleranta_dimensionala = 0.002
            elif clasa == "2":
                toleranta_dimensionala = 0.003
            elif clasa == "3":
                toleranta_dimensionala = 0.005
            elif clasa == "4":
                toleranta_dimensionala = 0.008
            elif clasa == "5":
                toleranta_dimensionala = 0.013
            elif clasa == "6":
                toleranta_dimensionala = 0.019
            elif clasa == "7":
                toleranta_dimensionala = 0.03
            elif clasa == "8":
                toleranta_dimensionala = 0.046
            elif clasa == "9":
                toleranta_dimensionala = 0.074
            elif clasa == "10":
                toleranta_dimensionala = 0.12
            elif clasa == "11":
                toleranta_dimensionala = 0.19
            elif clasa == "12":
                toleranta_dimensionala = 0.3
            elif clasa == "13":
                toleranta_dimensionala = 0.46
            elif clasa == "14":
                toleranta_dimensionala = 0.74
            elif clasa == "15":
                toleranta_dimensionala = 1.2
            elif clasa == "16":
                toleranta_dimensionala = 1.9
            elif clasa == "17":
                toleranta_dimensionala = 3
            elif clasa == "18":
                toleranta_dimensionala = 4.6
            if tip == "Alezaj" and dimensiune <=65:
                if zona == "A":
                    abaterea_inferioara = 0.34
                elif zona == "B":
                    abaterea_inferioara = 0.19
                elif zona == "C":
                    abaterea_inferioara = 0.14
                elif zona == "D":
                    abaterea_inferioara = 0.1
                elif zona == "E":
                    abaterea_inferioara = 0.06
                elif zona == "F":
                    abaterea_inferioara = 0.03
                elif zona == "G":
                    abaterea_inferioara = 0.01
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.013
                    elif clasa == "7":
                        abaterea_superioara = 0.018
                    elif clasa == "8":
                        abaterea_superioara = 0.028
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.016
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.011
                    elif clasa == "3":
                        abaterea_superioara = -0.011 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.011 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.011 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.011 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.011 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.011 + 0.016
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.02
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.02 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.02 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.02 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.02 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.02 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.02 + 0.016
                elif zona == "P":
                    abaterea_superioara = -0.032
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "R":
                    abaterea_superioara = -0.041
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "S":
                    abaterea_superioara = -0.053
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "T":
                    abaterea_superioara = -0.066
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "U":
                    abaterea_superioara = -0.087
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "V":
                    abaterea_superioara = -0.102
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "X":
                    abaterea_superioara = -0.122
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "Y":
                    abaterea_superioara = -0.144
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "Z":
                    abaterea_superioara = -0.172
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZA":
                    abaterea_superioara = -0.226
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZB":
                    abaterea_superioara = -0.3
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZC":
                    abaterea_superioara = -0.405
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
            elif tip == "Alezaj" and dimensiune >65:
                if zona == "A":
                    abaterea_inferioara = 0.36
                elif zona == "B":
                    abaterea_inferioara = 0.2
                elif zona == "C":
                    abaterea_inferioara = 0.15
                elif zona == "D":
                    abaterea_inferioara = 0.1
                elif zona == "E":
                    abaterea_inferioara = 0.06
                elif zona == "F":
                    abaterea_inferioara = 0.03
                elif zona == "G":
                    abaterea_inferioara = 0.01
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.013
                    elif clasa == "7":
                        abaterea_superioara = 0.018
                    elif clasa == "8":
                        abaterea_superioara = 0.028
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.002
                    elif clasa == "3":
                        abaterea_superioara = -0.002 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.002 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.002 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.002 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.002 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.002 + 0.016
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.011
                    elif clasa == "3":
                        abaterea_superioara = -0.011 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.011 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.011 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.011 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.011 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.011 + 0.016
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.02
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.02 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.02 + 0.003
                    elif clasa == "5":
                        abaterea_superioara = -0.02 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.02 + 0.006
                    elif clasa == "7":
                        abaterea_superioara = -0.02 + 0.011
                    elif clasa == "8":
                        abaterea_superioara = -0.02 + 0.016
                elif zona == "P":
                    abaterea_superioara = -0.032
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "R":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "S":
                    abaterea_superioara = -0.059
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "T":
                    abaterea_superioara = -0.075
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "U":
                    abaterea_superioara = -0.102
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "V":
                    abaterea_superioara = -0.120
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "X":
                    abaterea_superioara = -0.146
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "Y":
                    abaterea_superioara = -0.174
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "Z":
                    abaterea_superioara = -0.21
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZA":
                    abaterea_superioara = -0.274
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZB":
                    abaterea_superioara = -0.36
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
                elif zona == "ZC":
                    abaterea_superioara = -0.48
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.003
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.006
                    if clasa == "7":
                        abaterea_superioara += 0.011
                    if clasa == "8":
                        abaterea_superioara += 0.016
            elif tip == "Arbore" and dimensiune <=65:
                if zona == "a":
                    abaterea_superioara = -0.34
                elif zona == "b":
                    abaterea_superioara = -0.19
                elif zona == "c":
                    abaterea_superioara = -0.14
                elif zona == "d":
                    abaterea_superioara = -0.1
                elif zona == "e":
                    abaterea_superioara = -0.06
                elif zona == "f":
                    abaterea_superioara = -0.03
                elif zona == "g":
                    abaterea_superioara = -0.01
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.007
                    elif clasa == "7":
                        abaterea_inferioara = -0.012
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.011
                elif zona == "n":
                    abaterea_inferioara = 0.02
                elif zona == "p":
                    abaterea_inferioara = 0.032
                elif zona == "r":
                    abaterea_inferioara = 0.041
                elif zona == "s":
                    abaterea_inferioara = 0.053
                elif zona == "t":
                    abaterea_inferioara = 0.066
                elif zona == "u":
                    abaterea_inferioara = 0.087
                elif zona == "v":
                    abaterea_inferioara = 0.102
                elif zona == "x":
                    abaterea_inferioara = 0.122
                elif zona == "y":
                    abaterea_inferioara = 0.144
                elif zona == "z":
                    abaterea_inferioara = 0.172
                elif zona == "za":
                    abaterea_inferioara = 0.226
                elif zona == "zb":
                    abaterea_inferioara = 0.3
                elif zona == "zc":
                    abaterea_inferioara = 0.405
            elif tip == "Arbore" and dimensiune >65:
                if zona == "a":
                    abaterea_superioara = -0.36
                elif zona == "b":
                    abaterea_superioara = -0.2
                elif zona == "c":
                    abaterea_superioara = -0.15
                elif zona == "d":
                    abaterea_superioara = -0.1
                elif zona == "e":
                    abaterea_superioara = -0.06
                elif zona == "f":
                    abaterea_superioara = -0.03
                elif zona == "g":
                    abaterea_superioara = -0.01
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.007
                    elif clasa == "7":
                        abaterea_inferioara = -0.012
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.002
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.011
                elif zona == "n":
                    abaterea_inferioara = 0.02
                elif zona == "p":
                    abaterea_inferioara = 0.032
                elif zona == "r":
                    abaterea_inferioara = 0.043
                elif zona == "s":
                    abaterea_inferioara = 0.059
                elif zona == "t":
                    abaterea_inferioara = 0.075
                elif zona == "u":
                    abaterea_inferioara = 0.102
                elif zona == "v":
                    abaterea_inferioara = 0.12
                elif zona == "x":
                    abaterea_inferioara = 0.146
                elif zona == "y":
                    abaterea_inferioara = 0.174
                elif zona == "z":
                    abaterea_inferioara = 0.21
                elif zona == "za":
                    abaterea_inferioara = 0.274
                elif zona == "zb":
                    abaterea_inferioara = 0.36
                elif zona == "zc":
                    abaterea_inferioara = 0.48
        elif dimensiune >80 and dimensiune <=120:
            if clasa == "01":
                toleranta_dimensionala = 0.001
            elif clasa == "0":
                toleranta_dimensionala = 0.0015
            elif clasa == "1":
                toleranta_dimensionala = 0.0025
            elif clasa == "2":
                toleranta_dimensionala = 0.004
            elif clasa == "3":
                toleranta_dimensionala = 0.006
            elif clasa == "4":
                toleranta_dimensionala = 0.01
            elif clasa == "5":
                toleranta_dimensionala = 0.015
            elif clasa == "6":
                toleranta_dimensionala = 0.022
            elif clasa == "7":
                toleranta_dimensionala = 0.035
            elif clasa == "8":
                toleranta_dimensionala = 0.054
            elif clasa == "9":
                toleranta_dimensionala = 0.087
            elif clasa == "10":
                toleranta_dimensionala = 0.14
            elif clasa == "11":
                toleranta_dimensionala = 0.22
            elif clasa == "12":
                toleranta_dimensionala = 0.35
            elif clasa == "13":
                toleranta_dimensionala = 0.54
            elif clasa == "14":
                toleranta_dimensionala = 0.87
            elif clasa == "15":
                toleranta_dimensionala = 1.4
            elif clasa == "16":
                toleranta_dimensionala = 2.2
            elif clasa == "17":
                toleranta_dimensionala = 3.5
            elif clasa == "18":
                toleranta_dimensionala = 5.4
            if tip == "Alezaj" and dimensiune <=100:
                if zona == "A":
                    abaterea_inferioara = 0.38
                elif zona == "B":
                    abaterea_inferioara = 0.22
                elif zona == "C":
                    abaterea_inferioara = 0.17
                elif zona == "D":
                    abaterea_inferioara = 0.12
                elif zona == "E":
                    abaterea_inferioara = 0.072
                elif zona == "F":
                    abaterea_inferioara = 0.036
                elif zona == "G":
                    abaterea_inferioara = 0.012
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.018
                    elif clasa == "7":
                        abaterea_superioara = 0.022
                    elif clasa == "8":
                        abaterea_superioara = 0.034
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.003
                    elif clasa == "3":
                        abaterea_superioara = -0.003 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.003 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.003 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.003 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.003 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.003 + 0.019
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.013
                    elif clasa == "3":
                        abaterea_superioara = -0.013 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.013 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.013 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.013 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.013 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.013 + 0.019
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.023
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.023 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.023 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.023 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.023 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.023 + 0.019
                elif zona == "P":
                    abaterea_superioara = -0.037
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "R":
                    abaterea_superioara = -0.051
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "S":
                    abaterea_superioara = -0.071
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "T":
                    abaterea_superioara = -0.091
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "U":
                    abaterea_superioara = -0.124
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "V":
                    abaterea_superioara = -0.146
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "X":
                    abaterea_superioara = -0.178
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "Y":
                    abaterea_superioara = -0.214
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "Z":
                    abaterea_superioara = -0.258
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZA":
                    abaterea_superioara = -0.335
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZB":
                    abaterea_superioara = -0.445
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZC":
                    abaterea_superioara = -0.585
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
            elif tip == "Alezaj" and dimensiune >100:
                if zona == "A":
                    abaterea_inferioara = 0.41
                elif zona == "B":
                    abaterea_inferioara = 0.24
                elif zona == "C":
                    abaterea_inferioara = 0.18
                elif zona == "D":
                    abaterea_inferioara = 0.12
                elif zona == "E":
                    abaterea_inferioara = 0.072
                elif zona == "F":
                    abaterea_inferioara = 0.036
                elif zona == "G":
                    abaterea_inferioara = 0.012
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.018
                    elif clasa == "7":
                        abaterea_superioara = 0.022
                    elif clasa == "8":
                        abaterea_superioara = 0.034
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.003
                    elif clasa == "3":
                        abaterea_superioara = -0.003 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.003 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.003 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.003 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.003 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.003 + 0.019
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.013
                    elif clasa == "3":
                        abaterea_superioara = -0.013 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.013 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.013 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.013 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.013 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.013 + 0.019
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.023
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.023 + 0.002
                    elif clasa == "4":
                        abaterea_superioara = -0.023 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "6":
                        abaterea_superioara = -0.023 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.023 + 0.013
                    elif clasa == "8":
                        abaterea_superioara = -0.023 + 0.019
                elif zona == "P":
                    abaterea_superioara = -0.037
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "R":
                    abaterea_superioara = -0.054
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "S":
                    abaterea_superioara = -0.079
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "T":
                    abaterea_superioara = -0.104
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "U":
                    abaterea_superioara = -0.144
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "V":
                    abaterea_superioara = -0.172
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "X":
                    abaterea_superioara = -0.21
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "Y":
                    abaterea_superioara = -0.254
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "Z":
                    abaterea_superioara = -0.31
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZA":
                    abaterea_superioara = -0.4
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZB":
                    abaterea_superioara = -0.525
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
                elif zona == "ZC":
                    abaterea_superioara = -0.69
                    if clasa == "3":
                        abaterea_superioara += 0.002
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.005
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.013
                    if clasa == "8":
                        abaterea_superioara += 0.019
            elif tip == "Arbore" and dimensiune <=100:
                if zona == "a":
                    abaterea_superioara = -0.38
                elif zona == "b":
                    abaterea_superioara = -0.22
                elif zona == "c":
                    abaterea_superioara = -0.17
                elif zona == "d":
                    abaterea_superioara = -0.12
                elif zona == "e":
                    abaterea_superioara = -0.072
                elif zona == "f":
                    abaterea_superioara = -0.036
                elif zona == "g":
                    abaterea_superioara = -0.012
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.009
                    elif clasa == "7":
                        abaterea_inferioara = -0.015
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.003
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.013
                elif zona == "n":
                    abaterea_inferioara = 0.023
                elif zona == "p":
                    abaterea_inferioara = 0.037
                elif zona == "r":
                    abaterea_inferioara = 0.051
                elif zona == "s":
                    abaterea_inferioara = 0.071
                elif zona == "t":
                    abaterea_inferioara = 0.091
                elif zona == "u":
                    abaterea_inferioara = 0.124
                elif zona == "v":
                    abaterea_inferioara = 0.146
                elif zona == "x":
                    abaterea_inferioara = 0.178
                elif zona == "y":
                    abaterea_inferioara = 0.214
                elif zona == "z":
                    abaterea_inferioara = 0.258
                elif zona == "za":
                    abaterea_inferioara = 0.335
                elif zona == "zb":
                    abaterea_inferioara = 0.445
                elif zona == "zc":
                    abaterea_inferioara = 0.585
            elif tip == "Arbore" and dimensiune >100:
                if zona == "a":
                    abaterea_superioara = -0.41
                elif zona == "b":
                    abaterea_superioara = -0.24
                elif zona == "c":
                    abaterea_superioara = -0.18
                elif zona == "d":
                    abaterea_superioara = -0.12
                elif zona == "e":
                    abaterea_superioara = -0.072
                elif zona == "f":
                    abaterea_superioara = -0.036
                elif zona == "g":
                    abaterea_superioara = -0.012
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.009
                    elif clasa == "7":
                        abaterea_inferioara = -0.015
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.003
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.013
                elif zona == "n":
                    abaterea_inferioara = 0.023
                elif zona == "p":
                    abaterea_inferioara = 0.037
                elif zona == "r":
                    abaterea_inferioara = 0.054
                elif zona == "s":
                    abaterea_inferioara = 0.079
                elif zona == "t":
                    abaterea_inferioara = 0.104
                elif zona == "u":
                    abaterea_inferioara = 0.144
                elif zona == "v":
                    abaterea_inferioara = 0.172
                elif zona == "x":
                    abaterea_inferioara = 0.21
                elif zona == "y":
                    abaterea_inferioara = 0.254
                elif zona == "z":
                    abaterea_inferioara = 0.31
                elif zona == "za":
                    abaterea_inferioara = 0.4
                elif zona == "zb":
                    abaterea_inferioara = 0.525
                elif zona == "zc":
                    abaterea_inferioara = 0.69
        elif dimensiune >120 and dimensiune <=180:
            if clasa == "01":
                toleranta_dimensionala = 0.0012
            elif clasa == "0":
                toleranta_dimensionala = 0.002
            elif clasa == "1":
                toleranta_dimensionala = 0.0035
            elif clasa == "2":
                toleranta_dimensionala = 0.005
            elif clasa == "3":
                toleranta_dimensionala = 0.008
            elif clasa == "4":
                toleranta_dimensionala = 0.012
            elif clasa == "5":
                toleranta_dimensionala = 0.018
            elif clasa == "6":
                toleranta_dimensionala = 0.025
            elif clasa == "7":
                toleranta_dimensionala = 0.04
            elif clasa == "8":
                toleranta_dimensionala = 0.063
            elif clasa == "9":
                toleranta_dimensionala = 0.1
            elif clasa == "10":
                toleranta_dimensionala = 0.16
            elif clasa == "11":
                toleranta_dimensionala = 0.25
            elif clasa == "12":
                toleranta_dimensionala = 0.4
            elif clasa == "13":
                toleranta_dimensionala = 0.63
            elif clasa == "14":
                toleranta_dimensionala = 1
            elif clasa == "15":
                toleranta_dimensionala = 1.6
            elif clasa == "16":
                toleranta_dimensionala = 2.5
            elif clasa == "17":
                toleranta_dimensionala = 4
            elif clasa == "18":
                toleranta_dimensionala = 6.3
            if tip == "Alezaj" and dimensiune <=140:
                if zona == "A":
                    abaterea_inferioara = 0.46
                elif zona == "B":
                    abaterea_inferioara = 0.26
                elif zona == "C":
                    abaterea_inferioara = 0.2
                elif zona == "D":
                    abaterea_inferioara = 0.145
                elif zona == "E":
                    abaterea_inferioara = 0.085
                elif zona == "F":
                    abaterea_inferioara = 0.043
                elif zona == "G":
                    abaterea_inferioara = 0.014
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.018
                    elif clasa == "7":
                        abaterea_superioara = 0.026
                    elif clasa == "8":
                        abaterea_superioara = 0.041
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.003
                    elif clasa == "3":
                        abaterea_superioara = -0.003 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.003 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.003 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.003 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.003 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.003 + 0.023
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.015
                    elif clasa == "3":
                        abaterea_superioara = -0.015 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.015 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.015 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.015 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.015 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.015 + 0.023
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.027
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.027 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.027 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.027 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.027 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.027 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.027 + 0.023
                elif zona == "P":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "R":
                    abaterea_superioara = -0.063
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "S":
                    abaterea_superioara = -0.092
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "T":
                    abaterea_superioara = -0.122
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "U":
                    abaterea_superioara = -0.17
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "V":
                    abaterea_superioara = -0.202
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "X":
                    abaterea_superioara = -0.248
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Y":
                    abaterea_superioara = -0.3
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Z":
                    abaterea_superioara = -0.365
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZA":
                    abaterea_superioara = -0.47
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZB":
                    abaterea_superioara = -0.62
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZC":
                    abaterea_superioara = -0.8
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
            elif tip == "Alezaj" and dimensiune >140 and dimensiune <=160:
                if zona == "A":
                    abaterea_inferioara = 0.52
                elif zona == "B":
                    abaterea_inferioara = 0.28
                elif zona == "C":
                    abaterea_inferioara = 0.21
                elif zona == "D":
                    abaterea_inferioara = 0.145
                elif zona == "E":
                    abaterea_inferioara = 0.085
                elif zona == "F":
                    abaterea_inferioara = 0.043
                elif zona == "G":
                    abaterea_inferioara = 0.014
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.018
                    elif clasa == "7":
                        abaterea_superioara = 0.026
                    elif clasa == "8":
                        abaterea_superioara = 0.041
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.003
                    elif clasa == "3":
                        abaterea_superioara = -0.003 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.003 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.003 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.003 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.003 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.003 + 0.023
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.015
                    elif clasa == "3":
                        abaterea_superioara = -0.015 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.015 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.015 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.015 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.015 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.015 + 0.023
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.027
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.027 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.027 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.027 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.027 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.027 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.027 + 0.023
                elif zona == "P":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "R":
                    abaterea_superioara = -0.065
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "S":
                    abaterea_superioara = -0.1
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "T":
                    abaterea_superioara = -0.134
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "U":
                    abaterea_superioara = -0.19
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "V":
                    abaterea_superioara = -0.228
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "X":
                    abaterea_superioara = -0.28
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Y":
                    abaterea_superioara = -0.34
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Z":
                    abaterea_superioara = -0.415
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZA":
                    abaterea_superioara = -0.535
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZB":
                    abaterea_superioara = -0.7
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZC":
                    abaterea_superioara = -0.9
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
            elif tip == "Alezaj" and dimensiune >160:
                if zona == "A":
                    abaterea_inferioara = 0.58
                elif zona == "B":
                    abaterea_inferioara = 0.31
                elif zona == "C":
                    abaterea_inferioara = 0.23
                elif zona == "D":
                    abaterea_inferioara = 0.145
                elif zona == "E":
                    abaterea_inferioara = 0.085
                elif zona == "F":
                    abaterea_inferioara = 0.043
                elif zona == "G":
                    abaterea_inferioara = 0.014
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.018
                    elif clasa == "7":
                        abaterea_superioara = 0.026
                    elif clasa == "8":
                        abaterea_superioara = 0.041
                elif zona == "K":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.003
                    elif clasa == "3":
                        abaterea_superioara = -0.003 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.003 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.003 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.003 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.003 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.003 + 0.023
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.015
                    elif clasa == "3":
                        abaterea_superioara = -0.015 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.015 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.015 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.015 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.015 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.015 + 0.023
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.027
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.027 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.027 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.027 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.027 + 0.007
                    elif clasa == "7":
                        abaterea_superioara = -0.027 + 0.015
                    elif clasa == "8":
                        abaterea_superioara = -0.027 + 0.023
                elif zona == "P":
                    abaterea_superioara = -0.043
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "R":
                    abaterea_superioara = -0.068
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "S":
                    abaterea_superioara = -0.108
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "T":
                    abaterea_superioara = -0.146
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "U":
                    abaterea_superioara = -0.21
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "V":
                    abaterea_superioara = -0.252
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "X":
                    abaterea_superioara = -0.31
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Y":
                    abaterea_superioara = -0.38
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "Z":
                    abaterea_superioara = -0.465
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZA":
                    abaterea_superioara = -0.6
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZB":
                    abaterea_superioara = -0.78
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
                elif zona == "ZC":
                    abaterea_superioara = -1
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.007
                    if clasa == "7":
                        abaterea_superioara += 0.015
                    if clasa == "8":
                        abaterea_superioara += 0.023
            elif tip == "Arbore" and dimensiune <=140:
                if zona == "a":
                    abaterea_superioara = -0.46
                elif zona == "b":
                    abaterea_superioara = -0.26
                elif zona == "c":
                    abaterea_superioara = -0.2
                elif zona == "d":
                    abaterea_superioara = -0.145
                elif zona == "e":
                    abaterea_superioara = -0.085
                elif zona == "f":
                    abaterea_superioara = -0.043
                elif zona == "g":
                    abaterea_superioara = -0.014
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.011
                    elif clasa == "7":
                        abaterea_inferioara = -0.018
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.003
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.015
                elif zona == "n":
                    abaterea_inferioara = 0.027
                elif zona == "p":
                    abaterea_inferioara = 0.043
                elif zona == "r":
                    abaterea_inferioara = 0.063
                elif zona == "s":
                    abaterea_inferioara = 0.092
                elif zona == "t":
                    abaterea_inferioara = 0.122
                elif zona == "u":
                    abaterea_inferioara = 0.17
                elif zona == "v":
                    abaterea_inferioara = 0.202
                elif zona == "x":
                    abaterea_inferioara = 0.248
                elif zona == "y":
                    abaterea_inferioara = 0.3
                elif zona == "z":
                    abaterea_inferioara = 0.365
                elif zona == "za":
                    abaterea_inferioara = 0.47
                elif zona == "zb":
                    abaterea_inferioara = 0.62
                elif zona == "zc":
                    abaterea_inferioara = 0.8
            elif tip == "Arbore" and dimensiune >140 and dimensiune <=160:
                if zona == "a":
                    abaterea_superioara = -0.52
                elif zona == "b":
                    abaterea_superioara = -0.28
                elif zona == "c":
                    abaterea_superioara = -0.21
                elif zona == "d":
                    abaterea_superioara = -0.145
                elif zona == "e":
                    abaterea_superioara = -0.085
                elif zona == "f":
                    abaterea_superioara = -0.043
                elif zona == "g":
                    abaterea_superioara = -0.014
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.011
                    elif clasa == "7":
                        abaterea_inferioara = -0.018
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.003
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.015
                elif zona == "n":
                    abaterea_inferioara = 0.027
                elif zona == "p":
                    abaterea_inferioara = 0.043
                elif zona == "r":
                    abaterea_inferioara = 0.065
                elif zona == "s":
                    abaterea_inferioara = 0.1
                elif zona == "t":
                    abaterea_inferioara = 0.134
                elif zona == "u":
                    abaterea_inferioara = 0.19
                elif zona == "v":
                    abaterea_inferioara = 0.228
                elif zona == "x":
                    abaterea_inferioara = 0.28
                elif zona == "y":
                    abaterea_inferioara = 0.34
                elif zona == "z":
                    abaterea_inferioara = 0.415
                elif zona == "za":
                    abaterea_inferioara = 0.535
                elif zona == "zb":
                    abaterea_inferioara = 0.7
                elif zona == "zc":
                    abaterea_inferioara = 0.9
            elif tip == "Arbore" and dimensiune >160:
                if zona == "a":
                    abaterea_superioara = -0.58
                elif zona == "b":
                    abaterea_superioara = -0.31
                elif zona == "c":
                    abaterea_superioara = -0.23
                elif zona == "d":
                    abaterea_superioara = -0.145
                elif zona == "e":
                    abaterea_superioara = -0.085
                elif zona == "f":
                    abaterea_superioara = -0.043
                elif zona == "g":
                    abaterea_superioara = -0.014
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.011
                    elif clasa == "7":
                        abaterea_inferioara = -0.018
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.003
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.015
                elif zona == "n":
                    abaterea_inferioara = 0.027
                elif zona == "p":
                    abaterea_inferioara = 0.043
                elif zona == "r":
                    abaterea_inferioara = 0.068
                elif zona == "s":
                    abaterea_inferioara = 0.108
                elif zona == "t":
                    abaterea_inferioara = 0.146
                elif zona == "u":
                    abaterea_inferioara = 0.21
                elif zona == "v":
                    abaterea_inferioara = 0.252
                elif zona == "x":
                    abaterea_inferioara = 0.31
                elif zona == "y":
                    abaterea_inferioara = 0.38
                elif zona == "z":
                    abaterea_inferioara = 0.465
                elif zona == "za":
                    abaterea_inferioara = 0.6
                elif zona == "zb":
                    abaterea_inferioara = 0.78
                elif zona == "zc":
                    abaterea_inferioara = 1
        elif dimensiune >180 and dimensiune <=250:
            if clasa == "01":
                toleranta_dimensionala = 0.002
            elif clasa == "0":
                toleranta_dimensionala = 0.003
            elif clasa == "1":
                toleranta_dimensionala = 0.0045
            elif clasa == "2":
                toleranta_dimensionala = 0.007
            elif clasa == "3":
                toleranta_dimensionala = 0.01
            elif clasa == "4":
                toleranta_dimensionala = 0.014
            elif clasa == "5":
                toleranta_dimensionala = 0.02
            elif clasa == "6":
                toleranta_dimensionala = 0.029
            elif clasa == "7":
                toleranta_dimensionala = 0.046
            elif clasa == "8":
                toleranta_dimensionala = 0.072
            elif clasa == "9":
                toleranta_dimensionala = 0.115
            elif clasa == "10":
                toleranta_dimensionala = 0.185
            elif clasa == "11":
                toleranta_dimensionala = 0.29
            elif clasa == "12":
                toleranta_dimensionala = 0.46
            elif clasa == "13":
                toleranta_dimensionala = 0.72
            elif clasa == "14":
                toleranta_dimensionala = 1.15
            elif clasa == "15":
                toleranta_dimensionala = 1.85
            elif clasa == "16":
                toleranta_dimensionala = 2.9
            elif clasa == "17":
                toleranta_dimensionala = 4.6
            elif clasa == "18":
                toleranta_dimensionala = 7.2
            if tip == "Alezaj" and dimensiune <=200:
                if zona == "A":
                    abaterea_inferioara = 0.66
                elif zona == "B":
                    abaterea_inferioara = 0.34
                elif zona == "C":
                    abaterea_inferioara = 0.24
                elif zona == "D":
                    abaterea_inferioara = 0.17
                elif zona == "E":
                    abaterea_inferioara = 0.1
                elif zona == "F":
                    abaterea_inferioara = 0.05
                elif zona == "G":
                    abaterea_inferioara = 0.015
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.022
                    elif clasa == "7":
                        abaterea_superioara = 0.03
                    elif clasa == "8":
                        abaterea_superioara = 0.047
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.017
                    elif clasa == "3":
                        abaterea_superioara = -0.017 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.017 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.017 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.017 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.017 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.017 + 0.026
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.031
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.031 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.031 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.031 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.031 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.031 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.031 + 0.026
                elif zona == "P":
                    abaterea_superioara = -0.05
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "R":
                    abaterea_superioara = -0.077
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "S":
                    abaterea_superioara = -0.122
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "T":
                    abaterea_superioara = -0.166
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "U":
                    abaterea_superioara = -0.236
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "V":
                    abaterea_superioara = -0.284
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "X":
                    abaterea_superioara = -0.35
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Y":
                    abaterea_superioara = -0.425
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Z":
                    abaterea_superioara = -0.52
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZA":
                    abaterea_superioara = -0.67
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZB":
                    abaterea_superioara = -0.88
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZC":
                    abaterea_superioara = -1.115
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
            elif tip == "Alezaj" and dimensiune >200 and dimensiune <=225:
                if zona == "A":
                    abaterea_inferioara = 0.74
                elif zona == "B":
                    abaterea_inferioara = 0.38
                elif zona == "C":
                    abaterea_inferioara = 0.26
                elif zona == "D":
                    abaterea_inferioara = 0.17
                elif zona == "E":
                    abaterea_inferioara = 0.1
                elif zona == "F":
                    abaterea_inferioara = 0.05
                elif zona == "G":
                    abaterea_inferioara = 0.015
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.022
                    elif clasa == "7":
                        abaterea_superioara = 0.03
                    elif clasa == "8":
                        abaterea_superioara = 0.047
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.017
                    elif clasa == "3":
                        abaterea_superioara = -0.017 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.017 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.017 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.017 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.017 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.017 + 0.026
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.031
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.031 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.031 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.031 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.031 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.031 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.031 + 0.026
                elif zona == "P":
                    abaterea_superioara = -0.05
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "R":
                    abaterea_superioara = -0.08
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "S":
                    abaterea_superioara = -0.13
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "T":
                    abaterea_superioara = -0.18
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "U":
                    abaterea_superioara = -0.258
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "V":
                    abaterea_superioara = -0.31
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "X":
                    abaterea_superioara = -0.385
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Y":
                    abaterea_superioara = -0.47
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Z":
                    abaterea_superioara = -0.575
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZA":
                    abaterea_superioara = -0.74
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZB":
                    abaterea_superioara = -0.96
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZC":
                    abaterea_superioara = -1.25
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
            elif tip == "Alezaj" and dimensiune >225:
                if zona == "A":
                    abaterea_inferioara = 0.82
                elif zona == "B":
                    abaterea_inferioara = 0.42
                elif zona == "C":
                    abaterea_inferioara = 0.28
                elif zona == "D":
                    abaterea_inferioara = 0.17
                elif zona == "E":
                    abaterea_inferioara = 0.1
                elif zona == "F":
                    abaterea_inferioara = 0.05
                elif zona == "G":
                    abaterea_inferioara = 0.015
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.022
                    elif clasa == "7":
                        abaterea_superioara = 0.03
                    elif clasa == "8":
                        abaterea_superioara = 0.047
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.017
                    elif clasa == "3":
                        abaterea_superioara = -0.017 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.017 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.017 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.017 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.017 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.017 + 0.026
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.031
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.031 + 0.003
                    elif clasa == "4":
                        abaterea_superioara = -0.031 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.031 + 0.006
                    elif clasa == "6":
                        abaterea_superioara = -0.031 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.031 + 0.017
                    elif clasa == "8":
                        abaterea_superioara = -0.031 + 0.026
                elif zona == "P":
                    abaterea_superioara = -0.05
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "R":
                    abaterea_superioara = -0.084
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "S":
                    abaterea_superioara = -0.140
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "T":
                    abaterea_superioara = -0.196
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "U":
                    abaterea_superioara = -0.284
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "V":
                    abaterea_superioara = -0.34
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "X":
                    abaterea_superioara = -0.425
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Y":
                    abaterea_superioara = -0.52
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "Z":
                    abaterea_superioara = -0.64
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZA":
                    abaterea_superioara = -0.82
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZB":
                    abaterea_superioara = -1.05
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
                elif zona == "ZC":
                    abaterea_superioara = -1.35
                    if clasa == "3":
                        abaterea_superioara += 0.003
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.006
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.017
                    if clasa == "8":
                        abaterea_superioara += 0.026
            elif tip == "Arbore" and dimensiune <=200:
                if zona == "a":
                    abaterea_superioara = -0.66
                elif zona == "b":
                    abaterea_superioara = -0.34
                elif zona == "c":
                    abaterea_superioara = -0.24
                elif zona == "d":
                    abaterea_superioara = -0.17
                elif zona == "e":
                    abaterea_superioara = -0.1
                elif zona == "f":
                    abaterea_superioara = -0.05
                elif zona == "g":
                    abaterea_superioara = -0.015
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.013
                    elif clasa == "7":
                        abaterea_inferioara = -0.021
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.017
                elif zona == "n":
                    abaterea_inferioara = 0.031
                elif zona == "p":
                    abaterea_inferioara = 0.05
                elif zona == "r":
                    abaterea_inferioara = 0.077
                elif zona == "s":
                    abaterea_inferioara = 0.122
                elif zona == "t":
                    abaterea_inferioara = 0.166
                elif zona == "u":
                    abaterea_inferioara = 0.236
                elif zona == "v":
                    abaterea_inferioara = 0.284
                elif zona == "x":
                    abaterea_inferioara = 0.35
                elif zona == "y":
                    abaterea_inferioara = 0.425
                elif zona == "z":
                    abaterea_inferioara = 0.52
                elif zona == "za":
                    abaterea_inferioara = 0.67
                elif zona == "zb":
                    abaterea_inferioara = 0.88
                elif zona == "zc":
                    abaterea_inferioara = 1.15
            elif tip == "Arbore" and dimensiune >200 and dimensiune <=225:
                if zona == "a":
                    abaterea_superioara = -0.74
                elif zona == "b":
                    abaterea_superioara = -0.38
                elif zona == "c":
                    abaterea_superioara = -0.26
                elif zona == "d":
                    abaterea_superioara = -0.17
                elif zona == "e":
                    abaterea_superioara = -0.1
                elif zona == "f":
                    abaterea_superioara = -0.05
                elif zona == "g":
                    abaterea_superioara = -0.015
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.013
                    elif clasa == "7":
                        abaterea_inferioara = -0.021
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.017
                elif zona == "n":
                    abaterea_inferioara = 0.031
                elif zona == "p":
                    abaterea_inferioara = 0.05
                elif zona == "r":
                    abaterea_inferioara = 0.08
                elif zona == "s":
                    abaterea_inferioara = 0.13
                elif zona == "t":
                    abaterea_inferioara = 0.18
                elif zona == "u":
                    abaterea_inferioara = 0.258
                elif zona == "v":
                    abaterea_inferioara = 0.31
                elif zona == "x":
                    abaterea_inferioara = 0.385
                elif zona == "y":
                    abaterea_inferioara = 0.47
                elif zona == "z":
                    abaterea_inferioara = 0.575
                elif zona == "za":
                    abaterea_inferioara = 0.74
                elif zona == "zb":
                    abaterea_inferioara = 0.96
                elif zona == "zc":
                    abaterea_inferioara = 1.25
            elif tip == "Arbore" and dimensiune >225:
                if zona == "a":
                    abaterea_superioara = -0.82
                elif zona == "b":
                    abaterea_superioara = -0.42
                elif zona == "c":
                    abaterea_superioara = -0.28
                elif zona == "d":
                    abaterea_superioara = -0.17
                elif zona == "e":
                    abaterea_superioara = -0.1
                elif zona == "f":
                    abaterea_superioara = -0.05
                elif zona == "g":
                    abaterea_superioara = -0.015
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.013
                    elif clasa == "7":
                        abaterea_inferioara = -0.021
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.017
                elif zona == "n":
                    abaterea_inferioara = 0.031
                elif zona == "p":
                    abaterea_inferioara = 0.05
                elif zona == "r":
                    abaterea_inferioara = 0.084
                elif zona == "s":
                    abaterea_inferioara = 0.14
                elif zona == "t":
                    abaterea_inferioara = 0.196
                elif zona == "u":
                    abaterea_inferioara = 0.284
                elif zona == "v":
                    abaterea_inferioara = 0.34
                elif zona == "x":
                    abaterea_inferioara = 0.425
                elif zona == "y":
                    abaterea_inferioara = 0.52
                elif zona == "z":
                    abaterea_inferioara = 0.64
                elif zona == "za":
                    abaterea_inferioara = 0.82
                elif zona == "zb":
                    abaterea_inferioara = 1.05
                elif zona == "zc":
                    abaterea_inferioara = 1.35
        elif dimensiune >250 and dimensiune <=315:
            if clasa == "01":
                toleranta_dimensionala = 0.0025
            elif clasa == "0":
                toleranta_dimensionala = 0.004
            elif clasa == "1":
                toleranta_dimensionala = 0.006
            elif clasa == "2":
                toleranta_dimensionala = 0.008
            elif clasa == "3":
                toleranta_dimensionala = 0.012
            elif clasa == "4":
                toleranta_dimensionala = 0.016
            elif clasa == "5":
                toleranta_dimensionala = 0.023
            elif clasa == "6":
                toleranta_dimensionala = 0.032
            elif clasa == "7":
                toleranta_dimensionala = 0.052
            elif clasa == "8":
                toleranta_dimensionala = 0.081
            elif clasa == "9":
                toleranta_dimensionala = 0.13
            elif clasa == "10":
                toleranta_dimensionala = 0.21
            elif clasa == "11":
                toleranta_dimensionala = 0.32
            elif clasa == "12":
                toleranta_dimensionala = 0.52
            elif clasa == "13":
                toleranta_dimensionala = 0.81
            elif clasa == "14":
                toleranta_dimensionala = 1.3
            elif clasa == "15":
                toleranta_dimensionala = 2.1
            elif clasa == "16":
                toleranta_dimensionala = 3.2
            elif clasa == "17":
                toleranta_dimensionala = 5.2
            elif clasa == "18":
                toleranta_dimensionala = 8.1
            if tip == "Alezaj" and dimensiune <=280:
                if zona == "A":
                    abaterea_inferioara = 0.92
                elif zona == "B":
                    abaterea_inferioara = 0.48
                elif zona == "C":
                    abaterea_inferioara = 0.3
                elif zona == "D":
                    abaterea_inferioara = 0.19
                elif zona == "E":
                    abaterea_inferioara = 0.11
                elif zona == "F":
                    abaterea_inferioara = 0.056
                elif zona == "G":
                    abaterea_inferioara = 0.017
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.025
                    elif clasa == "7":
                        abaterea_superioara = 0.036
                    elif clasa == "8":
                        abaterea_superioara = 0.055
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                    elif clasa == "3":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.004 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.004 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.004 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.004 + 0.029
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.02
                    elif clasa == "3":
                        abaterea_superioara = -0.02 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.02 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.02 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.02 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.02 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.02 + 0.029
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.034
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.034 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.034 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.034 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.034 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.034 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.034 + 0.029
                elif zona == "P":
                    abaterea_superioara = -0.056
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "R":
                    abaterea_superioara = -0.094
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "S":
                    abaterea_superioara = -0.158
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "T":
                    abaterea_superioara = -0.218
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "U":
                    abaterea_superioara = -0.315
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "V":
                    abaterea_superioara = -0.385
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "X":
                    abaterea_superioara = -0.475
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "Y":
                    abaterea_superioara = -0.58
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "Z":
                    abaterea_superioara = -0.71
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZA":
                    abaterea_superioara = -0.92
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZB":
                    abaterea_superioara = -1.2
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZC":
                    abaterea_superioara = -1.55
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
            elif tip == "Alezaj" and dimensiune >280:
                if zona == "A":
                    abaterea_inferioara = 1.05
                elif zona == "B":
                    abaterea_inferioara = 0.54
                elif zona == "C":
                    abaterea_inferioara = 0.33
                elif zona == "D":
                    abaterea_inferioara = 0.19
                elif zona == "E":
                    abaterea_inferioara = 0.11
                elif zona == "F":
                    abaterea_inferioara = 0.056
                elif zona == "G":
                    abaterea_inferioara = 0.017
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.025
                    elif clasa == "7":
                        abaterea_superioara = 0.036
                    elif clasa == "8":
                        abaterea_superioara = 0.055
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                    elif clasa == "3":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.004 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.004 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.004 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.004 + 0.029
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.02
                    elif clasa == "3":
                        abaterea_superioara = -0.02 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.02 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.02 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.02 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.02 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.02 + 0.029
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.034
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.034 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.034 + 0.004
                    elif clasa == "5":
                        abaterea_superioara = -0.034 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.034 + 0.009
                    elif clasa == "7":
                        abaterea_superioara = -0.034 + 0.02
                    elif clasa == "8":
                        abaterea_superioara = -0.034 + 0.029
                elif zona == "P":
                    abaterea_superioara = -0.056
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "R":
                    abaterea_superioara = -0.098
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "S":
                    abaterea_superioara = -0.17
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "T":
                    abaterea_superioara = -0.24
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "U":
                    abaterea_superioara = -0.35
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "V":
                    abaterea_superioara = -0.425
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "X":
                    abaterea_superioara = -0.525
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "Y":
                    abaterea_superioara = -0.65
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "Z":
                    abaterea_superioara = -0.79
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZA":
                    abaterea_superioara = -1
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZB":
                    abaterea_superioara = -1.3
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
                elif zona == "ZC":
                    abaterea_superioara = -1.7
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.004
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.009
                    if clasa == "7":
                        abaterea_superioara += 0.02
                    if clasa == "8":
                        abaterea_superioara += 0.029
            elif tip == "Arbore" and dimensiune <=280:
                if zona == "a":
                    abaterea_superioara = -0.92
                elif zona == "b":
                    abaterea_superioara = -0.48
                elif zona == "c":
                    abaterea_superioara = -0.3
                elif zona == "d":
                    abaterea_superioara = -0.19
                elif zona == "e":
                    abaterea_superioara = -0.11
                elif zona == "f":
                    abaterea_superioara = -0.056
                elif zona == "g":
                    abaterea_superioara = -0.017
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.016
                    elif clasa == "7":
                        abaterea_inferioara = -0.026
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.02
                elif zona == "n":
                    abaterea_inferioara = 0.034
                elif zona == "p":
                    abaterea_inferioara = 0.056
                elif zona == "r":
                    abaterea_inferioara = 0.094
                elif zona == "s":
                    abaterea_inferioara = 0.158
                elif zona == "t":
                    abaterea_inferioara = 0.218
                elif zona == "u":
                    abaterea_inferioara = 0.315
                elif zona == "v":
                    abaterea_inferioara = 0.385
                elif zona == "x":
                    abaterea_inferioara = 0.475
                elif zona == "y":
                    abaterea_inferioara = 0.58
                elif zona == "z":
                    abaterea_inferioara = 0.71
                elif zona == "za":
                    abaterea_inferioara = 0.92
                elif zona == "zb":
                    abaterea_inferioara = 1.2
                elif zona == "zc":
                    abaterea_inferioara = 1.55
            elif tip == "Arbore" and dimensiune >280:
                if zona == "a":
                    abaterea_superioara = -1.05
                elif zona == "b":
                    abaterea_superioara = -0.54
                elif zona == "c":
                    abaterea_superioara = -0.33
                elif zona == "d":
                    abaterea_superioara = -0.19
                elif zona == "e":
                    abaterea_superioara = -0.11
                elif zona == "f":
                    abaterea_superioara = -0.056
                elif zona == "g":
                    abaterea_superioara = -0.017
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.016
                    elif clasa == "7":
                        abaterea_inferioara = -0.026
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.02
                elif zona == "n":
                    abaterea_inferioara = 0.034
                elif zona == "p":
                    abaterea_inferioara = 0.056
                elif zona == "r":
                    abaterea_inferioara = 0.098
                elif zona == "s":
                    abaterea_inferioara = 0.17
                elif zona == "t":
                    abaterea_inferioara = 0.24
                elif zona == "u":
                    abaterea_inferioara = 0.35
                elif zona == "v":
                    abaterea_inferioara = 0.425
                elif zona == "x":
                    abaterea_inferioara = 0.525
                elif zona == "y":
                    abaterea_inferioara = 0.65
                elif zona == "z":
                    abaterea_inferioara = 0.79
                elif zona == "za":
                    abaterea_inferioara = 1
                elif zona == "zb":
                    abaterea_inferioara = 1.3
                elif zona == "zc":
                    abaterea_inferioara = 1.7
        elif dimensiune >315 and dimensiune <=400:
            if clasa == "01":
                toleranta_dimensionala = 0.003
            elif clasa == "0":
                toleranta_dimensionala = 0.005
            elif clasa == "1":
                toleranta_dimensionala = 0.007
            elif clasa == "2":
                toleranta_dimensionala = 0.009
            elif clasa == "3":
                toleranta_dimensionala = 0.013
            elif clasa == "4":
                toleranta_dimensionala = 0.018
            elif clasa == "5":
                toleranta_dimensionala = 0.025
            elif clasa == "6":
                toleranta_dimensionala = 0.036
            elif clasa == "7":
                toleranta_dimensionala = 0.057
            elif clasa == "8":
                toleranta_dimensionala = 0.089
            elif clasa == "9":
                toleranta_dimensionala = 0.14
            elif clasa == "10":
                toleranta_dimensionala = 0.23
            elif clasa == "11":
                toleranta_dimensionala = 0.36
            elif clasa == "12":
                toleranta_dimensionala = 0.57
            elif clasa == "13":
                toleranta_dimensionala = 0.89
            elif clasa == "14":
                toleranta_dimensionala = 1.4
            elif clasa == "15":
                toleranta_dimensionala = 2.3
            elif clasa == "16":
                toleranta_dimensionala = 3.6
            elif clasa == "17":
                toleranta_dimensionala = 5.7
            elif clasa == "18":
                toleranta_dimensionala = 8.9
            if tip == "Alezaj" and dimensiune <=355:
                if zona == "A":
                    abaterea_inferioara = 1.2
                elif zona == "B":
                    abaterea_inferioara = 0.6
                elif zona == "C":
                    abaterea_inferioara = 0.36
                elif zona == "D":
                    abaterea_inferioara = 0.21
                elif zona == "E":
                    abaterea_inferioara = 0.125
                elif zona == "F":
                    abaterea_inferioara = 0.062
                elif zona == "G":
                    abaterea_inferioara = 0.018
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.029
                    elif clasa == "7":
                        abaterea_superioara = 0.039
                    elif clasa == "8":
                        abaterea_superioara = 0.06
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                    elif clasa == "3":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.004 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.004 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.004 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.004 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.004 + 0.032
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.021
                    elif clasa == "3":
                        abaterea_superioara = -0.021 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.021 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.021 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.021 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.021 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.021 + 0.032
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.037
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.037 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.037 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.037 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.037 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.037 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.037 + 0.032
                elif zona == "P":
                    abaterea_superioara = -0.062
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "R":
                    abaterea_superioara = -0.108
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "S":
                    abaterea_superioara = -0.19
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "T":
                    abaterea_superioara = -0.268
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "U":
                    abaterea_superioara = -0.39
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "V":
                    abaterea_superioara = -0.475
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "X":
                    abaterea_superioara = -0.59
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "Y":
                    abaterea_superioara = -0.73
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "Z":
                    abaterea_superioara = -0.9
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZA":
                    abaterea_superioara = -1.15
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZB":
                    abaterea_superioara = -1.5
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZC":
                    abaterea_superioara = -1.9
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
            elif tip == "Alezaj" and dimensiune >355:
                if zona == "A":
                    abaterea_inferioara = 1.35
                elif zona == "B":
                    abaterea_inferioara = 0.68
                elif zona == "C":
                    abaterea_inferioara = 0.4
                elif zona == "D":
                    abaterea_inferioara = 0.21
                elif zona == "E":
                    abaterea_inferioara = 0.125
                elif zona == "F":
                    abaterea_inferioara = 0.062
                elif zona == "G":
                    abaterea_inferioara = 0.018
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.029
                    elif clasa == "7":
                        abaterea_superioara = 0.039
                    elif clasa == "8":
                        abaterea_superioara = 0.06
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.004
                    elif clasa == "3":
                        abaterea_superioara = -0.004 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.004 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.004 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.004 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.004 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.004 + 0.032
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.021
                    elif clasa == "3":
                        abaterea_superioara = -0.021 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.021 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.021 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.021 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.021 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.021 + 0.032
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.037
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.037 + 0.004
                    elif clasa == "4":
                        abaterea_superioara = -0.037 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.037 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.037 + 0.011
                    elif clasa == "7":
                        abaterea_superioara = -0.037 + 0.021
                    elif clasa == "8":
                        abaterea_superioara = -0.037 + 0.032
                elif zona == "P":
                    abaterea_superioara = -0.062
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "R":
                    abaterea_superioara = -0.114
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "S":
                    abaterea_superioara = -0.208
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "T":
                    abaterea_superioara = -0.294
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "U":
                    abaterea_superioara = -0.435
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "V":
                    abaterea_superioara = -0.53
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "X":
                    abaterea_superioara = -0.66
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "Y":
                    abaterea_superioara = -0.82
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "Z":
                    abaterea_superioara = -1
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZA":
                    abaterea_superioara = -1.3
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZB":
                    abaterea_superioara = -1.65
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
                elif zona == "ZC":
                    abaterea_superioara = -2.1
                    if clasa == "3":
                        abaterea_superioara += 0.004
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.011
                    if clasa == "7":
                        abaterea_superioara += 0.021
                    if clasa == "8":
                        abaterea_superioara += 0.032
            elif tip == "Arbore" and dimensiune <=355:
                if zona == "a":
                    abaterea_superioara = -1.2
                elif zona == "b":
                    abaterea_superioara = -0.6
                elif zona == "c":
                    abaterea_superioara = -0.36
                elif zona == "d":
                    abaterea_superioara = -0.21
                elif zona == "e":
                    abaterea_superioara = -0.125
                elif zona == "f":
                    abaterea_superioara = -0.062
                elif zona == "g":
                    abaterea_superioara = -0.018
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.018
                    elif clasa == "7":
                        abaterea_inferioara = -0.028
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.021
                elif zona == "n":
                    abaterea_inferioara = 0.037
                elif zona == "p":
                    abaterea_inferioara = 0.062
                elif zona == "r":
                    abaterea_inferioara = 0.108
                elif zona == "s":
                    abaterea_inferioara = 0.19
                elif zona == "t":
                    abaterea_inferioara = 0.268
                elif zona == "u":
                    abaterea_inferioara = 0.39
                elif zona == "v":
                    abaterea_inferioara = 0.475
                elif zona == "x":
                    abaterea_inferioara = 0.59
                elif zona == "y":
                    abaterea_inferioara = 0.73
                elif zona == "z":
                    abaterea_inferioara = 0.9
                elif zona == "za":
                    abaterea_inferioara = 1.15
                elif zona == "zb":
                    abaterea_inferioara = 1.5
                elif zona == "zc":
                    abaterea_inferioara = 1.9
            elif tip == "Arbore" and dimensiune >355:
                if zona == "a":
                    abaterea_superioara = -1.35
                elif zona == "b":
                    abaterea_superioara = -0.68
                elif zona == "c":
                    abaterea_superioara = -0.4
                elif zona == "d":
                    abaterea_superioara = -0.21
                elif zona == "e":
                    abaterea_superioara = -0.125
                elif zona == "f":
                    abaterea_superioara = -0.062
                elif zona == "g":
                    abaterea_superioara = -0.018
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.018
                    elif clasa == "7":
                        abaterea_inferioara = -0.028
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.004
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.021
                elif zona == "n":
                    abaterea_inferioara = 0.037
                elif zona == "p":
                    abaterea_inferioara = 0.062
                elif zona == "r":
                    abaterea_inferioara = 0.114
                elif zona == "s":
                    abaterea_inferioara = 0.208
                elif zona == "t":
                    abaterea_inferioara = 0.294
                elif zona == "u":
                    abaterea_inferioara = 0.435
                elif zona == "v":
                    abaterea_inferioara = 0.53
                elif zona == "x":
                    abaterea_inferioara = 0.66
                elif zona == "y":
                    abaterea_inferioara = 0.82
                elif zona == "z":
                    abaterea_inferioara = 1
                elif zona == "za":
                    abaterea_inferioara = 1.3
                elif zona == "zb":
                    abaterea_inferioara = 1.65
                elif zona == "zc":
                    abaterea_inferioara = 2.1
        elif dimensiune >400 and dimensiune <=500:
            if clasa == "01":
                toleranta_dimensionala = 0.004
            elif clasa == "0":
                toleranta_dimensionala = 0.006
            elif clasa == "1":
                toleranta_dimensionala = 0.008
            elif clasa == "2":
                toleranta_dimensionala = 0.01
            elif clasa == "3":
                toleranta_dimensionala = 0.015
            elif clasa == "4":
                toleranta_dimensionala = 0.02
            elif clasa == "5":
                toleranta_dimensionala = 0.027
            elif clasa == "6":
                toleranta_dimensionala = 0.04
            elif clasa == "7":
                toleranta_dimensionala = 0.063
            elif clasa == "8":
                toleranta_dimensionala = 0.097
            elif clasa == "9":
                toleranta_dimensionala = 0.155
            elif clasa == "10":
                toleranta_dimensionala = 0.25
            elif clasa == "11":
                toleranta_dimensionala = 0.4
            elif clasa == "12":
                toleranta_dimensionala = 0.63
            elif clasa == "13":
                toleranta_dimensionala = 0.97
            elif clasa == "14":
                toleranta_dimensionala = 1.55
            elif clasa == "15":
                toleranta_dimensionala = 2.5
            elif clasa == "16":
                toleranta_dimensionala = 4
            elif clasa == "17":
                toleranta_dimensionala = 6.3
            elif clasa == "18":
                toleranta_dimensionala = 9.7
            if tip == "Alezaj" and dimensiune <=450:
                if zona == "A":
                    abaterea_inferioara = 1.5
                elif zona == "B":
                    abaterea_inferioara = 0.76
                elif zona == "C":
                    abaterea_inferioara = 0.44
                elif zona == "D":
                    abaterea_inferioara = 0.23
                elif zona == "E":
                    abaterea_inferioara = 0.135
                elif zona == "F":
                    abaterea_inferioara = 0.068
                elif zona == "G":
                    abaterea_inferioara = 0.02
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.033
                    elif clasa == "7":
                        abaterea_superioara = 0.043
                    elif clasa == "8":
                        abaterea_superioara = 0.068
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.005
                    elif clasa == "3":
                        abaterea_superioara = -0.005 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.005 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.005 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.005 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.005 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.005 + 0.034
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.023
                    elif clasa == "3":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.023 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.023 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.023 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.023 + 0.034
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.04
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.04 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.04 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.04 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.04 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.04 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.04 + 0.034
                elif zona == "P":
                    abaterea_superioara = -0.068
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "R":
                    abaterea_superioara = -0.126
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "S":
                    abaterea_superioara = -0.232
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "T":
                    abaterea_superioara = -0.33
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "U":
                    abaterea_superioara = -0.49
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "V":
                    abaterea_superioara = -0.595
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "X":
                    abaterea_superioara = -0.74
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "Y":
                    abaterea_superioara = -0.92
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "Z":
                    abaterea_superioara = -1.1
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZA":
                    abaterea_superioara = -1.45
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZB":
                    abaterea_superioara = -1.85
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZC":
                    abaterea_superioara = -2.4
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
            elif tip == "Alezaj" and dimensiune >450:
                if zona == "A":
                    abaterea_inferioara = 1.65
                elif zona == "B":
                    abaterea_inferioara = 0.84
                elif zona == "C":
                    abaterea_inferioara = 0.48
                elif zona == "D":
                    abaterea_inferioara = 0.23
                elif zona == "E":
                    abaterea_inferioara = 0.135
                elif zona == "F":
                    abaterea_inferioara = 0.068
                elif zona == "G":
                    abaterea_inferioara = 0.02
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "J":
                    if clasa == "6":
                        abaterea_superioara = 0.033
                    elif clasa == "7":
                        abaterea_superioara = 0.043
                    elif clasa == "8":
                        abaterea_superioara = 0.068
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = -0.005
                    elif clasa == "3":
                        abaterea_superioara = -0.005 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.005 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.005 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.005 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.005 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.005 + 0.034
                elif zona == "M":
                    if int(clasa) <=2 or int(clasa) >=9:
                        abaterea_superioara = -0.023
                    elif clasa == "3":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.023 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.023 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.023 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.023 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.023 + 0.034
                elif zona == "N":
                    if int(clasa) <=2:
                        abaterea_superioara = -0.04
                    elif int(clasa) >=9:
                        abaterea_superioara = 0
                    elif clasa == "3":
                        abaterea_superioara = -0.04 + 0.005
                    elif clasa == "4":
                        abaterea_superioara = -0.04 + 0.005
                    elif clasa == "5":
                        abaterea_superioara = -0.04 + 0.007
                    elif clasa == "6":
                        abaterea_superioara = -0.04 + 0.013
                    elif clasa == "7":
                        abaterea_superioara = -0.04 + 0.023
                    elif clasa == "8":
                        abaterea_superioara = -0.04 + 0.034
                elif zona == "P":
                    abaterea_superioara = -0.068
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "R":
                    abaterea_superioara = -0.132
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "S":
                    abaterea_superioara = -0.252
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "T":
                    abaterea_superioara = -0.36
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "U":
                    abaterea_superioara = -0.54
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "V":
                    abaterea_superioara = -0.66
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "X":
                    abaterea_superioara = -0.82
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "Y":
                    abaterea_superioara = -1
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "Z":
                    abaterea_superioara = -1.25
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZA":
                    abaterea_superioara = -1.6
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZB":
                    abaterea_superioara = -2.1
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
                elif zona == "ZC":
                    abaterea_superioara = -2.6
                    if clasa == "3":
                        abaterea_superioara += 0.005
                    if clasa == "4":
                        abaterea_superioara += 0.005
                    if clasa == "5":
                        abaterea_superioara += 0.007
                    if clasa == "6":
                        abaterea_superioara += 0.013
                    if clasa == "7":
                        abaterea_superioara += 0.023
                    if clasa == "8":
                        abaterea_superioara += 0.034
            elif tip == "Arbore" and dimensiune <=450:
                if zona == "a":
                    abaterea_superioara = -1.5
                elif zona == "b":
                    abaterea_superioara = -0.76
                elif zona == "c":
                    abaterea_superioara = -0.44
                elif zona == "d":
                    abaterea_superioara = -0.23
                elif zona == "e":
                    abaterea_superioara = -0.135
                elif zona == "f":
                    abaterea_superioara = -0.068
                elif zona == "g":
                    abaterea_superioara = -0.02
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.02
                    elif clasa == "7":
                        abaterea_inferioara = -0.032
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.005
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.023
                elif zona == "n":
                    abaterea_inferioara = 0.04
                elif zona == "p":
                    abaterea_inferioara = 0.068
                elif zona == "r":
                    abaterea_inferioara = 0.126
                elif zona == "s":
                    abaterea_inferioara = 0.232
                elif zona == "t":
                    abaterea_inferioara = 0.33
                elif zona == "u":
                    abaterea_inferioara = 0.49
                elif zona == "v":
                    abaterea_inferioara = 0.595
                elif zona == "x":
                    abaterea_inferioara = 0.74
                elif zona == "y":
                    abaterea_inferioara = 0.92
                elif zona == "z":
                    abaterea_inferioara = 1.1
                elif zona == "za":
                    abaterea_inferioara = 1.45
                elif zona == "zb":
                    abaterea_inferioara = 1.85
                elif zona == "zc":
                    abaterea_inferioara = 2.4
            elif tip == "Arbore" and dimensiune >450:
                if zona == "a":
                    abaterea_superioara = -1.65
                elif zona == "b":
                    abaterea_superioara = -0.84
                elif zona == "c":
                    abaterea_superioara = -0.48
                elif zona == "d":
                    abaterea_superioara = -0.23
                elif zona == "e":
                    abaterea_superioara = -0.135
                elif zona == "f":
                    abaterea_superioara = -0.068
                elif zona == "g":
                    abaterea_superioara = -0.02
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "j":
                    if clasa == "5" or clasa == "6":
                        abaterea_inferioara = -0.02
                    elif clasa == "7":
                        abaterea_inferioara = -0.032
                elif zona == "k":
                    if int(clasa)>=4 and int(clasa)<=7:
                        abaterea_inferioara = 0.005
                    else:
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.023
                elif zona == "n":
                    abaterea_inferioara = 0.04
                elif zona == "p":
                    abaterea_inferioara = 0.068
                elif zona == "r":
                    abaterea_inferioara = 0.132
                elif zona == "s":
                    abaterea_inferioara = 0.252
                elif zona == "t":
                    abaterea_inferioara = 0.36
                elif zona == "u":
                    abaterea_inferioara = 0.54
                elif zona == "v":
                    abaterea_inferioara = 0.66
                elif zona == "x":
                    abaterea_inferioara = 0.82
                elif zona == "y":
                    abaterea_inferioara = 1
                elif zona == "z":
                    abaterea_inferioara = 1.25
                elif zona == "za":
                    abaterea_inferioara = 1.6
                elif zona == "zb":
                    abaterea_inferioara = 2.1
                elif zona == "zc":
                    abaterea_inferioara = 2.6
        elif dimensiune >500 and dimensiune <=630:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.009
            elif clasa == "2":
                toleranta_dimensionala = 0.011
            elif clasa == "3":
                toleranta_dimensionala = 0.016
            elif clasa == "4":
                toleranta_dimensionala = 0.022
            elif clasa == "5":
                toleranta_dimensionala = 0.032
            elif clasa == "6":
                toleranta_dimensionala = 0.044
            elif clasa == "7":
                toleranta_dimensionala = 0.07
            elif clasa == "8":
                toleranta_dimensionala = 0.11
            elif clasa == "9":
                toleranta_dimensionala = 0.175
            elif clasa == "10":
                toleranta_dimensionala = 0.28
            elif clasa == "11":
                toleranta_dimensionala = 0.44
            elif clasa == "12":
                toleranta_dimensionala = 0.7
            elif clasa == "13":
                toleranta_dimensionala = 1.1
            elif clasa == "14":
                toleranta_dimensionala = 1.75
            elif clasa == "15":
                toleranta_dimensionala = 2.8
            elif clasa == "16":
                toleranta_dimensionala = 4.4
            elif clasa == "17":
                toleranta_dimensionala = 7
            elif clasa == "18":
                toleranta_dimensionala = 11
            if tip == "Alezaj" and dimensiune <=560:
                if zona == "D":
                    abaterea_inferioara = 0.26
                elif zona == "E":
                    abaterea_inferioara = 0.145
                elif zona == "F":
                    abaterea_inferioara = 0.076
                elif zona == "G":
                    abaterea_inferioara = 0.022
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.026
                elif zona == "N":
                    abaterea_superioara = -0.044
                elif zona == "P":
                    abaterea_superioara = -0.078
                elif zona == "R":
                    abaterea_superioara = -0.15
                elif zona == "S":
                    abaterea_superioara = -0.28
                elif zona == "T":
                    abaterea_superioara = -0.4
                elif zona == "U":
                    abaterea_superioara = -0.6
            elif tip == "Alezaj" and dimensiune >560:
                if zona == "D":
                    abaterea_inferioara = 0.26
                elif zona == "E":
                    abaterea_inferioara = 0.145
                elif zona == "F":
                    abaterea_inferioara = 0.076
                elif zona == "G":
                    abaterea_inferioara = 0.022
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.026
                elif zona == "N":
                    abaterea_superioara = -0.044
                elif zona == "P":
                    abaterea_superioara = -0.078
                elif zona == "R":
                    abaterea_superioara = -0.155
                elif zona == "S":
                    abaterea_superioara = -0.31
                elif zona == "T":
                    abaterea_superioara = -0.45
                elif zona == "U":
                    abaterea_superioara = -0.66
            elif tip == "Arbore" and dimensiune <=560:
                if zona == "d":
                    abaterea_superioara = -0.26
                elif zona == "e":
                    abaterea_superioara = -0.145
                elif zona == "f":
                    abaterea_superioara = -0.076
                elif zona == "g":
                    abaterea_superioara = -0.022
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.026
                elif zona == "n":
                    abaterea_inferioara = 0.044
                elif zona == "p":
                    abaterea_inferioara = 0.078
                elif zona == "r":
                    abaterea_inferioara = 0.15
                elif zona == "s":
                    abaterea_inferioara = 0.28
                elif zona == "t":
                    abaterea_inferioara = 0.4
                elif zona == "u":
                    abaterea_inferioara = 0.6
            elif tip == "Arbore" and dimensiune >560:
                if zona == "d":
                    abaterea_superioara = -0.26
                elif zona == "e":
                    abaterea_superioara = -0.145
                elif zona == "f":
                    abaterea_superioara = -0.076
                elif zona == "g":
                    abaterea_superioara = -0.022
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.026
                elif zona == "n":
                    abaterea_inferioara = 0.044
                elif zona == "p":
                    abaterea_inferioara = 0.078
                elif zona == "r":
                    abaterea_inferioara = 0.155
                elif zona == "s":
                    abaterea_inferioara = 0.31
                elif zona == "t":
                    abaterea_inferioara = 0.45
                elif zona == "u":
                    abaterea_inferioara = 0.66
        elif dimensiune >630 and dimensiune <=800:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.01
            elif clasa == "2":
                toleranta_dimensionala = 0.013
            elif clasa == "3":
                toleranta_dimensionala = 0.018
            elif clasa == "4":
                toleranta_dimensionala = 0.025
            elif clasa == "5":
                toleranta_dimensionala = 0.036
            elif clasa == "6":
                toleranta_dimensionala = 0.05
            elif clasa == "7":
                toleranta_dimensionala = 0.08
            elif clasa == "8":
                toleranta_dimensionala = 0.125
            elif clasa == "9":
                toleranta_dimensionala = 0.2
            elif clasa == "10":
                toleranta_dimensionala = 0.32
            elif clasa == "11":
                toleranta_dimensionala = 0.5
            elif clasa == "12":
                toleranta_dimensionala = 0.8
            elif clasa == "13":
                toleranta_dimensionala = 1.25
            elif clasa == "14":
                toleranta_dimensionala = 2
            elif clasa == "15":
                toleranta_dimensionala = 3.2
            elif clasa == "16":
                toleranta_dimensionala = 5
            elif clasa == "17":
                toleranta_dimensionala = 8
            elif clasa == "18":
                toleranta_dimensionala = 12.5
            if tip == "Alezaj" and dimensiune <=710:
                if zona == "D":
                    abaterea_inferioara = 0.29
                elif zona == "E":
                    abaterea_inferioara = 0.16
                elif zona == "F":
                    abaterea_inferioara = 0.08
                elif zona == "G":
                    abaterea_inferioara = 0.024
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.03
                elif zona == "N":
                    abaterea_superioara = -0.05
                elif zona == "P":
                    abaterea_superioara = -0.088
                elif zona == "R":
                    abaterea_superioara = -0.175
                elif zona == "S":
                    abaterea_superioara = -0.34
                elif zona == "T":
                    abaterea_superioara = -0.5
                elif zona == "U":
                    abaterea_superioara = -0.74
            elif tip == "Alezaj" and dimensiune >710:
                if zona == "D":
                    abaterea_inferioara = 0.29
                elif zona == "E":
                    abaterea_inferioara = 0.16
                elif zona == "F":
                    abaterea_inferioara = 0.08
                elif zona == "G":
                    abaterea_inferioara = 0.024
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.03
                elif zona == "N":
                    abaterea_superioara = -0.05
                elif zona == "P":
                    abaterea_superioara = -0.088
                elif zona == "R":
                    abaterea_superioara = -0.185
                elif zona == "S":
                    abaterea_superioara = -0.38
                elif zona == "T":
                    abaterea_superioara = -0.56
                elif zona == "U":
                    abaterea_superioara = -0.84
            elif tip == "Arbore" and dimensiune <=710:
                if zona == "d":
                    abaterea_superioara = -0.29
                elif zona == "e":
                    abaterea_superioara = -0.16
                elif zona == "f":
                    abaterea_superioara = -0.08
                elif zona == "g":
                    abaterea_superioara = -0.024
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.03
                elif zona == "n":
                    abaterea_inferioara = 0.05
                elif zona == "p":
                    abaterea_inferioara = 0.088
                elif zona == "r":
                    abaterea_inferioara = 0.175
                elif zona == "s":
                    abaterea_inferioara = 0.34
                elif zona == "t":
                    abaterea_inferioara = 0.5
                elif zona == "u":
                    abaterea_inferioara = 0.74
            elif tip == "Arbore" and dimensiune >710:
                if zona == "d":
                    abaterea_superioara = -0.29
                elif zona == "e":
                    abaterea_superioara = -0.16
                elif zona == "f":
                    abaterea_superioara = -0.08
                elif zona == "g":
                    abaterea_superioara = -0.024
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.03
                elif zona == "n":
                    abaterea_inferioara = 0.05
                elif zona == "p":
                    abaterea_inferioara = 0.088
                elif zona == "r":
                    abaterea_inferioara = 0.185
                elif zona == "s":
                    abaterea_inferioara = 0.38
                elif zona == "t":
                    abaterea_inferioara = 0.56
                elif zona == "u":
                    abaterea_inferioara = 0.84
        elif dimensiune >800 and dimensiune <=1000:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.011
            elif clasa == "2":
                toleranta_dimensionala = 0.015
            elif clasa == "3":
                toleranta_dimensionala = 0.021
            elif clasa == "4":
                toleranta_dimensionala = 0.028
            elif clasa == "5":
                toleranta_dimensionala = 0.04
            elif clasa == "6":
                toleranta_dimensionala = 0.056
            elif clasa == "7":
                toleranta_dimensionala = 0.09
            elif clasa == "8":
                toleranta_dimensionala = 0.14
            elif clasa == "9":
                toleranta_dimensionala = 0.23
            elif clasa == "10":
                toleranta_dimensionala = 0.36
            elif clasa == "11":
                toleranta_dimensionala = 0.56
            elif clasa == "12":
                toleranta_dimensionala = 0.9
            elif clasa == "13":
                toleranta_dimensionala = 1.4
            elif clasa == "14":
                toleranta_dimensionala = 2.3
            elif clasa == "15":
                toleranta_dimensionala = 3.6
            elif clasa == "16":
                toleranta_dimensionala = 5.6
            elif clasa == "17":
                toleranta_dimensionala = 9
            elif clasa == "18":
                toleranta_dimensionala = 14
            if tip == "Alezaj" and dimensiune <=900:
                if zona == "D":
                    abaterea_inferioara = 0.32
                elif zona == "E":
                    abaterea_inferioara = 0.17
                elif zona == "F":
                    abaterea_inferioara = 0.086
                elif zona == "G":
                    abaterea_inferioara = 0.026
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.034
                elif zona == "N":
                    abaterea_superioara = -0.056
                elif zona == "P":
                    abaterea_superioara = -0.1
                elif zona == "R":
                    abaterea_superioara = -0.21
                elif zona == "S":
                    abaterea_superioara = -0.43
                elif zona == "T":
                    abaterea_superioara = -0.62
                elif zona == "U":
                    abaterea_superioara = -0.94
            elif tip == "Alezaj" and dimensiune >900:
                if zona == "D":
                    abaterea_inferioara = 0.32
                elif zona == "E":
                    abaterea_inferioara = 0.17
                elif zona == "F":
                    abaterea_inferioara = 0.086
                elif zona == "G":
                    abaterea_inferioara = 0.026
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.034
                elif zona == "N":
                    abaterea_superioara = -0.056
                elif zona == "P":
                    abaterea_superioara = -0.1
                elif zona == "R":
                    abaterea_superioara = -0.22
                elif zona == "S":
                    abaterea_superioara = -0.47
                elif zona == "T":
                    abaterea_superioara = -0.68
                elif zona == "U":
                    abaterea_superioara = -1.05
            elif tip == "Arbore" and dimensiune <=900:
                if zona == "d":
                    abaterea_superioara = -0.32
                elif zona == "e":
                    abaterea_superioara = -0.17
                elif zona == "f":
                    abaterea_superioara = -0.086
                elif zona == "g":
                    abaterea_superioara = -0.026
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.034
                elif zona == "n":
                    abaterea_inferioara = 0.056
                elif zona == "p":
                    abaterea_inferioara = 0.1
                elif zona == "r":
                    abaterea_inferioara = 0.21
                elif zona == "s":
                    abaterea_inferioara = 0.43
                elif zona == "t":
                    abaterea_inferioara = 0.62
                elif zona == "u":
                    abaterea_inferioara = 0.94
            elif tip == "Arbore" and dimensiune >900:
                if zona == "d":
                    abaterea_superioara = -0.32
                elif zona == "e":
                    abaterea_superioara = -0.17
                elif zona == "f":
                    abaterea_superioara = -0.086
                elif zona == "g":
                    abaterea_superioara = -0.026
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.034
                elif zona == "n":
                    abaterea_inferioara = 0.056
                elif zona == "p":
                    abaterea_inferioara = 0.1
                elif zona == "r":
                    abaterea_inferioara = 0.22
                elif zona == "s":
                    abaterea_inferioara = 0.47
                elif zona == "t":
                    abaterea_inferioara = 0.68
                elif zona == "u":
                    abaterea_inferioara = 1.05
        elif dimensiune >1000 and dimensiune <=1250:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.013
            elif clasa == "2":
                toleranta_dimensionala = 0.018
            elif clasa == "3":
                toleranta_dimensionala = 0.024
            elif clasa == "4":
                toleranta_dimensionala = 0.033
            elif clasa == "5":
                toleranta_dimensionala = 0.047
            elif clasa == "6":
                toleranta_dimensionala = 0.066
            elif clasa == "7":
                toleranta_dimensionala = 0.105
            elif clasa == "8":
                toleranta_dimensionala = 0.165
            elif clasa == "9":
                toleranta_dimensionala = 0.26
            elif clasa == "10":
                toleranta_dimensionala = 0.42
            elif clasa == "11":
                toleranta_dimensionala = 0.66
            elif clasa == "12":
                toleranta_dimensionala = 1.05
            elif clasa == "13":
                toleranta_dimensionala = 1.65
            elif clasa == "14":
                toleranta_dimensionala = 2.6
            elif clasa == "15":
                toleranta_dimensionala = 4.2
            elif clasa == "16":
                toleranta_dimensionala = 6.6
            elif clasa == "17":
                toleranta_dimensionala = 10.5
            elif clasa == "18":
                toleranta_dimensionala = 16.5
            if tip == "Alezaj" and dimensiune <=1120:
                if zona == "D":
                    abaterea_inferioara = 0.35
                elif zona == "E":
                    abaterea_inferioara = 0.195
                elif zona == "F":
                    abaterea_inferioara = 0.098
                elif zona == "G":
                    abaterea_inferioara = 0.028
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.04
                elif zona == "N":
                    abaterea_superioara = -0.066
                elif zona == "P":
                    abaterea_superioara = -0.12
                elif zona == "R":
                    abaterea_superioara = -0.25
                elif zona == "S":
                    abaterea_superioara = -0.52
                elif zona == "T":
                    abaterea_superioara = -0.78
                elif zona == "U":
                    abaterea_superioara = -1.15
            elif tip == "Alezaj" and dimensiune >1120:
                if zona == "D":
                    abaterea_inferioara = 0.35
                elif zona == "E":
                    abaterea_inferioara = 0.195
                elif zona == "F":
                    abaterea_inferioara = 0.098
                elif zona == "G":
                    abaterea_inferioara = 0.028
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.04
                elif zona == "N":
                    abaterea_superioara = -0.066
                elif zona == "P":
                    abaterea_superioara = -0.12
                elif zona == "R":
                    abaterea_superioara = -0.26
                elif zona == "S":
                    abaterea_superioara = -0.58
                elif zona == "T":
                    abaterea_superioara = -0.84
                elif zona == "U":
                    abaterea_superioara = -1.3
            elif tip == "Arbore" and dimensiune <=1120:
                if zona == "d":
                    abaterea_superioara = -0.35
                elif zona == "e":
                    abaterea_superioara = -0.195
                elif zona == "f":
                    abaterea_superioara = -0.098
                elif zona == "g":
                    abaterea_superioara = -0.028
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.04
                elif zona == "n":
                    abaterea_inferioara = 0.066
                elif zona == "p":
                    abaterea_inferioara = 0.12
                elif zona == "r":
                    abaterea_inferioara = 0.25
                elif zona == "s":
                    abaterea_inferioara = 0.52
                elif zona == "t":
                    abaterea_inferioara = 0.78
                elif zona == "u":
                    abaterea_inferioara = 1.15
            elif tip == "Arbore" and dimensiune >1120:
                if zona == "d":
                    abaterea_superioara = -0.35
                elif zona == "e":
                    abaterea_superioara = -0.195
                elif zona == "f":
                    abaterea_superioara = -0.098
                elif zona == "g":
                    abaterea_superioara = -0.028
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.04
                elif zona == "n":
                    abaterea_inferioara = 0.066
                elif zona == "p":
                    abaterea_inferioara = 0.12
                elif zona == "r":
                    abaterea_inferioara = 0.26
                elif zona == "s":
                    abaterea_inferioara = 0.58
                elif zona == "t":
                    abaterea_inferioara = 0.84
                elif zona == "u":
                    abaterea_inferioara = 1.3
        elif dimensiune >1250 and dimensiune <=1600:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.015
            elif clasa == "2":
                toleranta_dimensionala = 0.021
            elif clasa == "3":
                toleranta_dimensionala = 0.029
            elif clasa == "4":
                toleranta_dimensionala = 0.039
            elif clasa == "5":
                toleranta_dimensionala = 0.055
            elif clasa == "6":
                toleranta_dimensionala = 0.078
            elif clasa == "7":
                toleranta_dimensionala = 0.125
            elif clasa == "8":
                toleranta_dimensionala = 0.195
            elif clasa == "9":
                toleranta_dimensionala = 0.31
            elif clasa == "10":
                toleranta_dimensionala = 0.5
            elif clasa == "11":
                toleranta_dimensionala = 0.78
            elif clasa == "12":
                toleranta_dimensionala = 1.25
            elif clasa == "13":
                toleranta_dimensionala = 1.95
            elif clasa == "14":
                toleranta_dimensionala = 3.1
            elif clasa == "15":
                toleranta_dimensionala = 5
            elif clasa == "16":
                toleranta_dimensionala = 7.8
            elif clasa == "17":
                toleranta_dimensionala = 12.5
            elif clasa == "18":
                toleranta_dimensionala = 19.5
            if tip == "Alezaj" and dimensiune <=1400:
                if zona == "D":
                    abaterea_inferioara = 0.39
                elif zona == "E":
                    abaterea_inferioara = 0.22
                elif zona == "F":
                    abaterea_inferioara = 0.11
                elif zona == "G":
                    abaterea_inferioara = 0.03
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.048
                elif zona == "N":
                    abaterea_superioara = -0.078
                elif zona == "P":
                    abaterea_superioara = -0.14
                elif zona == "R":
                    abaterea_superioara = -0.3
                elif zona == "S":
                    abaterea_superioara = -0.64
                elif zona == "T":
                    abaterea_superioara = -0.96
                elif zona == "U":
                    abaterea_superioara = -1.45
            elif tip == "Alezaj" and dimensiune >1400:
                if zona == "D":
                    abaterea_inferioara = 0.39
                elif zona == "E":
                    abaterea_inferioara = 0.22
                elif zona == "F":
                    abaterea_inferioara = 0.11
                elif zona == "G":
                    abaterea_inferioara = 0.03
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.048
                elif zona == "N":
                    abaterea_superioara = -0.078
                elif zona == "P":
                    abaterea_superioara = -0.14
                elif zona == "R":
                    abaterea_superioara = -0.33
                elif zona == "S":
                    abaterea_superioara = -0.72
                elif zona == "T":
                    abaterea_superioara = -1.05
                elif zona == "U":
                    abaterea_superioara = -1.6
            elif tip == "Arbore" and dimensiune <=1400:
                if zona == "d":
                    abaterea_superioara = -0.39
                elif zona == "e":
                    abaterea_superioara = -0.22
                elif zona == "f":
                    abaterea_superioara = -0.11
                elif zona == "g":
                    abaterea_superioara = -0.03
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.048
                elif zona == "n":
                    abaterea_inferioara = 0.078
                elif zona == "p":
                    abaterea_inferioara = 0.14
                elif zona == "r":
                    abaterea_inferioara = 0.3
                elif zona == "s":
                    abaterea_inferioara = 0.64
                elif zona == "t":
                    abaterea_inferioara = 0.96
                elif zona == "u":
                    abaterea_inferioara = 1.45
            elif tip == "Arbore" and dimensiune >1400:
                if zona == "d":
                    abaterea_superioara = -0.39
                elif zona == "e":
                    abaterea_superioara = -0.22
                elif zona == "f":
                    abaterea_superioara = -0.11
                elif zona == "g":
                    abaterea_superioara = -0.03
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.048
                elif zona == "n":
                    abaterea_inferioara = 0.078
                elif zona == "p":
                    abaterea_inferioara = 0.14
                elif zona == "r":
                    abaterea_inferioara = 0.33
                elif zona == "s":
                    abaterea_inferioara = 0.72
                elif zona == "t":
                    abaterea_inferioara = 1.05
                elif zona == "u":
                    abaterea_inferioara = 1.6
        elif dimensiune >1600 and dimensiune <=2000:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.018
            elif clasa == "2":
                toleranta_dimensionala = 0.025
            elif clasa == "3":
                toleranta_dimensionala = 0.035
            elif clasa == "4":
                toleranta_dimensionala = 0.046
            elif clasa == "5":
                toleranta_dimensionala = 0.065
            elif clasa == "6":
                toleranta_dimensionala = 0.092
            elif clasa == "7":
                toleranta_dimensionala = 0.15
            elif clasa == "8":
                toleranta_dimensionala = 0.23
            elif clasa == "9":
                toleranta_dimensionala = 0.37
            elif clasa == "10":
                toleranta_dimensionala = 0.6
            elif clasa == "11":
                toleranta_dimensionala = 0.92
            elif clasa == "12":
                toleranta_dimensionala = 1.5
            elif clasa == "13":
                toleranta_dimensionala = 2.3
            elif clasa == "14":
                toleranta_dimensionala = 3.7
            elif clasa == "15":
                toleranta_dimensionala = 6
            elif clasa == "16":
                toleranta_dimensionala = 9.2
            elif clasa == "17":
                toleranta_dimensionala = 15
            elif clasa == "18":
                toleranta_dimensionala = 23
            if tip == "Alezaj" and dimensiune <=1800:
                if zona == "D":
                    abaterea_inferioara = 0.43
                elif zona == "E":
                    abaterea_inferioara = 0.24
                elif zona == "F":
                    abaterea_inferioara = 0.12
                elif zona == "G":
                    abaterea_inferioara = 0.032
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.058
                elif zona == "N":
                    abaterea_superioara = -0.092
                elif zona == "P":
                    abaterea_superioara = -0.17
                elif zona == "R":
                    abaterea_superioara = -0.37
                elif zona == "S":
                    abaterea_superioara = -0.82
                elif zona == "T":
                    abaterea_superioara = -1.2
                elif zona == "U":
                    abaterea_superioara = -1.85
            elif tip == "Alezaj" and dimensiune >1800:
                if zona == "D":
                    abaterea_inferioara = 0.43
                elif zona == "E":
                    abaterea_inferioara = 0.24
                elif zona == "F":
                    abaterea_inferioara = 0.12
                elif zona == "G":
                    abaterea_inferioara = 0.032
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.058
                elif zona == "N":
                    abaterea_superioara = -0.092
                elif zona == "P":
                    abaterea_superioara = -0.17
                elif zona == "R":
                    abaterea_superioara = -0.4
                elif zona == "S":
                    abaterea_superioara = -0.92
                elif zona == "T":
                    abaterea_superioara = -1.35
                elif zona == "U":
                    abaterea_superioara = -2
            elif tip == "Arbore" and dimensiune <=1800:
                if zona == "d":
                    abaterea_superioara = -0.43
                elif zona == "e":
                    abaterea_superioara = -0.24
                elif zona == "f":
                    abaterea_superioara = -0.12
                elif zona == "g":
                    abaterea_superioara = -0.032
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.058
                elif zona == "n":
                    abaterea_inferioara = 0.092
                elif zona == "p":
                    abaterea_inferioara = 0.17
                elif zona == "r":
                    abaterea_inferioara = 0.37
                elif zona == "s":
                    abaterea_inferioara = 0.82
                elif zona == "t":
                    abaterea_inferioara = 1.2
                elif zona == "u":
                    abaterea_inferioara = 1.85
            elif tip == "Arbore" and dimensiune >1800:
                if zona == "d":
                    abaterea_superioara = -0.43
                elif zona == "e":
                    abaterea_superioara = -0.24
                elif zona == "f":
                    abaterea_superioara = -0.12
                elif zona == "g":
                    abaterea_superioara = -0.032
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.058
                elif zona == "n":
                    abaterea_inferioara = 0.092
                elif zona == "p":
                    abaterea_inferioara = 0.17
                elif zona == "r":
                    abaterea_inferioara = 0.4
                elif zona == "s":
                    abaterea_inferioara = 0.92
                elif zona == "t":
                    abaterea_inferioara = 1.35
                elif zona == "u":
                    abaterea_inferioara = 2
        elif dimensiune >2000 and dimensiune <=2500:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.022
            elif clasa == "2":
                toleranta_dimensionala = 0.03
            elif clasa == "3":
                toleranta_dimensionala = 0.041
            elif clasa == "4":
                toleranta_dimensionala = 0.055
            elif clasa == "5":
                toleranta_dimensionala = 0.078
            elif clasa == "6":
                toleranta_dimensionala = 0.11
            elif clasa == "7":
                toleranta_dimensionala = 0.175
            elif clasa == "8":
                toleranta_dimensionala = 0.28
            elif clasa == "9":
                toleranta_dimensionala = 0.44
            elif clasa == "10":
                toleranta_dimensionala = 0.7
            elif clasa == "11":
                toleranta_dimensionala = 1.1
            elif clasa == "12":
                toleranta_dimensionala = 1.75
            elif clasa == "13":
                toleranta_dimensionala = 2.8
            elif clasa == "14":
                toleranta_dimensionala = 4.4
            elif clasa == "15":
                toleranta_dimensionala = 7
            elif clasa == "16":
                toleranta_dimensionala = 11
            elif clasa == "17":
                toleranta_dimensionala = 17.5
            elif clasa == "18":
                toleranta_dimensionala = 28
            if tip == "Alezaj" and dimensiune <=2240:
                if zona == "D":
                    abaterea_inferioara = 0.48
                elif zona == "E":
                    abaterea_inferioara = 0.26
                elif zona == "F":
                    abaterea_inferioara = 0.13
                elif zona == "G":
                    abaterea_inferioara = 0.034
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.068
                elif zona == "N":
                    abaterea_superioara = -0.11
                elif zona == "P":
                    abaterea_superioara = -0.195
                elif zona == "R":
                    abaterea_superioara = -0.44
                elif zona == "S":
                    abaterea_superioara = -1
                elif zona == "T":
                    abaterea_superioara = -1.5
                elif zona == "U":
                    abaterea_superioara = -2.3
            elif tip == "Alezaj" and dimensiune >2240:
                if zona == "D":
                    abaterea_inferioara = 0.48
                elif zona == "E":
                    abaterea_inferioara = 0.26
                elif zona == "F":
                    abaterea_inferioara = 0.13
                elif zona == "G":
                    abaterea_inferioara = 0.034
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.068
                elif zona == "N":
                    abaterea_superioara = -0.11
                elif zona == "P":
                    abaterea_superioara = -0.195
                elif zona == "R":
                    abaterea_superioara = -0.46
                elif zona == "S":
                    abaterea_superioara = -1.1
                elif zona == "T":
                    abaterea_superioara = -1.65
                elif zona == "U":
                    abaterea_superioara = -2.5
            elif tip == "Arbore" and dimensiune <=2240:
                if zona == "d":
                    abaterea_superioara = -0.48
                elif zona == "e":
                    abaterea_superioara = -0.26
                elif zona == "f":
                    abaterea_superioara = -0.13
                elif zona == "g":
                    abaterea_superioara = -0.034
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.068
                elif zona == "n":
                    abaterea_inferioara = 0.11
                elif zona == "p":
                    abaterea_inferioara = 0.195
                elif zona == "r":
                    abaterea_inferioara = 0.44
                elif zona == "s":
                    abaterea_inferioara = 1
                elif zona == "t":
                    abaterea_inferioara = 1.5
                elif zona == "u":
                    abaterea_inferioara = 2.3
            elif tip == "Arbore" and dimensiune >2240:
                if zona == "d":
                    abaterea_superioara = -0.48
                elif zona == "e":
                    abaterea_superioara = -0.26
                elif zona == "f":
                    abaterea_superioara = -0.13
                elif zona == "g":
                    abaterea_superioara = -0.034
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.068
                elif zona == "n":
                    abaterea_inferioara = 0.11
                elif zona == "p":
                    abaterea_inferioara = 0.195
                elif zona == "r":
                    abaterea_inferioara = 0.46
                elif zona == "s":
                    abaterea_inferioara = 1.1
                elif zona == "t":
                    abaterea_inferioara = 1.65
                elif zona == "u":
                    abaterea_inferioara = 2.5
        elif dimensiune >2500 and dimensiune <=3150:
            if clasa == "01":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "0":
                toleranta_dimensionala = float("NaN")
                casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                        "Pentru dimensiunile mai mari de 500 mm, nu sunt definite toleranțe pentru treptele IT01, respectiv IT0!")
                return
            elif clasa == "1":
                toleranta_dimensionala = 0.026
            elif clasa == "2":
                toleranta_dimensionala = 0.036
            elif clasa == "3":
                toleranta_dimensionala = 0.05
            elif clasa == "4":
                toleranta_dimensionala = 0.068
            elif clasa == "5":
                toleranta_dimensionala = 0.096
            elif clasa == "6":
                toleranta_dimensionala = 0.135
            elif clasa == "7":
                toleranta_dimensionala = 0.21
            elif clasa == "8":
                toleranta_dimensionala = 0.33
            elif clasa == "9":
                toleranta_dimensionala = 0.54
            elif clasa == "10":
                toleranta_dimensionala = 0.86
            elif clasa == "11":
                toleranta_dimensionala = 1.35
            elif clasa == "12":
                toleranta_dimensionala = 2.1
            elif clasa == "13":
                toleranta_dimensionala = 3.3
            elif clasa == "14":
                toleranta_dimensionala = 5.4
            elif clasa == "15":
                toleranta_dimensionala = 8.6
            elif clasa == "16":
                toleranta_dimensionala = 13.5
            elif clasa == "17":
                toleranta_dimensionala = 21
            elif clasa == "18":
                toleranta_dimensionala = 33
            if tip == "Alezaj" and dimensiune <=2800:
                if zona == "D":
                    abaterea_inferioara = 0.52
                elif zona == "E":
                    abaterea_inferioara = 0.29
                elif zona == "F":
                    abaterea_inferioara = 0.145
                elif zona == "G":
                    abaterea_inferioara = 0.038
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.076
                elif zona == "N":
                    abaterea_superioara = -0.135
                elif zona == "P":
                    abaterea_superioara = -0.24
                elif zona == "R":
                    abaterea_superioara = -0.55
                elif zona == "S":
                    abaterea_superioara = -1.25
                elif zona == "T":
                    abaterea_superioara = -1.9
                elif zona == "U":
                    abaterea_superioara = -2.9
            elif tip == "Alezaj" and dimensiune >2800:
                if zona == "D":
                    abaterea_inferioara = 0.52
                elif zona == "E":
                    abaterea_inferioara = 0.29
                elif zona == "F":
                    abaterea_inferioara = 0.145
                elif zona == "G":
                    abaterea_inferioara = 0.038
                elif zona == "H":
                    abaterea_inferioara = 0
                elif zona == "JS":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "K":
                    if int(clasa) <=8:
                        abaterea_superioara = 0
                elif zona == "M":
                    abaterea_superioara = -0.076
                elif zona == "N":
                    abaterea_superioara = -0.135
                elif zona == "P":
                    abaterea_superioara = -0.24
                elif zona == "R":
                    abaterea_superioara = -0.58
                elif zona == "S":
                    abaterea_superioara = -1.4
                elif zona == "T":
                    abaterea_superioara = -2.1
                elif zona == "U":
                    abaterea_superioara = -3.2
            elif tip == "Arbore" and dimensiune <=2800:
                if zona == "d":
                    abaterea_superioara = -0.52
                elif zona == "e":
                    abaterea_superioara = -0.29
                elif zona == "f":
                    abaterea_superioara = -0.145
                elif zona == "g":
                    abaterea_superioara = -0.038
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.076
                elif zona == "n":
                    abaterea_inferioara = 0.135
                elif zona == "p":
                    abaterea_inferioara = 0.24
                elif zona == "r":
                    abaterea_inferioara = 0.55
                elif zona == "s":
                    abaterea_inferioara = 1.25
                elif zona == "t":
                    abaterea_inferioara = 1.9
                elif zona == "u":
                    abaterea_inferioara = 2.9
            elif tip == "Arbore" and dimensiune >2800:
                if zona == "d":
                    abaterea_superioara = -0.52
                elif zona == "e":
                    abaterea_superioara = -0.29
                elif zona == "f":
                    abaterea_superioara = -0.145
                elif zona == "g":
                    abaterea_superioara = -0.038
                elif zona == "h":
                    abaterea_superioara = 0
                elif zona == "js":
                    abaterea_superioara = toleranta_dimensionala/2
                    abaterea_inferioara = -toleranta_dimensionala/2
                elif zona == "k":
                        abaterea_inferioara = 0
                elif zona == "m":
                    abaterea_inferioara = 0.076
                elif zona == "n":
                    abaterea_inferioara = 0.135
                elif zona == "p":
                    abaterea_inferioara = 0.24
                elif zona == "r":
                    abaterea_inferioara = 0.58
                elif zona == "s":
                    abaterea_inferioara = 1.4
                elif zona == "t":
                    abaterea_inferioara = 2.1
                elif zona == "u":
                    abaterea_inferioara = 3.2
        
        toldim_dinGUI.config(state="normal")
        toldim_dinGUI.delete(0, 'end')
        toldim_dinGUI.insert(0, toleranta_dimensionala)
        toldim_dinGUI.config(state="readonly")
        
        if not math.isnan(abaterea_superioara) and math.isnan(abaterea_inferioara):
            abaterea_inferioara = abaterea_superioara - toleranta_dimensionala
        elif not math.isnan(abaterea_inferioara) and math.isnan(abaterea_superioara):
            abaterea_superioara = abaterea_inferioara + toleranta_dimensionala

        abatereinf_dinGUI.config(state="normal")
        abatereinf_dinGUI.delete(0, 'end')
        abatereinf_dinGUI.insert(0, round(abaterea_inferioara, 6))
        abatereinf_dinGUI.config(state="readonly")

        abateresup_dinGUI.config(state="normal")
        abateresup_dinGUI.delete(0, 'end')
        abateresup_dinGUI.insert(0, round(abaterea_superioara, 6))
        abateresup_dinGUI.config(state="readonly")

        print(f"TD: {toleranta_dimensionala}, AS: {abaterea_superioara}, AI: {abaterea_inferioara}\n")

    except ValueError:
        casuta_dialog.showerror("Atenție! S-a produs o eroare în introducerea datelor!",
                                "Verificați ca toate câmpurile să conțină valori valide!")

# Crearea ferestrei principale
fereastra_GUI = interfata.Tk()
fereastra_GUI.title("Calculator toleranța dimensională și abateri limită")
fereastra_GUI.geometry("455x225")
continut_fereastra = tema_interfata.Frame(fereastra_GUI, padding="20")
continut_fereastra.grid(row=0, column=0, sticky=(interfata.W, interfata.E, interfata.N, interfata.S))

# Etichete și câmpuri pentru introducerea valorilor a parametrilor
tema_interfata.Label(continut_fereastra, text="Dimensiune nominală [mm]", anchor="center").grid(row=0, column=0, sticky=interfata.W, padx=5)
dnom_dinGUI = interfata.Entry(continut_fereastra, width=6)
dnom_dinGUI.grid(row=0, column=1, sticky=interfata.W)
dnom_dinGUI.insert(0, "10")

tema_interfata.Label(continut_fereastra, text="Tip dimensiune", anchor="e").grid(row=0, column=2, sticky=interfata.E, ipadx=20, padx=5)
tip_dinGUI = interfata.Listbox(continut_fereastra, width=7, height=2)
tip_dinGUI.grid(row=0, column=3, sticky=interfata.W)
tip_dinGUI.insert(1, "Arbore")
tip_dinGUI.insert(2, "Alezaj")
tip_ales = interfata.StringVar()

tema_interfata.Label(continut_fereastra, text="Poziția clasei de toleranță", anchor="s").grid(row=1, column=0, sticky=interfata.W+interfata.E)
zona_dinGUI = tema_interfata.Combobox(continut_fereastra, width=6)
zona_dinGUI.grid(row=2, column=0, sticky=interfata.N)
tip_dinGUI.bind("<<ListboxSelect>>", update_zona_toleranta)

tema_interfata.Label(continut_fereastra, text="Treapta de toleranță (IT)", anchor="n").grid(row=3, column=0, sticky=interfata.W+interfata.E)
clasa_dinGUI = tema_interfata.Combobox(continut_fereastra, width=6)
clasa_dinGUI.grid(row=4, column=0, sticky=interfata.N, pady=(0, 20))
clasa_dinGUI['values'] = ("01", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18")

buton_calculeaza = tema_interfata.Button(continut_fereastra, text="Calculează valorile!", command=calculare, width=25, padding=15)
buton_calculeaza.grid(row=5, column=0, columnspan=2)

buton_reset = tema_interfata.Button(continut_fereastra, text="RESET", command=reset, width=10, padding=0)
buton_reset.grid(row=5, column=2, columnspan=2, sticky=interfata.S)

tema_interfata.Label(continut_fereastra, text="Toleranța dimensională [mm]", anchor="center").grid(row=2, column=2, sticky=interfata.N+interfata.E)
toldim_dinGUI = interfata.Entry(continut_fereastra, width=8, state="normal", border=3)
toldim_dinGUI.grid(row=2, column=3, sticky=interfata.E)
toldim_dinGUI.config(state="readonly")

tema_interfata.Label(continut_fereastra, text="Abaterea superioară [mm]", anchor="center").grid(row=4, column=2, sticky=interfata.N+interfata.E, padx=(22, 0))
abateresup_dinGUI = interfata.Entry(continut_fereastra, width=8, state="normal", border=2)
abateresup_dinGUI.grid(row=4, column=3, sticky=interfata.N)
abateresup_dinGUI.config(state="readonly")

tema_interfata.Label(continut_fereastra, text="Abaterea inferioară [mm]", anchor="center").grid(row=5, column=2, sticky=interfata.N+interfata.E, padx=(26, 0))
abatereinf_dinGUI = interfata.Entry(continut_fereastra, width=8, state="normal", border=2)
abatereinf_dinGUI.grid(row=5, column=3, sticky=interfata.N)
abatereinf_dinGUI.config(state="readonly")

fereastra_GUI.columnconfigure(0, weight=1)
fereastra_GUI.rowconfigure(0, weight=1)

fereastra_GUI.mainloop()