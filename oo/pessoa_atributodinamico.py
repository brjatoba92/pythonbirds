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
    jatoba = Pessoa(nome = 'Jatoba')
    gustavo = Pessoa(jatoba, nome = 'Gustavo') 
    rafael = Pessoa(jatoba, gustavo, nome = 'Rafael') #gustavo filho do Rafael
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar()) #objeto.metodo() ==> ja passa o objeto p implicitamente
    print(rafael.nome)
    print(rafael.idade)
    print('Filhos: ')
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome ='Gomes' #atributo dinamico
    print(rafael.sobrenome)
    print(rafael.__dict__) #informa todos os atributos de instancia ligados ao objeto nome(rafael)
    print(gustavo.__dict__)
    #print(rafael.filhos)
