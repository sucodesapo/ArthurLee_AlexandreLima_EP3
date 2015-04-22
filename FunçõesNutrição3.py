# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:21:05 2015

@author: Arthur
"""

# cálculo do IMC
def cálculoIMC(peso,altura):
    imc = float(peso / (altura ** 2))
    if imc < 17:
        return ("Muito abaixo do peso")
    elif imc >= 17 and imc < 18.5:
        return("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        return("Peso normal")
    elif imc >= 25 and imc < 30:
        return("Acima do peso")
    elif imc >= 30 and imc < 35:
        return("Obesidade I")
    elif imc >= 35 and imc < 40:
        return("Obesidade II\(severa)")
    else:
        return("Obesidade III\(mórbida)")
#-----------------------------------------------------------------------------        
# cálculo Harris-Benedict
# peso(kg) / altura(cm)
def cálculoTMB(sexo,idade,altura,peso):
    if sexo == "M":
        TMB = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        return float(TMB)
    elif sexo == "F":
        TMB = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
        return float(TMB)

def cálculoNC(TMB,fator):

    NC = {"mínimo" : TMB * 1.2 ,
          "baixo" : TMB * 1.375 ,
          "médio" : TMB * 1.55 ,
          "alto" : TMB * 1.725 ,
          "muito alto" : TMB * 1.9}
    return NC[fator]
#print(cálculoNC(1000,"mínimo"))
#------------------------------------------------------------------------------
# cálculo das calorias:
def cálculonutrientes(dic,dados):
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
            cal_consumidas = float(cal_per_g * int(qtd))
            
            prot_per_g = float(dic[alimento][2]) / float(dic[alimento][0])
            prot_consumidas = float(prot_per_g * int(qtd))
            
            carb_per_g = float(dic[alimento][3]) / float(dic[alimento][0])
            carb_consumidas = float(carb_per_g * int(qtd))
            
            gord_per_g = float(dic[alimento][4]) / float(dic[alimento][0])
            gord_consumidas = float(gord_per_g * int(qtd))
            
        lista3 = [cal_consumidas, prot_consumidas, carb_consumidas, gord_consumidas]
       
        if data in dic2:
            for i in range(4):
                dic2[data][i] += lista3[i]
            
        else:
            dic2[data] = lista3
    return dic2

#------------------------------------------------------------------------------
# plotar o gráfico com os valores de proteínas, carb,calorias e etc:
"""
def gráfico(dic2,NC):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    
    nutrientes = ("calorias","calorias rec","proteínas","carboidratos","gorduras")
    y_pos = np.arange(len(nutrientes))
    for i in range(len(nutrientes)):
        
    error = np.arrange(len(nutrientes))
    
    plt.barh(y_pos, valores, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, nutrientes)
    plt.xlabel('Valores Nutricionais')
    plt.title('Nutrientes consumidos em ')
    
    plt.show()
    


# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()
"""