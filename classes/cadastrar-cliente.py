class cliente:
  def __init__(self,nome,idade,cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
  def exibir_dados(self):
    print(f"{self.nome},{self.idade},{self.cpf}")

Usuario = cliente('asafe', ' 18', ' 15458640985')
Usuario.exibir_dados()
