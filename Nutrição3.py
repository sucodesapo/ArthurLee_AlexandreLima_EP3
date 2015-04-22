# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:40:59 2015

@author: Arthur
"""
import csv
import datetime
     
file = open("alimentos.csv")    #Abrir a lista com as palavras
lista = file.readlines()
#dados = lista[1].strip().split(",")
#-------------------------------------------------------------------------------
# dicionários com dados dos alimentos:

lista2 = []
for i in range(1,len(lista)):
   a = lista[i].strip().split(",")
   lista2.append(a)
#print (lista2)
dic = {}
for i in lista2:
    dic[i[0]] = i[1:]
#print(dic)
    
#------------------------------------------------------------------------------
# acesso à lista com dados do usuário
file2 = open("usuario.csv")
lista2 = file2.readlines()

#print(lista2)

alimentos = []
data = []
quantidade = []

dados2 = lista2[1].strip().split(",")

#print(dados2)

nome = dados2[0]
idade = int(dados2[1])
peso = float(dados2[2])
sexo = dados2[3]
altura = float(dados2[4])
fator = dados2[5]



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

def cálculoNC(TMB,fator):
    NC = {"mínimo" : TMB * 1.2 ,"baixo" :TMB * 1.375 ,"médio" : TMB * 1.55 ,"alto" : TMB * 1.725 ,"muito alto" : TMB * 1.9}
    
    if fator == key in NC:
        print("Necessidades calóricas : %s" %  NC.get(key))
        


