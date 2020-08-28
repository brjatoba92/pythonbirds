class Pessoa: #Segundo a pep8 classes começa com letra maiuscula
    def cumprimentar(self):
        return f'Ola {id(self)}'

# from oo.pessoa import Pessoa
# p = Pessoa()

if __name__ == "__main__":
    p = Pessoa()
    print(id(p))
    print(p.cumprimentar())