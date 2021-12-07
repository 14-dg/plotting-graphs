#29.11.2021
#Daniel Gräf 
#Ermittlung der Parameter a,b,c und d fuer die Funktion m(p)=a*p^b+c*p^d


#Anleitung/Vorbereitende Aufgaben:
# 1. Brennerkurven ablesen und in Tabellenkalkulation uebertragen (Leistung gegenueber HG-außentemperatur),
# 2. Leistung der Brennerkurven durch jeweiligen Heizwert der Heizgaszusammensetzung teilen
#    damit erhält man aus den Wertepaare, Leistung/außentemperatur die Wertepaare für Massenstrom und außentemperatur
# 3. Diese Wertepaare nach hier übertragen (ab Zeile 29)


#Pakete importieren
# from warnings import catch_warnings
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.arraypad import _round_if_needed
from scipy.optimize import curve_fit

# import warnings
# warnings.filterwarnings("ignore")

GROEßE_DER_FENSTER=100
NACHKOMMASTELLEN = 3


#Form der Funktion fuer die Naeherung, diese Funktion ist frei veränderbar, je nach BK-Form ggf. Anpassungen notwendig
def func(x, a, b, c, d):
    #print(np.sign(x) * a * np.power(abs(x),b) + np.sign(x) * c * np.power(abs(x),d))
    return np.sign(x) * a * abs(x)**b + np.sign(x) * c * abs(x)**d
    


#außentemperaturwerte (x-Werte)
außentemperatur = np.array([20, 15, 10, 5, 0, -5, -10, -15, -20])


#Massenstromwerte hier eintagen, aus BK ermittelt (s. Anleitung oben) (y-Werte für Graphik 1)
F1massenstrom = np.array([20, 30, 38, 44, 50, 55, 61, 67, 72])
F2massenstrom = np.array([20, 25, 30, 35, 38, 41, 45, 48, 50])
F3massenstrom = np.array([20, 25, 28, 30, 33, 36, 38, 40, 42])


#Ausfuehren der Curve Fit Funktion fuer alle Massenstroeme (y-Werte für Graphik 2)
F1parameter, pcov = curve_fit(func, außentemperatur, F1massenstrom)
F2parameter, pcov = curve_fit(func, außentemperatur, F2massenstrom)
F3parameter, pcov = curve_fit(func, außentemperatur, F3massenstrom)


#Ausgeben der Parameter
print("\nArrays fuer die Parameter der Form [a b c d]:")
print("Curve-Fit-Paramter fuer Massenstrom 1: ", round(float(F1parameter[0]), NACHKOMMASTELLEN), ",", round(float(F1parameter[1]), NACHKOMMASTELLEN), ",", round(float(F1parameter[2]), NACHKOMMASTELLEN), ",", round(float(F1parameter[3]), NACHKOMMASTELLEN))
print("Curve-Fit-Paramter fuer Massenstrom 2: ", round(float(F2parameter[0]), NACHKOMMASTELLEN), ",", round(float(F2parameter[1]), NACHKOMMASTELLEN), ",", round(float(F2parameter[2]), NACHKOMMASTELLEN), ",", round(float(F2parameter[3]), NACHKOMMASTELLEN))
print("Curve-Fit-Paramter fuer Massenstrom 3: ", round(float(F3parameter[0]), NACHKOMMASTELLEN), ",", round(float(F3parameter[1]), NACHKOMMASTELLEN), ",", round(float(F3parameter[2]), NACHKOMMASTELLEN), ",", round(float(F3parameter[3]), NACHKOMMASTELLEN))


#Ausgeben aller Massenstromkurven in Abhaengigkeit zum außentemperatur
plt.figure(1, dpi=GROEßE_DER_FENSTER)
plt.plot(außentemperatur, F1massenstrom, 'blue', label='F1 BK')
plt.plot(außentemperatur, F2massenstrom, 'green', label='F2 BK')
plt.plot(außentemperatur, F3massenstrom, 'red', label='F3 BK') 
 

plt.ylabel('Massenstrom in kg/h')
plt.xlabel('außentemperatur in celsius')
plt.title('Massenstrom aus Brennerkurven')
plt.legend(loc='best')
plt.axis([max(außentemperatur), min(außentemperatur), min(min(F1massenstrom), min(F2massenstrom), min(F3massenstrom)), max(max(F1massenstrom), max(F2massenstrom), max(F3massenstrom))])
plt.grid()
plt.show()

#Ausgeben aller gennaeherten Kurven fuer Massenstrom in Abhaengigkeit zum außentemperatur
#außentemperatur=np.array(list(map(lambda x : x-37, außentemperatur)))
y1 = func(außentemperatur, *F1parameter)
y2 = func(außentemperatur, *F2parameter)
y3 = func(außentemperatur, *F3parameter)



plt.figure(2, dpi=GROEßE_DER_FENSTER)
plt.plot(außentemperatur, y1, 'blue', label='F1')
plt.plot(außentemperatur, y2, 'green', label='F2')
plt.plot(außentemperatur, y3, 'red', label='F3') 


plt.ylabel('Massenstrom in kg/h')
plt.xlabel('außentemperatur in celsius')
plt.title('Massenstrom aus Formel')
plt.legend(loc='best')
#plt.axis([40, 0, 20, 60])
plt.axis([max(außentemperatur), min(außentemperatur), min(min(y1), min(y2), min(y3)), max(max(y1), max(y2), max(y3))])
plt.grid()
plt.show()


#Nachbereitung:
# 1. Ermittelte Parameter sortieren 
# 2. Mittelwerte von Parameter a, b, c und d bilden
# 3. Mittelwert von Dichte (Dichte_MW) aller Heinzgaszusammensetzungen bilden
# 4. Mittelwerte der Parameter und der Dichte in folgende Formel eintragen:
#         Q= (a * p^b + c * p^d) * Wurzel(Dichte_x/Dichte_MW) Heizwert_x           
#        (Q=Leistung, p=außentemperatur, Dichte_x und Heizwert_x Heizgasmesswerte aus dem Prozess)
# 5. Diese Formel für Leistungsberechnung verwenden (Leistungs-Istwert) und Leistungsregler vor außentemperaturregler schalten, 
#      damit dieser den außentemperatur-Sollwert abhaenigig von der Heizgaszusammensetzung vorgibt


#Ausfuehrlichere Erklaerungen siehe Bachelor_Thesis_Verena_Neuneier.pdf ab Seite 86 im PDF