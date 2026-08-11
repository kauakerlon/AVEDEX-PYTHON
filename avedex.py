import unicodedata


def normalizar_texto(texto):
    # Converte o valor recebido para texto.
    texto = str(texto)

    # Padroniza para minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa letras e acentos.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os acentos e mantém apenas as letras.
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def pausar():
    # Pausa a execução para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    # Exibe apenas ID e nome popular para facilitar a escolha.
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    # Percorre o catálogo procurando uma ave com o ID informado.
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    # Se nenhuma ave for encontrada, retorna None.
    return None


def exibir_detalhes_ave(ave):
    # Exibe informações completas de uma ave.
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    # Mostra as aves antes de pedir o ID.
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()

    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def buscar_aves(catalogo, termo_busca):
    # Lista que armazenará as aves encontradas.
    resultados = []

    # Normaliza o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves cadastradas.
    for ave in catalogo:
        # Campos em que a busca será realizada.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Junta todos os campos em um único texto.
        texto_busca = " ".join(campos_busca)

        # Normaliza o texto da ave.
        texto_busca = normalizar_texto(texto_busca)

        # Se o termo estiver no texto, a ave entra nos resultados.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    # Mostra os resultados encontrados pela busca.
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    # Solicita o termo de busca.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    # Busca as aves e exibe os resultados.
    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)

    # Se houver resultados, permite abrir os detalhes.
    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(resultados, escolha)

            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)


catalogo_aves = [
    {
        # ID único da ave.
        "id": 1,

        # Nomes da ave.
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",

        # Classificação.
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",

        # Tipo principal de dieta.
        "dieta_tipo": "Onívora",

        # Ambiente onde a ave costuma viver.
        "habitat": "Áreas abertas, cidades e bordas de florestas",

        # Medidas aproximadas usadas na comparação.
        "comprimento_cm": 23,
        "peso_g": 68,

        # Situação de conservação.
        # Nesta versão didática, usamos texto simples.
        "status_conservacao": "Pouco preocupante",

        # Índice numérico que será útil futuramente na batalha.
        # Quanto maior, maior será o nível de atenção na conservação.
        "indice_conservacao": 1,

        # Outros detalhes.
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
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        print("A AveDex é um catálogo interativo de aves.")
        print(
        "Em breve, teremos batalha, imagens, sons "
        "e dados em arquivo JSON."
    )

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print(
        "Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5."
    )

    if opcao_menu != "0":
        pausar()

def valor_ou_indisponivel(valor, unidade=""):
        # Se o valor for None ou texto vazio, informamos isso ao usuário.
        if valor is None or valor == "":
            return "Não informado"
        
        # Se uma unidade foi informada, adicionamos essa unidade ao valor.
        # Exemplo: valor 23 com unidade "cm" vira "23 cm".
        if unidade != "":
            return f"{valor} {unidade}"
        
        # Se não houver unidade, retornamos o valor como texto.
            return str(valor)

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    # O rótulo identifica o campo comparado.
    # Exemplo: "Família", "Dieta" ou "Peso".
    #
    # O símbolo :<18 significa:
    # alinhar à esquerda em um espaço de 18 caracteres.
    #
    # Isso ajuda a deixar a saída parecida com uma tabela.
    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")

def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    # Primeira linha: mostra os nomes das duas aves.
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    # Linhas de comparação textual.
    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    # Linhas de comparação numérica com unidade.
    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(
            ave_1.get("comprimento_cm"),
            "cm"
        ),
        valor_ou_indisponivel(
            ave_2.get("comprimento_cm"),
            "cm"
        )
    )

    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(
            ave_1.get("peso_g"),
            "g"
        ),
        valor_ou_indisponivel(
            ave_2.get("peso_g"),
            "g"
        )
    )

    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get("status_conservacao", "Não informado"),
        ave_2.get("status_conservacao", "Não informado")
    )

    imprimir_linha_comparacao(
        "Índice",
        ave_1.get("indice_conservacao", "Não informado"),
        ave_2.get("indice_conservacao", "Não informado")
    )

    def escolher_ave(catalogo, mensagem):
        # Mostra a lista de aves antes de pedir o ID.
        listar_aves(catalogo)

        # A mensagem muda conforme a situação.
        # Exemplo: "Digite o ID da primeira ave".
        id_escolhido = input(f"\n{mensagem}: ").strip()

        # Reaproveitamos a função que já busca ave por ID.
        ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

        # Se nenhuma ave for encontrada, avisamos e retornamos None.
        if ave_encontrada is None:
            print("Ave não encontrada. Confira o ID informado.")
            return None

        # Se encontrou, devolvemos a ave escolhida.
        return ave_encontrada

def comparar_duas_aves(catalogo):
    print()
    print("Escolha a primeira ave")

    # Escolhe a primeira ave.
    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    # Se a primeira ave não foi encontrada, encerramos a função.
    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    # Escolhe a segunda ave.
    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    # Se a segunda ave não foi encontrada, encerramos a função.
    if ave_2 is None:
        return

    # Se as duas aves existem, exibimos a comparação.
    exibir_comparacao_aves(ave_1, ave_2)