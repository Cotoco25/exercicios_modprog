# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:08:12 2026

@author: PC-PROF
"""
#Ex Espaco vazio: cubo e esferas

import math

def calcVolEsfera(raio):
    vesf= (4*math.pi*raio**3)/3 
    return vesf 

def calcVolCubo(lado): 
    return lado**3 

def espaco_vazio (lado):
    vCubo= calcVolCubo(lado)
    vUmaEsf= calcVolEsfera(lado/4)
    espVazio= vCubo - 8* vUmaEsf
    return espVazio 
    
#BP
aresta= 80 #float(input('Entre lado:'))
vvazio= espaco_vazio(aresta)
print(f'Vol vazio:{vvazio:.3f}')
    


