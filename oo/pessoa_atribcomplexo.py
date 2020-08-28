class Pessoa: #Segundo a pep8 classes começa com letra maiuscula
    def __init__(self, *filhos, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
         
    def cumprimentar(self): #metodo
        return f'Ola {id(self)}'

# from oo.pessoa import Pessoa
# p = Pessoa()

if __name__ == "__main__":
    gustavo = Pessoa(nome = 'Gustavo') 
    rafael = Pessoa(gustavo, nome = 'Rafael') #gustavo filho do Rafael
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar()) #objeto.metodo() ==> ja passa o objeto p implicitamente
    print(rafael.nome)
    print(rafael.idade)
    for filho in rafael.filhos:
        print(filho.nome)
    #print(rafael.filhos)
