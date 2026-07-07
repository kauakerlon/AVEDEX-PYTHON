def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Conhecer uma ave")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def mostrar_ave_inicial():
    print("Ave escolhida: Bem-te-vi")
    print("Nome científico: Pitangus sulphuratus")
    print("O bem-te-vi é uma das aves mais conhecidas do Brasil.")


def mostrar_curiosidade():
    print("Curiosidade:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex será um catálogo interativo de aves.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# Programa principal
nome_usuario = input("Digite seu nome: ")

while True:
    exibir_menu()
    opcao_menu = input("\nEscolha uma opção: ")

    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)

    elif opcao_menu == "2":
        mostrar_ave_inicial()

    elif opcao_menu == "3":
        mostrar_curiosidade()

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Obrigado por usar a AveDex. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

    pausar()