# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:33:59 2015

@author: Arthur
"""
import csv
"""
import csv
with open('alimentos.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
"""
     
file = open("alimentos.csv")    #Abrir a lista com as palavras
lista = csv.reader(file)
print(lista)

for row in lista:
    print (row)

# cálculo do IMC
def cálculoIMC(peso,altura):
    imc = float(peso / (altura ** 2))
    if imc < 17:
        print ("Muito abaixo do peso")
    elif imc >= 17 and imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso normal")
    elif imc >= 25 and imc < 30:
        print("Acima do peso")
    elif imc >= 30 and imc < 35:
        print("Obesidade I")
    elif imc >= 35 and imc < 40:
        print("Obesidade II\(severa)")
    else:
        print("Obesidade III\(mórbida)")


#cálculoIMC(60,1.8)    
#------------------------------------------------------------------------------------   
"""
import csv
with open('alimentos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["ABACATE"], row["YAKULT"])

import csv
with open('alimentos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
    for row in spamreader:
        print(', '.join(row))
"""
#csv.QUOTE_ALL
#csv.DictReader

#csv.DictReader("alimentos.csv", fieldnames=None, restkey=None, restval=None, dialect='excel')








