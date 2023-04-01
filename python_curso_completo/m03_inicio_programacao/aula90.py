import os

purshace_list = []

while True:
    print("Selecione uma opção")
    option = input("[a]pagar [i]nserir [l]istar: ")
    option = option.lower()

    if option == "a":
        if len(purshace_list) > 0:
            i = input("Insira o índice: ")
            try:
                del purshace_list[int(i)]
            except IndexError:
                print("Índice não existe!")
            except ValueError:
                print("Por favor digite um valor inteiro!")
            except Exception:
                print("Erro desconhecido")
        else:
            print("Lista já está vazia!")
    
    elif option == "i":
        new_item = input("Digite o nome do item: ")
        purshace_list.append(new_item)
    
    elif option == "l":
        os.system("clear")
        if len(purshace_list) > 0:
            for i, item in enumerate(purshace_list):
                print(i, item)
        else:
            print("Lista está vazia!")

    else:
        print("Programa finalizado")
        break
