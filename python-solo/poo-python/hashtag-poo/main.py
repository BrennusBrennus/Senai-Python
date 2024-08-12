import cmath
import cmd
from os import system
from time import sleep

class ControleRemoto:

    def __init__(self, cor, altura, largura, profundidade):

        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade


controle_remoto_um = ControleRemoto("rosa", "30 cm", "6 cm", "3.5 cm")

controle_remoto_dois = ControleRemoto("verde", "13 cm", "5 cm", "1 cm")