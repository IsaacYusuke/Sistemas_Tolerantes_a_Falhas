#PCS3578 - Sistemas Tolerantes a Falhas (2023)
#Nome 1: Isaac Yusuke Yanagui
#NUSP 1: 10772369
#Nome 2:
#NUSP 2:

import numpy

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
C = 1   #0.7   #fator de cobertura (chance da falha ser detectada)
deltat = 1e-3   #testa valores pequenos????

A = [
    [1 - 2*l*deltat, 2*l*C*deltat              , l*(1-C)*deltat          , l*(1-C)*deltat],  #1 - ambos os modulos funcionando
    [mic*deltat    , 1 - l*deltat - mic*deltat , 0                       , l*deltat],        #2 - 1 funcionando e 1 teve uma falha detectada
    [mip*deltat    , 0                         , 1-l*deltat - mip*deltat , l*deltat],        #3 - 1 funcionando e 1 teve uma falha não detectada
    [mic*deltat    , 0                         , 0                       , 1 - mic*deltat]   #F - sistema não está funcionando
]

P= [
    [1],
    [0],
    [0],
    [0]
]

dif = P - numpy.dot(A,P)
difList = []
#print(sum(numpy.dot(A,P)))
#print(numpy.dot(A,P))
print(A)
#print(numpy.dot(A,A))
#"""
#while max(abs(dif)) > 1e-11:  #testar com outros valores
for i in range(100):
    dif = P - numpy.dot(A,P)
    diflist = difList + dif
    P = numpy.dot(A,P)
    print(P)
    #A = numpy.dot(A,A)
    #print(numpy.dot(A,P))
#"""
