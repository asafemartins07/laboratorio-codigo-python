def calculo(numeroA, numeroB):
  soma = numeroA + numeroB
  subtracao = numeroA - numeroB
  multi = numeroA * numeroB
  divisao = numeroA / numeroB
  print(f"soma: {soma}, subtracao: {subtracao}, multiplicação: {multi}, divisão: 1{divisao}")

numeroA = float(input("número 1:"))
numeroB = float(input("numero 2:"))
calculo(numeroA, numeroB)

