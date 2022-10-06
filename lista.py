from no import *


class Lista:


    def __init__(self):

        self.inicio = None
        self.final = None
        self.tamanho = 0

    def insere_inicio(self, elem):
        novo = No(elem)
        novo.prox = self.inicio
        self.inicio = novo
        self.tamanho = self.tamanho + 1
        
    def mostrar(self):
        auxiliar = self.inicio
        while auxiliar is not None:
            print(auxiliar.elem)
            auxiliar = auxiliar.prox


    def insere_final(self, elem):
        novo = No(elem)
        novo.prox = None
        self.final.prox = novo
        self.final = novo
        self.tamanho = self.tamanho + 1



