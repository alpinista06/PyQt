'''
Graphic plotter

Aplicativo desenvolvido para desktop com PyQt5 que tem por
finalidade plotar graficamente informações com a biblioteca
matplotlib

Autor: Mario Borges
Website: https://alpinista06.github.io
Ultima edicao: 16/08/2018
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from plotter import Ui_plotter
import random
import time

#Importacao do modulo matplotlib
import matplotlib.pyplot as plt
import numpy as np


class grafico(QDialog, Ui_plotter):


#variaveis globais e configuracao da plotagem

    leitura =[]
    fig, ax = plt.subplots(figsize=(5,4))
    i = 0
    comeco_eixo_x = 0
    fim_eixo_x = 50

    def __init__(self, parent=None):
        super(grafico, self).__init__()
        self.setupUi(self)

        # configuracao padrao do timer usando para criar um main loop
        self.meu_timer = QTimer()
        #configurando o intervalo entre as contagens do timer em microsec
        self.meu_timer.setInterval(1000)
        self.meu_timer.timeout.connect(self.contador)
        self.contador_do_timer = 0

        #conectores de eventos
        self.iniciar.clicked.connect(self.btn_iniciar)
        self.parar.clicked.connect(self.btn_parar)

    def btn_iniciar(self):
        self.meu_timer.start()

    def btn_parar(self):
        self.meu_timer.stop()

    def contador(self):
        self.contador_do_timer = self.contador_do_timer + 1
        self.plot(self.ax, self.leitura, self.fig, self.i, self.comeco_eixo_x, self.fim_eixo_x)

    # Metodo que plota um grafico, cria uma imagem chamada plot.jpg
    # e por fim insere essa imagem no label chamado grafico
    # parametros
    # ax: inicializacao do eixos
    # leitura: vetor que recebe os dados a cada loop
    # fig: inicializacao de uma figura para para salvar a plotagem
    # i: parametro usado no metodo pop para mover a linha do Grafico
    # fim_eixo_x: parametro que seta o fim do eixo x
    # comeco_eixo_x:parametro que seta o comeco do eixo x
    def plot(self, ax, leitura, fig, i, comeco_eixo_x, fim_eixo_x):
        #neste exemplo estou plotando um numero randomico
        dados = random.randint(59,69)
        ax.clear()
        #Titulo do grafico
        plt.title('Grafico do nivel de humidade do solo')
        ax.set_xlim([comeco_eixo_x, fim_eixo_x])   #faixa do eixo horizontal
        plt.xlabel('Tempo')
        ax.set_ylim([0,100]) # faixa do eixo vertical
        plt.ylabel('Nivel de humidade')
        leitura.append(dados)
        # plotagem do vetor de dados
        ax.plot(leitura)
        # salvando a imagem em uma fiura
        fig.savefig('plot.jpg')
        # bloco que move o eixo x quando a plotagem passa do limite
        if (self.contador_do_timer > fim_eixo_x):
            self.comeco_eixo_x += 1
            self.fim_eixo_x += 1
            leitura.pop(2)
            i=i+1
        # inserindo uma imagem no label grafico
        pixmap = QPixmap('plot.jpg')
        self.grafico.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    form = grafico()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
