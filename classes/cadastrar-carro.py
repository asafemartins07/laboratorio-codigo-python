class Carro:
  def __init__ (self,marca,modelo,ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def Descrever(self):
    print(f"esse carro é do modelo {self.modelo}, da marca {self.marca}, e do ano {self.ano}")

  def Ligar(self):
    return f" o carro {self.modelo}, esta ligado "

carrinho = Carro("mitsubish", "Lancer evo 9", 2009)
carrinho.Descrever()
carrinho.Ligar()
