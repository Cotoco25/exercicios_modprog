# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:06:10 2026

@author: PC-PROF
"""

# A) Escreva uma função que receba uma lista 
# e retorne a quantidade de elementos do 
# tipo string, em qualquer nivel da lista
# (considerando todos os niveis da lista)
def contaStringRec(ls):
    cont = 0
    for el in ls:
        if type(el) == str:
            cont+=1 
        elif type(el) == list:  
            qtdDaListinha = contaStringRec(el)
            cont+= qtdDaListinha 
    return cont


# B) Escreva uma função que receba uma lista e um valor X 
#   e retorne a quantidade de valores numericos maiores do que
#   x em qualquer nivel da lista
    
# C) Escreva uma função que receba uma lista e substitua 
#    toda string  pelo seu tamanho em qualquer nivel da lista
    
# D) Escreva uma função que receba uma lista 
#     e retorne a soma dos  valores numericos 
#     da lista, em qualquer nivel da lista

#BO
lz=[12,'au',[34,'uau',4,'ceu'],67,'eu',[[23,'mar'],'ze',['sol']],14]
print('\nLISTA:',lz)
qt= contaStringRec(lz)
print(f'Há {qt} strings na lista')