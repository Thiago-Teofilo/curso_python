# Mensagens de erros
INT_VAL_ERROR_MSG = "Erro! Digite um número inteiro válido"

try:
  jump_to = int(input("Qual exercício deseja executar? (1/2/3) "))

  if jump_to == 1:
    """
    Exercicio 1
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
    """
    try:
      value = int(input("Digite um número inteiro: "))
      
      it_pair = value % 2 == 0
      print(f"O número digitado é {'par' if it_pair else 'impar'}!")
    except ValueError:
      print(INT_VAL_ERROR_MSG)

  elif jump_to == 2:
    """
    Exercicio 2
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
    descrito, exiba a saudação apropriada. Ex. 
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
    """
    try:
      time = int(input("Digite a hora atual: "))

      if time >= 0 and time <= 11:
        print("Bom dia!")
      elif time <= 17:
        print("Boa tarde!")
      elif time <= 23:
        print("Boa noite!")
      else:
        print("Erro! Digite uma hora válida")

    except ValueError:
      print(INT_VAL_ERROR_MSG)


  elif jump_to == 3:
    """
    Exercicio 3
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
    menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
    "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
    """
    name = input("Digite seu primeiro nome: ")

    qtt_char = len(name)

    if qtt_char > 0:
      if qtt_char <= 4:
        print("Seu nome é curto")
      elif qtt_char <= 6:
        print("Seu nome é normal")
      elif qtt_char > 6:
        print("Seu nome é muito grande")
    else:
      print("Erro! Digite um número válido")

except ValueError:
  print(INT_VAL_ERROR_MSG)