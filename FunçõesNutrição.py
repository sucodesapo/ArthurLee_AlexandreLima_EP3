# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:27:05 2015

@author: Arthur
"""

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

    NC = {"mínimo" : TMB * 1.2 ,
          "baixo" : TMB * 1.375 ,
          "médio" : TMB * 1.55 ,
          "alto" : TMB * 1.725 ,
          "muito alto" : TMB * 1.9}
    return NC[fator]
    
    
  

#print(cálculoNC(1000,"mínimo"))

