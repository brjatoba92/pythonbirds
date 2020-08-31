"""
PROGRAMA CARRO
- COMPOSTO POR DUAS CLASSES: A) MOTOR E B) DIRECAO
A) MOTOR: INCLUI TRES ATRIBUTOS = VELOCIDADE (0 COMO INICIAL), ACELERAR (ACRESCENTA 1 UNIDADE) E FREAR (REDUZ 2 UNIDADES E QUANDO NEGATIVO IMPLEMENTA 0 COMO VALOR)
B) DIREÇÃO: INCLUI TRES ATRIBUTOS = DIREÇÃO (NORTE COMO INICIAL), MUDAR PARA DIREITA (VARIAR NO SENTIDO HORARIO N ==> L, L ==> S, ...) 
E MUDAR PARA DIREITA (VARIAR NO SENTIDO ANTIHORARIO N ==> O, O ==> S, ...)
- IMPLEMENTA CLASSE CARRO PARA INCLUSÃO DAS CLASSES MOTOR E DIREÇÃO 
"""
#implementando a classe motor ok
class Motor(): 
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2

if __name__ == "__main__":
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    if motor.velocidade < 1: #incluindo 0 para evitar valores negativos 
        print(0)
    #print(motor.velocidade)

#implementando a classe direcao ok
class Direcao():
    def __init__ (self):
        self.direcao = 'Norte'
    
    def mudar_a_direita(self): 
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def mudar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'    

if __name__ == "__main__":
    direcao = Direcao() #criando variavel para a classe
    print(direcao.direcao) #Norte 
    """sentido horario"""
    direcao.mudar_a_direita()
    print(direcao.direcao) #Norte ==> Leste
    direcao.mudar_a_direita()
    print(direcao.direcao) #Leste ==> Sul
    direcao.mudar_a_direita()
    print(direcao.direcao) # Sul ==> Oeste
    direcao.mudar_a_direita()
    print(direcao.direcao) #Oeste ==> Norte
    """ sentido antihorario"""
    print(direcao.direcao) #Norte
    direcao.mudar_a_esquerda()
    print(direcao.direcao) #Norte ==> Leste
    direcao.mudar_a_esquerda()
    print(direcao.direcao) #Leste ==> Sul
    direcao.mudar_a_esquerda()
    print(direcao.direcao) # Sul ==> Oeste
    direcao.mudar_a_esquerda()
    print(direcao.direcao) #Oeste ==> Norte

#implementação da classe carro que inclui duas outras classes: direcao e motor ok
class Carro():
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calculando_velocidade(self):
        return self.motor.velocidade #atributo da classe motor
    def carro_acelerar(self):
        return self.motor.acelerar() #atributo da classe motor
    def carro_frear(self):
        return self.motor.frear() ##atributo da classe motor
    def calcular_direcao(self):
        return self.direcao.direcao #atributo da classe direcao
    def virar_a_direita(self):
        return self.direcao.mudar_a_direita() #atributo da classe direcao
    def virar_a_esquerda(self):
        return self.direcao.mudar_a_esquerda() #atributo da classe direcao
    
if __name__ == "__main__":
    motor = Motor() #criando variaveis para as classes
    direcao = Direcao()
    carro = Carro(direcao, motor)
    #motor
    print(carro.calculando_velocidade()) 
    carro.carro_acelerar() #classe(carro).atributo(carro_acelerar)
    print(carro.calculando_velocidade())
    carro.carro_acelerar()
    print(carro.calculando_velocidade())
    carro.carro_frear() #classe(carro).atributo(carro_frear)
    print(carro.calculando_velocidade())
    #direcao
    print(carro.calcular_direcao())
    carro.virar_a_direita() #classe(carro).atributo(virar_a_direita)
    print(carro.calcular_direcao())
    carro.virar_a_esquerda() #classe(carro).atributo(virar_a_esquerda)
    print(carro.calcular_direcao())
    carro.virar_a_esquerda() #classe(carro).atributo(virar_a_esquerda)
    print(carro.calcular_direcao())    
