# --- Banco de dados inicial (Catálogo de Aves atualizado com detalhes) ---
catalogo_aves = [
    {
        # Identificador único da ave.
        "id": 1,

        # Nome mais conhecido da ave.
        "nome_popular": "Bem-te-vi",

        # Nome científico da espécie.
        "nome_cientifico": "Pitangus sulphuratus",

        # Classificação taxonômica.
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",

        # Tipo principal de dieta.
        "dieta_tipo": "Onívora",

        # Informações descritivas usadas nos detalhes.
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    }
]

# --- Funções do Sistema ---

def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Listar aves")
    print("2 - Conhecer uma ave (Detalhes)")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    print()
    print("-" * 50)
    print("AVES CADASTRADAS")
    print("-" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave
    return None


def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Tipo de dieta: {ave.get('dieta_tipo', 'Não informado')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def mostrar_curiosidade():
    print("Curiosidade Geral:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex será um catálogo interativo de aves.")
    print("Ao longo da disciplina, adicionaremos novas funcionalidades.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# --- Programa principal ---
exibir_linha()
print("AVEDEX")
exibir_linha()

nome_usuario = input("Digite seu nome: ").strip()

print(f"\nOlá, {nome_usuario}!")
print("Seja bem-vindo(a) à AveDex.")

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()
    print()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "3":
        mostrar_curiosidade()

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "0":
        print(f"Até logo, {nome_usuario}! Obrigado por usar a AveDex.")

    else:
        print("Opção inválida. Tente novamente.")

    if opcao_menu != "0":
        pausar() 

    print()