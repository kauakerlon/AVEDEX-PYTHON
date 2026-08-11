import unicodedata

def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Ver detalhes de uma ave")
    print("3 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)
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


catalogo_aves = [
    {
        # Identificador único da ave.
        # Usamos o ID para escolher uma ave no menu.
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

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ").strip()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "3":
        print("A AveDex é um catálogo interativo de aves.")
        print("Aos poucos, vamos adicionar busca, comparação, documentação e testes.")

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2 ou 3.")

    if opcao_menu != "0":
        pausar()

def buscar_aves_por_nome(catalogo, termo_busca):
    resultados = []

    # Normalizamos o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        # Normalizamos também o nome cadastrado.
        nome = normalizar_texto(ave["nome_popular"])

        if termo in nome:
            resultados.append(ave)

    return resultados

def normalizar_texto(texto):
    # Garante que o valor recebido será tratado como texto.
    texto = str(texto)

    # Converte para minúsculas e remove espaços no início e no final.
    texto = texto.lower().strip()

    # Separa as letras dos sinais de acentuação.
    # Exemplo: "á" passa a ser tratado como "a" + acento.
    texto = unicodedata.normalize("NFD", texto)

    # Monta um novo texto removendo os sinais de acentuação.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto

def buscar_aves(catalogo, termo_busca):
    # Lista que receberá todas as aves encontradas.
    resultados = []

    # Normalizamos o termo digitado uma única vez.
    termo = normalizar_texto(termo_busca)

    # Percorremos todas as aves do catálogo.
    for ave in catalogo:
        # Separamos os campos em que a busca será feita.
        # Usamos get() para evitar erro caso alguma chave esteja ausente.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Juntamos todos os campos em um único texto.
        # Assim, a busca pode procurar em todos eles de uma vez.
        texto_busca = " ".join(campos_busca)

        # Normalizamos o texto completo da ave.
        texto_busca = normalizar_texto(texto_busca)

        # Se o termo digitado estiver no texto da ave,
        # adicionamos essa ave aos resultados.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados