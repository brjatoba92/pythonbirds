"""
RESULTADO CANDIDATO ENEM
- INFORMA O NOME DO CANDIDATO
- IDADE
- CURSOS APROVADOS PELA NOTA DE CORTE
"""

class Enem: #Segundo a pep8 classes começa com letra maiuscula

    def __init__(self, *cursos, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
        self.cursos = list(cursos)
         
    def cumprimentar(self): #metodo
        return f'Bem vindo ao Sistema de Seleção Unificada - SISU 2021 {id(self)}'


if __name__ == "__main__":
    nota_de_corte = int(input('Digite sua pontuação: '))
    candidato = str(input('Informe seu nome:'))

    if 500 < int(nota_de_corte) < 650:
        x = ["meteorologia", "fisica", "matematica"]
    elif  int(nota_de_corte) > 650:
        x = ["direito", "engenharia",  "medicina"]
    else:
        x = ["pedagogia", "historia",  "filosofia"]
    print(x)

    
    x[0] = Enem(nome = x[0])
    x[1] = Enem(x[0], nome = x[1])
    x[2] = Enem(x[1], x[0], nome = x[2])
    candidato = Enem(x[2], x[1], x[0], nome = candidato)
    print(id(x[2]))
    print(candidato.cumprimentar()) 
    print(candidato.nome)
    print(candidato.idade)
    print('Parabens!!! Você foi aprovado nos seguintes cursos: ')
    for filho in candidato.cursos:
        print(filho.nome)
    
    """
    str(x[0]) = Enem(nome = 'Jatoba')
    str(x[1]) = Enem(x[0], nome = 'Gustavo') 
    str(x[2]) = Enem(x[1], x[0], nome = 'Rafael') #gustavo filho do Rafael
    print(Enem.cumprimentar(x[2])
    #print(id(x[2]))
    print(x[2].cumprimentar()) #objeto.metodo() ==> ja passa o objeto p implicitamente
    print(x[2].nome)
    print(x[2].idade)
    print('Filhos: ')
    for filho in x[2].cursos:
        print(filho.nome)
    #print(rafael.cursos)
"""