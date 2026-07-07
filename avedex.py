catalogo_aves = [
    {
        "codigo": "1",
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "codigo": "2",
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "habitat": "Campos, áreas abertas e ambientes rurais",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "codigo": "3",
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros pequenos invertebrados",
        "curiosidade": "Constrói um ninho de barro característico."
    }
]


def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def listar_aves(catalogo):
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()

    for ave in catalogo:
        print(f"{ave['codigo']} - {ave['nome_popular']}")


def buscar_ave_por_codigo(catalogo, codigo_procurado):
    for ave in catalogo:
        if ave["codigo"] == codigo_procurado:
            return ave
    return None


def exibir_detalhes(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves brasileiras.")
    print("Seu objetivo é apresentar informações sobre diferentes espécies.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# Programa principal
nome_usuario = input("Digite seu nome: ")

while True:
    exibir_menu()
    opcao_menu = input("\nEscolha uma opção: ").strip()

    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)

    elif opcao_menu == "2":
        listar_aves(catalogo_aves)

    elif opcao_menu == "3":
        listar_aves(catalogo_aves)
        codigo_escolhido = input("\nDigite o código da ave: ").strip()

        ave_encontrada = buscar_ave_por_codigo(
            catalogo_aves,
            codigo_escolhido
        )

        if ave_encontrada is not None:
            exibir_detalhes(ave_encontrada)
        else:
            print("Ave não encontrada. Confira o código informado.")

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Obrigado por usar a AveDex. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

    pausar()