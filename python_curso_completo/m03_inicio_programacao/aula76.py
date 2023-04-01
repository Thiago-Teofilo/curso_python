"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

word = "perfume"
len_word = len(word)

pass_str = "*"*len_word
try_count = 0

while True:
    print(pass_str)
    letter = input("Digite uma letra: ")
    try_count += 1

    if len(letter) > 1:
        print("Digite apenas uma letra!")
        continue
    
    if letter in word:
        for i in range(len_word):
            if word[i] == letter:
                pass_str = f"{pass_str[0:i:1]}{letter}{pass_str[i + 1:len_word:1]}"    
    if pass_str == word:
        os.system("clear")
        print("Parabéns! conseguiu")
        print("Tentativas:", try_count)
        break