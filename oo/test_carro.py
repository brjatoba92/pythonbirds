from unittest import TestCase
from oo.carro import Motor
from oo.carro import Direcao

class CarroTestCase(TestCase):

    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def teste_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.direcao)

    def teste_direita(self):
        direcao = Direcao()
        direcao.mudar_a_direita()
        self.assertEqual('Leste', direcao.direcao)
        direcao.mudar_a_direita()
        self.assertEqual('Sul', direcao.direcao)
        direcao.mudar_a_direita()
        self.assertEqual('Oeste', direcao.direcao)
        direcao.mudar_a_direita()
        self.assertEqual('Norte', direcao.direcao)

    def teste_esquerda(self):
        direcao = Direcao()
        direcao.mudar_a_esquerda()
        self.assertEqual('Oeste', direcao.direcao)
        direcao.mudar_a_esquerda()
        self.assertEqual('Sul', direcao.direcao)
        direcao.mudar_a_esquerda()
        self.assertEqual('Leste', direcao.direcao)
        direcao.mudar_a_esquerda()
        self.assertEqual('Norte', direcao.direcao)