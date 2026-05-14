# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:28:07 2026

@author: PC-PROF
"""

# A) Escreva uma função que receba uma lista 
# e exiba cada  elemento com sua respectiva 
# posição (usando while)
  
def exibe1(ls):
    print('\nLista:')
    tam = len(ls)
    ind=0
    while ind < tam:
        print(f'Posicao:{ind} - Elemento:ls[ind]')
        ind+=1 

# B) Escreva uma função que receba uma lista 
# e exiba cada  elemento da lista (for)
def exibe2(ls):
    print('\nLista:')
    for el in ls:
        print(el)

# C) Escreva uma função que receba uma lista 
# e exiba cada  elemento com sua respectiva 
# posição (usando for)
def exibe3(ls):
    print('\nLista:')
    for pos,elem in enumerate(ls):
        print(f'POS:{pos} - ELEM:{elem}')

# D)Escreva uma função que receba uma lista 
# de valores inteiros e SUBSTITUA todos os valores 
# pares pelo valor 666
def substituiElementosPares(ls):
    for ind,elem in enumerate(ls):
        if elem%2 == 0:
            ls[ind] = 666

# E)Escreva uma função que receba uma lista 
# de valores inteiros e SUBSTITUA todos os 
# elementos das posições pares pelo valor 0
def substituiNasPosicoesPares(ls):
    for ind in range(0,len(ls),2):
        ls[ind]=0 

# F)Escreva uma função que receba uma lista 
# e retorne a quantidade de elementos do 
# tipo string. (Considerando somente o
# primeiro nivel da lista)

#BP
la=[10,'oi',[5,4,3],23]
exibe3(la)
print('##############################')
lb= [13,44,22,97,60]
print('\nANTES:',lb)
substituiElementosPares(lb)
print('\nDEPOIS:',lb)
print('##############################')
print('\nANTES:',lb)
substituiNasPosicoesPares(lb)
print('\nDEPOIS:',lb)
print('##############################')


lz=[12,'au',[34,'uau',4,'ceu'],67,'eu',[[23,'mar'],'ze',['sol']],14]
