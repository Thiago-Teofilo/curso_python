# Calculadora com while
while True:
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operator = input("Digite o operador (+-/*): ")

    valid_nums = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_nums = True
    except:
        valid_nums = None
    
    if valid_nums is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operators_alowed = "+-/*"

    if operator not in operators_alowed:
        print("Operador inválido.")
        continue
    
    if len(operator) > 1:
        print("Digite apenas um operador.")
        continue
    
    print("Realizando sua conta. Confira o resultado abaixo")
    
    if operator == '+':
        print(num_1_float + num_2_float)
    elif operator == '-':
        print(num_1_float - num_2_float)
    elif operator == '/':
        print(num_1_float / num_2_float)
    elif operator == '*':
        print(num_1_float * num_2_float)
    else:
        print("Não deveria chegar aqui.")

    leave = input("Deseja sair? [s]im: ").lower().startswith('s')

    if leave:
        break