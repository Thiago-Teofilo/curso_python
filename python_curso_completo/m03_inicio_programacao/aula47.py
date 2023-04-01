"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    nome_invertido = nome[::-1]
    contem_espacos = " " in nome
    qtd_letras = len(nome)
    primeira_letra_nome = nome[0]
    ultima_letra_nome = nome[-1]

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Seu nome {'contém' if contem_espacos else 'não contém'} espaços")
    print(f"Seu nome tem {qtd_letras} letras")
    print(f"A primeira letra do seu nome é '{primeira_letra_nome}'")
    print(f"A ultima lera do seu nome é '{ultima_letra_nome}'")
else:
    print("Desculpe, você deixou campos vazios.")