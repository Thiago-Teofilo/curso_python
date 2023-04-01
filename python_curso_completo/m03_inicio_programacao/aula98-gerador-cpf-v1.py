"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0       - Step_1
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301     - Step_1_sum
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7                       - Step_1_div
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

user_cpf = input("Digite o CPF: ")

# Inconcistencias
invalid_cpf = "CPF Inválido!"
unknown_err = "Erro desconhecido!"

# Removendo os caracteres extras do cpf para adicionar a uma list e testando o tamanho do cpf
list_cpf_digits = user_cpf.replace(".", "")
list_cpf_digits = list_cpf_digits.replace("-", "")

# Variável booleana para saber se irá ser abortada a execução
abort = False

# Variáveis para validação
step_1 = []
step_1_sum = 0
step_1_div = 0

try:
    list_cpf_digits = [int(char) for char in list_cpf_digits]
    step_1 = [num*(10 - i) for i, num in enumerate(list_cpf_digits[:-2])]

    for num in step_1:
        step_1_sum += num

    step_1_div = (step_1_sum * 10) % 11

    if step_1_div > 9:
        step_1_div = 0
        
except ValueError:
    print(invalid_cpf)
    abort = True
except Exception:
    print(unknown_err)
    abort = True

print(step_1_div)

if len(list_cpf_digits) == 11 and not abort:
  for i in range(len(list_cpf_digits)):
      if i == 0:
         print(i)
