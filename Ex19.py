#PCS3578 - Sistemas Tolerantes a Falhas (2023)
#Nome 1: Isaac Yusuke Yanagui
#NUSP 1: 10772369
#Nome 2:
#NUSP 2:

import numpy as np
import matplotlib.pyplot as plt

"""
MTTF = 100h
MTTRc = 10h
MTTRp = 1 mês
"""

#Transforma tudo em horas
MTTF = 100        #tempo medio ate falhar
MTTRc = 10        #tempo medio ate reparo corretivo
MTTRp = 1*30*24   #tempo medio ate reparo preventivo

l = 1/MTTF     #lambda = taxa de falha
mic = 1/MTTRc  #mic = taxa de reparo corretivo
mip = 1/MTTRp  #mip = taxa de reparo preventivo
C = 0.7   #0.7 ou 1   #fator de cobertura (chance da falha ser detectada)
deltat = 1e-3   #testa valores pequenos????
N = 20000   # número de iterações

A = np.array([
    [1 - 2*l*deltat, 2*l*C*deltat              , l*(1-C)*deltat          , l*(1-C)*deltat],  #1 - ambos os modulos funcionando
    [mic*deltat    , 1 - l*deltat - mic*deltat , 0                       , l*deltat],        #2 - 1 funcionando e 1 teve uma falha detectada
    [mip*deltat    , 0                         , 1-l*deltat - mip*deltat , l*deltat],        #3 - 1 funcionando e 1 teve uma falha não detectada
    [mic*deltat    , 0                         , 0                       , 1 - mic*deltat]   #F - sistema não está funcionando
])

P= np.array([
    [1],
    [0],
    [0],
    [0]
])

difList = []  #lista pra armazenar as diferenças    
for i in range(N):
    dif = np.max(np.abs(P - np.dot(A,P)))
    difList.append(dif)
    P = np.dot(A,P)
    P = P/np.sum(P)  # normaliza dentro do loop? parece que ficou melhor assim
    print(P)
    #A = np.dot(A,A)
    #print(np.dot(A,P))
#"""

print("Disponibilidade Assintótica = ", 1- P[3])

# Plotando o gráfico
plt.plot(list(range(N)), difList)
plt.xlabel('Iterações')
plt.ylabel('Máxima Diferença')
plt.title('Evolução da Diferença Máxima em Cada Iteração')
plt.show()