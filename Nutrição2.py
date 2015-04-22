# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 07:40:32 2015

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
lista = file.readlines()

# criação de dicionários 
diccal = {}
dicprot = {}
diccarbo = {}
dicgord = {}
listadic = [diccal,dicprot,diccarbo,dicgord]

for i in range(1,len(lista)):
    elementos = str(lista[i])
    elementos = elementos.split(",")
    
    for j in (len(elementos) - 2):
        dic = listadic[j]
        dic[elementos[0]] = elementos[j+2]






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
        
# cálculo Harris-Benedict
# peso(kg) / altura(cm)
def cálculoTMB(sexo,idade,altura,peso):
    if sexo == "M":
        TMB = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        return TMB
    elif sexo == "F":
        TMB = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
        return TMB
"""
def cálculoNC(TMB,fator):
    NC = {"mínimo" = TMB * 1.2 ,"baixo" = TMB * 1.375 ,"médio" = TMB * 1.55 ,"alto" = TMB * 1.725 ,"muito alto" = TMB * 1.9}
    
    if fator == key in NC:
        print("Necessidades calóricas : %s" %  NC.get(key))
        
"""


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








