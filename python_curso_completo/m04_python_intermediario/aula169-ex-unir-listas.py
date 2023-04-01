# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(*list_1):
    def intern(*list_2):
        new_list = [
            (list_1[i], list_2[i]) 
            for i in range(min(len(list_1), len(list_2)))
        ]
        return new_list
    return intern

new_zipper = zipper('Salvador', 'Ubatuba', 'Belo Horizonte')
new_list = new_zipper('BA', 'SP', 'MG', 'RJ')

print(new_list)