'''
Controle de estufa

Interface homem-maquina para sistema de controle
de ambiente de estufa desenvolvida para desktop com PyQt5

Autor: Mario Borges
Website: https://alpinista06.github.io
Ultima edicao: 11/08/2018
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_controle_estufa5 import Ui_controle_estufa
import random
import time

#tentando inserir graficos
import matplotlib.pyplot as plt
import numpy as np

class executar_em_segundo_plano(QRunnable):
    '''
    Estrutura de uma thread
    '''

    @pyqtSlot()
    def run(self):

        #Aqui vao as funcoes a serem executadas em segundo plano


        print("Inicio do processamento em segundo plano")
        time.sleep(5)
        print("Fim do processamento em segundo plano")

class regar_em_segundo_plano(QRunnable):
    '''
    Thread para regar em segundo plano
    '''
    @pyqtSlot()
    def run(self):
        print ("Estou regando")
        time.sleep(2)
        print ("Acabei de regar")

class ventilar_em_segundo_plano(QRunnable):
    '''
    Thread para ventilar em segundo plano
    '''
    @pyqtSlot()
    def run(self):
        print ("Estou ventilando")
        time.sleep(2)
        print ("Acabei de ventilar")

#Estrutura basica de um programa main do pyqt

class controlador(QDialog, Ui_controle_estufa):

    def __init__(self, parent=None):
        super(controlador, self).__init__()
        self.setupUi(self)


        #configuracao de inicializacao da thread
        self.threadpool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # configuracao padrao do timer
        self.meu_timer = QTimer()
        #configurando o intervalo entre as contagens do timer em microsec
        self.meu_timer.setInterval(1000)
        self.meu_timer.timeout.connect(self.contador)
        self.contador_do_timer = 0
        '''
        # inserindo uma imagem no label_4
        pixmap = QPixmap('estufa.jpg')
        self.label_4.setPixmap(pixmap)
        '''
        #configuracao da plotagem com matplotlib
        #ax = plt.subplots()

        #Conexoes dos eventos da Interface
        self.regador.clicked.connect(self.regar)
        self.ventilador.clicked.connect(self.ventilar)
        self.parar_medicoes.clicked.connect(self.parar_medidas)
        self.iniciar_medicoes.clicked.connect(self.iniciar_medidas)
        self.Estabelecer_conexao.clicked.connect(self.progresso_conexao)

    #Tarefa a ser realizada pelo contador a cada constante de tempo
    def contador(self):
        self.contador_do_timer = self.contador_do_timer + 1
        self.lcd_umidade.display(random.randint(50,85))
        self.lcd_temperatura.display(random.randint(19,40))
        #ploting
        '''
        fig, ax = plt.subplots()
        ax.clear()
        plt.title('Grafico do nivel de humidade do solo')
        ax.set_xlim([0,10])   #faixa do eixo horizontal
        plt.xlabel('Tempo')
        ax.set_ylim([0,10]) # faixa do eixo vertical
        plt.ylabel('Nivel de humidade')
        ax.plot(random.randint(50,85))
        fig.savefig('plot.jpg')

        # inserindo uma imagem no label_4
        pixmap = QPixmap('plot.jpg')
        self.label_4.setPixmap(pixmap)
        '''
    def progresso_conexao(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0002
            self.barra_de_conexao.setValue(self.completed)

    def iniciar_medidas(self):
        self.meu_timer.start()

    def parar_medidas(self):
        self.meu_timer.stop()

    def funcao_a_ser_executada_em_segundo_plano(self):
        worker = executar_em_segundo_plano()
        self.threadpool.start(worker)


    def regar(self):
        worker = regar_em_segundo_plano()
        self.threadpool.start(worker)


    def ventilar(self):
        worker = ventilar_em_segundo_plano()
        self.threadpool.start(worker)


def main():
    app = QApplication(sys.argv)
    form = controlador()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
