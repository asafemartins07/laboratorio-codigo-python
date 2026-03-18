class dados_obrigatorios:
  def __init__(self):
      self.nome = input('digite seu nome! ')
      self.idade = input('Sua idade! ')
      self.cpf  = int(input('Digite seu CPF!  '))

  def resultar(self,nome,idade,cpf):
     self.nome = nome
     self.idade =  idade
     self.cpf  = cpf

class Professor(dados_obrigatorios):
    def dados(self,turma,disciplina):
     self.turma = turma
     self.discisplina = disciplina

    def dados_apresentar(self):
     self.turma = input('digite sua turma ')
     self.disciplina = input('digite suas diciplinas ')
     print(f'olá, sou o professor {self.nome}, e sou das diciplinas de {self.disciplina}, MUITO PRAZER!')
     print('-'*20)

class Aluno(dados_obrigatorios):
  def dados_aluno(self,turma1,):
    self.turma1 = turma1

  def apresentar(self):
    self.turma1 = input('digite sua turma! ')
    print(f'Olá, sou aluno {self.nome}, tenho {self.idade} anos, e sou da turma {self.turma1}.')

prof = Professor()
prof.dados_apresentar()
aluno = Aluno()
aluno.apresentar()







