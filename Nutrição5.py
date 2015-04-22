# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:30:52 2015

@author: Arthur
"""
#import datetime
from FunçõesNutrição4 import *
     
file = open("alimentos.csv")    #Abrir a lista com as palavras
lista = file.readlines()
#dados = lista[1].strip().split(",")
#-------------------------------------------------------------------------------
# dicionários com dados dos alimentos:

lista2 = []
for i in range(1,len(lista)):
   a = lista[i].strip().split(",")
   lista2.append(a)

dic = {}
for i in lista2:
    dic[i[0]] = i[1:]
#print(dic)
    
#------------------------------------------------------------------------------
# acesso à lista com dados do usuário:
file2 = open("usuario.csv")
lista2 = file2.readlines()
b = lista2[1].strip().split(",")

nome = b[0]
idade = int(b[1])
peso = float(b[2])
sexo = b[3]
altura = float(b[4])
fator = b[5]

dados = []
for i in range(lista2.index(lista2[3]),len(lista2)):
    c = lista2[i].strip().split(",")
    while '' in c:    
        c.remove('')
    dados.append(c)
#print(dados)

#------------------------------------------------------------------------------
# cálculo de calorias, gord,carb e prot totais por dia:
n = cálculonutrientes(dic,dados)
#print(n)        
#------------------------------------------------------------------------------
# cálculo de IMC:
IMC = cálculoIMC(peso,altura)
#print ("De acordo com o IMC, você ou a pessoa está %s! " % IMC)
#-----------------------------------------------------------------------------
# cálculo TMB, metabolismo basal:
TMB = cálculoTMB(sexo,idade,altura,peso)
#print ("O Tmetabolismo basal é cerca de %5.2f kcal" % TMB)
#------------------------------------------------------------------------------
# cáçculo NC, necessidade calórica :
NC = cálculoNC(TMB,fator)
#print ("A necessidade calórica é cerca de %5.2f kcal" % NC)


#------------------------------------------------------------------------------
# data - calorias - proteínas -carboidratos - gorduras - calorias recomendadas
# colocar os valores dos dicionários em variadas listas:
calorias = n[0]
calorias2 = list(calorias.values())
print (calorias2)
proteínas = n[1]
proteínas2 = list(proteínas.values())

carboidratos = n[2]
carboidratos2 = list(carboidratos.values())

gorduras = n[3]
gorduras2= list(gorduras.values())

cal_recomendadas = [NC] * 2
#print(cal_recomendadas)
#------------------------------------------------------------------------------
datas = list(n[0].keys())
from datetime import * 
dias = []

for i in datas:
    date = datetime.strptime(i,"%d/%m/%Y")
    dias.append(date)
    
#print(dias)    

sdias = sorted(dias)

prim_dia = sdias[0]
sqdias = []
for d in sdias:
    delta = d - prim_dia
    sqdias.append(delta.days)
#print(sqdias)
    
#------------------------------------------------------------------------------    
# gráfico
import matplotlib.pyplot as plt

f,axarr = plt.subplots(5, sharex = True)
axarr[0].plot(sqdias,calorias2,'r')
axarr[0].set_title("calorias")
axarr[0].set_ylabel("kcal")
axarr[1].plot(sqdias,cal_recomendadas,'y')
axarr[1].set_title("calorias recomendadas")
axarr[1].set_ylabel("gramas")
axarr[2].plot(sqdias,proteínas2,'g')
axarr[2].set_title("proteínas")
axarr[2].set_ylabel("gramas")
axarr[3].plot(sqdias,carboidratos2,'b')
axarr[3].set_title("carboidratos")
axarr[3].set_ylabel("gramas")
axarr[4].plot(sqdias,gorduras2,'y')
axarr[4].set_title("gorduras")
axarr[4].set_ylabel("gramas")

plt.show()














