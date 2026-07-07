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
    print("3 - Ver uma curiosidade sobre aves")
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
        listar_aves(catalogo_aves)

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