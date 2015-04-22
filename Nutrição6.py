# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:49:41 2015

@author: Arthur
"""
from FunçõesNutrição5 import *
from datetime import * 
import matplotlib.pyplot as plt
     
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
print(dados)
#------------------------------------------------------------------------------
# cálculo de calorias, gord,carb e prot totais por dia:
n = cálculonutrientes(dic,dados)
#print(n)        
#------------------------------------------------------------------------------
# cálculo de IMC:
IMC = cálculoIMC(peso,altura)
a = ("De acordo com o IMC %5.2f, você ou a pessoa está %s  " % IMC)
#-----------------------------------------------------------------------------
# cálculo TMB, metabolismo basal:
TMB = cálculoTMB(sexo,idade,altura,peso)
#print ("O Tmetabolismo basal é cerca de %5.2f kcal" % TMB)
#------------------------------------------------------------------------------
# cáçculo NC, necessidade calórica :
NC = cálculoNC(TMB,fator)
#print ("A necessidade calórica é cerca de %5.2f kcal" % NC)
#------------------------------------------------------------------------------
#calculo dis dias no gráfico e plotação do gráfico 
dias = sqdias(n)
print(gráfico(NC,n,dias))
#------------------------------------------------------------------------------
# é a média de calorias ingeridas por dia
calorias = list(n[0].values())
mediacalorias = mediakcal(calorias,dias) # essa variável é a média de calorias ingeridas por dia durante a dieta

#geração do arquivo texto com as informações requisitadas
saida = open("saida.txt","w")
saida.writelines(a + " e a média de calorias consumidas foi"+str(mediacalorias) + "kcal")
saida.close()















