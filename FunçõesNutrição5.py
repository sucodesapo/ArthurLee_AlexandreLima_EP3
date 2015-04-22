# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:53:46 2015

@author: Arthur
"""

from datetime import * 
import matplotlib.pyplot as plt
import doctest
# cálculo do IMC
def cálculoIMC(peso,altura):
  
    imc = float(peso / (altura ** 2))
    if imc < 17:
        return (imc,"Muito abaixo do peso")
    elif imc >= 17 and imc < 18.5:
        return(imc,"Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        return(imc,"Peso normal")
    elif imc >= 25 and imc < 30:
        return(imc,"Acima do peso")
    elif imc >= 30 and imc < 35:
        return(imc,"Obesidade I")
    elif imc >= 35 and imc < 40:
        return(imc,"Obesidade II\(severa)")
    else:
        return(imc,"Obesidade III\(mórbida)")
    """Calcula o IMC.
    >>> cálculoIMC(60,1.8)
    (18.5851851851852,"Peso normal")
    """
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
    """Calcula TMB, note que a altura é em cm.
    >>> cálculoTMB("M",25,178,72)
    1765
    """

def cálculoNC(TMB,fator):
    """Cálculo ne nesseciadades calóricas.
    >>> cálculoNC(1765,"médio")
    2735.75
    """
    NC = {"mínimo" : TMB * 1.2 ,
          "baixo" : TMB * 1.375 ,
          "médio" : TMB * 1.55 ,
          "alto" : TMB * 1.725 ,
          "muito alto" : TMB * 1.9}
    return NC[fator]
#------------------------------------------------------------------------------
# cálculo dos nutrientes consumidos por dia:
def cálculonutrientes(dic,dados):
    """Teste de verificação da função cálculonutrientes, que calcula os nutrientes consumidos por alimento.
    >>> dic = {"ABACATE":[100,177.00,1.80,6.40,16.00]}
    >>> dados =[["06/04/2015","ABACATE",40]]
    >>> cálculonutrientes(dic,dados)
    [{'06/04/2015': 70.8}, {'06/04/2015': 0.7200000000000001}, {'06/04/2015': 2.56}, {'06/04/2015': 6.4}]
    """
    diccalorias = {}
    dicproteínas = {}
    diccarboidratos = {}
    dicgorduras = {}
        
    for item in dados:
        data = item[0]
        alimento = item[1]
        qtd = item[2]
        
        calorias = 0
        proteínas = 0
        carboidratos = 0
        gorduras = 0 

        if alimento in dic:      # aqui se acessará os dados nutricionais dos alimentos, se ele estiver no arquivo
            cal_per_g = float(dic[alimento][1]) / float(dic[alimento][0])
            calorias = float(cal_per_g * int(qtd))
            
            prot_per_g = float(dic[alimento][2]) / float(dic[alimento][0])
            proteínas = float(prot_per_g * int(qtd))
            
            carb_per_g = float(dic[alimento][3]) / float(dic[alimento][0])
            carboidratos = float(carb_per_g * int(qtd))
            
            gord_per_g = float(dic[alimento][4]) / float(dic[alimento][0])
            gorduras = float(gord_per_g * int(qtd))
   
        if data in diccalorias:     # se no dicionário já se tiver a data, irá se adicionar ao valor dela o os nutrientes calculados para aquele dia
            diccalorias[data] += calorias
        if data in dicproteínas:
            dicproteínas[data] += proteínas
        if data in diccarboidratos:
            diccarboidratos[data] += carboidratos
        if data in dicgorduras:
            dicgorduras[data] += gorduras
        else:     # se não tiver a data no dicionário, criará-se uma nova chave no dicionário com valor inicial zero
            diccalorias[data] = calorias
            dicproteínas[data] = proteínas
            diccarboidratos[data] = carboidratos
            dicgorduras[data] = gorduras
    lista = [diccalorias,dicproteínas,diccarboidratos,dicgorduras]
    return lista
#------------------------------------------------------------------------------
# cálculo de kcal por dia:
def mediakcal(calorias,sqdias):
    """Calcula a média de calorias ingeridos no tempo total da dieta.
    >>> calorias = [500,1000]
    >>> sqdias = [0,1,2]
    >>> mediakcal(calorias,sqdias)
    500.0
    """
    total = 0
    for i in range(len(calorias)):
        total += calorias[i]
    return total / int((sqdias[-1] +1))
#------------------------------------------------------------------------------
# sqdias é o delta de cada dia tomando como referência o primeiro dia da dieta(deltas)
def sqdias(n):
    """Calcula o delta dias a partir do primeiro dia da dieta(dia 0)
    >>> n =[{"06/04/2015":0,"07/04/2015":0}]
    >>> sqdias(n)
    [0, 1]
    """
    datas = list(n[0].keys())
    dias = []
    sqdias = []
    for i in datas:
        date = datetime.strptime(i,"%d/%m/%Y")# a partir daqui será calculado os dias que a pessoa seguiu a dieta
        dias.append(date)
    sdias = sorted(dias)
    prim_dia = sdias[0]
    sqdias = []
    for d in sdias:
        delta = d - prim_dia
        sqdias.append(delta.days)
    return sqdias
#-----------------------------------------------------------------------------------
# plotar o gráfico com os valores de proteínas, carb,calorias e etc:

def gráfico(NC,n,sqdias):
    calorias = list(n[0].values())    # aqui serão criadas as lista com os valores de nutrientes consumidos cada dia
    proteínas = list(n[1].values())
    carboidratos = list(n[2].values())
    gorduras = list(n[3].values())
    cal_recomendadas = [NC] * len(sqdias) 
    
    f,axarr = plt.subplots(5, sharex = True) #plotação de gráficos
    axarr[0].plot(sqdias,calorias,'r')
    axarr[0].set_title("calorias")
    axarr[0].set_ylabel("kcal")
    axarr[1].plot(sqdias,cal_recomendadas,'r')
    axarr[1].set_title("calorias recomendadas")
    axarr[1].set_ylabel("kcal")
    axarr[2].plot(sqdias,proteínas,'g')
    axarr[2].set_title("proteínas")
    axarr[2].set_ylabel("gramas")
    axarr[3].plot(sqdias,carboidratos,'b')
    axarr[3].set_title("carboidratos")
    axarr[3].set_ylabel("gramas")
    axarr[4].plot(sqdias,gorduras,'y')
    axarr[4].set_title("gorduras")
    axarr[4].set_ylabel("gramas")
    plt.show()
    return None
if __name__=="__main__":
    doctest.testmod(verbose="True")