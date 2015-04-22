# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:48:18 2015

@author: Arthur
"""


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
dic2 = {}
for item in dados:
    
    data = item[0]
    alimento = item[1]
    qtd = item[2]
    cal_consumidas = 0
    prot_consumidas = 0
    carb_consumidas = 0
    gord_consumidas = 0

    if alimento in dic:
        cal_per_g = float(dic[alimento][1]) / float(dic[alimento][0])
        cal_consumidas = cal_per_g * int(qtd)
        
        prot_per_g = float(dic[alimento][2]) / float(dic[alimento][0])
        prot_consumidas = prot_per_g * int(qtd)
        
        carb_per_g = float(dic[alimento][3]) / float(dic[alimento][0])
        carb_consumidas = carb_per_g * int(qtd)
        
        gord_per_g = float(dic[alimento][4]) / float(dic[alimento][0])
        gord_consumidas = gord_per_g * int(qtd)
        
    lista3 = [cal_consumidas, prot_consumidas, carb_consumidas, gord_consumidas]
   
    if data in dic2:
        for i in range(4):
            dic2[data][i] += lista3[i]
        
    else:
        dic2[data] = lista3
print(dic2)
        
#------------------------------------------------------------------------------
# cálculo de gordura:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
