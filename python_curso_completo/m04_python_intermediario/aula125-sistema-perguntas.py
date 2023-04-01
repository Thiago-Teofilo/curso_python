# Exercício - sistema de perguntas e respostas


question_dict = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

def ask(question):
    question_tuple = tuple(question.values())
    ask = question_tuple[0]
    alternatives = question_tuple[1]
    answer = question_tuple[2]

    print()
    print(f'Pergunta: {ask}')
    print()
    print('Opções:')

    for i, value in enumerate(alternatives):
        print(f'{i}) {value}')

    user_choice = int(input("Escolha uma opção: "))
    if alternatives[user_choice] == answer:
        return True
    return False

count_hits = 0
for question in question_dict:
    if ask(question) is True:
        print("Parabéns, você acertou!!")
        count_hits += 1
    else:
        print("Você errou!")

print()
print(f'Total de acertos {count_hits}')
print("\n")