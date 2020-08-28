class Pessoa: #Segundo a pep8 classes começa com letra maiuscula
    def __init__(self, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
         
    def cumprimentar(self): #metodo
        return f'Ola {id(self)}'

# from oo.pessoa import Pessoa
# p = Pessoa()

if __name__ == "__main__":
    p = Pessoa('Jatoba') #objeto
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) #objeto.metodo() ==> ja passa o objeto p implicitamente
    print(p.nome)
    p.nome = 'Bruno'
    print(p.nome)
    print(p.idade)