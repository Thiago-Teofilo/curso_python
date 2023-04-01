# Exercícios
# Crie funções que duplicam, triplicam e quadrúplicam
# o número recebido como parâmetro.

def create_mult(num_mult):
    def mult(num):
        return num * num_mult
    return mult

duplicate = create_mult(2)
triple = create_mult(3)
quadruple = create_mult(4)

execute_def = (duplicate, triple, quadruple)

for data in execute_def:
    print(data(2))