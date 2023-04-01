"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf_received = "74682489070"

cpf_to_list = [int(char) for char in cpf_received]

# Validation digit 1

nine_digits = cpf_to_list[:9]
count_regres = [i for i in range(2, 11)[::-1]]
result_digit_1 = 0

for i in range(0, 9):
    result_digit_1 += count_regres[i] * nine_digits[i]

digit_1 = (result_digit_1*10) % 11 
digit_1 = 0 if digit_1 > 9 else digit_1

# Validation digit 2

ten_digits = nine_digits.copy()
ten_digits.append(digit_1)

count_regres = [i for i in range(2, 12)[::-1]]
result_digit_2 = 0

for i in range(0, 10):
    result_digit_2 += count_regres[i] * ten_digits[i]

digit_2 = (result_digit_2*10) % 11 
digit_2 = 0 if digit_2 > 9 else digit_2

cpf_gerator = ''.join([str(num) for num in nine_digits]) + str(digit_1) + str(digit_2)

if cpf_gerator == cpf_received:
    print(f'{cpf_received} é válido!')
else:
    print('CPF inválido')