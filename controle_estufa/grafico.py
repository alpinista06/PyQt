import matplotlib.pyplot as plt
import numpy as np
import time
import serial #importacao do modulo serial
import random


leitura =[]
fig, ax = plt.subplots()
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #abre porta serial ACM0

i=0
contador = 0
eixo_x = 60
while (i<60):
    '''
    while (ser.inWaiting()==0):
     pass
    dados  =int( ser.readline()[:-1])    #firmware deve ter um delay de pelo menos 100ms entre cada envio
    '''
    dados = random.randint(59,69)
    print dados
    ax.clear()
    plt.title('Grafico do nivel de humidade do solo')
    ax.set_xlim([0,eixo_x])   #faixa do eixo horizontal
    plt.xlabel('Tempo')
    ax.set_ylim([10,100]) # faixa do eixo vertical
    plt.ylabel('Nivel de humidade')
    leitura.append(dados)


    ax.plot(leitura)
    plt.pause(1)
    fig.savefig('plotter.png')
    contador = contador + 1
    if (contador > eixo_x):
	   leitura.pop(0)
    i=i+1

#ser.close()
