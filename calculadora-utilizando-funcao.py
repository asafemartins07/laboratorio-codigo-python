def soma(numeroa, numerob):
  resultado = numeroa + numerob
  print(f"O resultado da soma é: {resultado}")
  
def subtracao(numeroa, numerob):
  resultado = numeroa - numerob
  print(f"o resultado é: {resultado}")


def multiplicacao(numeroa, numerob):
  resultado = numeroa * numerob
  print(f"o resultado é: {resultado}")

def divisao(numeroa, numerob):
  resultado = numeroa / numerob
  print(f"o resultado é: {resultado}")

def raiz(numeroA):
  resultado = numeroA ** 0.5
  print(f"O resultado é: {resultado}")
  
while True:
  opcao = int(input("MENU, escolha sua formula para    calcular! APENAS NUMEROS!"))
  
  if (opcao ==  1):
    numeroa = float(input("Digite o 1º número: "))
    numerob = float(input("digite o 2° numero: "))
    soma(numeroa, numerob)
    break

  elif (opcao == 2):
  
   numeroa =float(input("digite o 1° numero: "))
   numerob =float(input("digite o 2° numero:" ))
   subtracao(numeroa, numerob)
   break
    
  elif (opcao == 3):
    numeroa = float(input("digite o 1° numero: "))
    numerob = float(input("digite o 2° numero: "))
    multiplicacao(numeroa, numerob)
    break
  elif (opcao == 4):
      numeroa = float(input("digite o primeiro numero: "))
      numerob = float(input("digite o 2° número: "))
      divisao(numeroa, numerob)
      break
  elif (opcao == 5):
    numeroa = float(input("Digite o número: "))
    raiz(numeroa)
    break

