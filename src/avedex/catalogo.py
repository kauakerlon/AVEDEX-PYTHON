"""Listagem, busca, seleção e detalhes das aves."""

import random

from src.avedex.utils import (
    mensagem_aviso,
    normalizar_texto,
    paginar_aves,
    subtitulo,
    titulo,
    valor_ou_indisponivel,
)


CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo",
]


def listar_aves(aves):
    """Lista as aves com paginação e permite abrir os detalhes pelo ID."""

    ave = paginar_aves(aves, "AVES CADASTRADAS")

    if ave is not None:
        mostrar_detalhes(ave)


def mostrar_ave_aleatoria(aves):
    """Sorteia uma ave e mostra seus detalhes completos."""

    if not aves:
        mensagem_aviso("Nenhuma ave disponível para sorteio.")
        return

    ave = random.choice(aves)

    titulo("AVE ALEATÓRIA")
    print(f"Ave sorteada: {ave.get('nome_popular', 'Ave')}")

    mostrar_detalhes(ave)


def buscar_ave_por_id(aves, id_procurado):
    """Procura e devolve uma ave pelo ID."""

    for ave in aves:
        if str(ave.get("id")) == str(id_procurado):
            return ave

    return None


def ler_id_ave(mensagem):
    """Lê um ID numérico; ENTER cancela a operação."""

    entrada = input(mensagem).strip()

    if entrada == "":
        return None

    if not entrada.isdigit():
        mensagem_aviso("Digite apenas números para o ID.")
        return None

    return entrada


def escolher_ave(aves, mensagem="Escolha uma ave"):
    """Mostra a seleção paginada e devolve a ave escolhida."""

    print(mensagem)

    return paginar_aves(
        aves,
        "ESCOLHA UMA AVE"
    )


def mostrar_detalhes(ave):
    """Exibe os dados completos de uma ave."""

    titulo(ave.get("nome_popular", "Ave"))

    print(
        f"ID: {valor_ou_indisponivel(ave.get('id'))}"
    )

    print(
        f"Nome popular: "
        f"{valor_ou_indisponivel(ave.get('nome_popular'))}"
    )

    print(
        f"Nome científico: "
        f"{valor_ou_indisponivel(ave.get('nome_cientifico'))}"
    )

    print(
        f"Ordem: "
        f"{valor_ou_indisponivel(ave.get('ordem'))}"
    )

    print(
        f"Família: "
        f"{valor_ou_indisponivel(ave.get('familia'))}"
    )

    print(
        f"Dieta: "
        f"{valor_ou_indisponivel(ave.get('dieta_tipo'))}"
    )

    print(
        "Comprimento: "
        + valor_ou_indisponivel(
            ave.get("comprimento_cm"),
            "cm"
        )
    )

    print(
        "Peso médio: "
        + valor_ou_indisponivel(
            ave.get("peso_g"),
            "g"
        )
    )

    print(
        "Status de conservação: "
        + valor_ou_indisponivel(
            ave.get("status_conservacao")
        )
    )

    print(
        "Índice de conservação: "
        + valor_ou_indisponivel(
            ave.get("indice_conservacao")
        )
    )

    subtitulo("Descrição")
    print(
        valor_ou_indisponivel(
            ave.get("descricao")
        )
    )

    subtitulo("Habitat")
    print(
        valor_ou_indisponivel(
            ave.get("habitat")
        )
    )

    subtitulo("Alimentação")
    print(
        valor_ou_indisponivel(
            ave.get("alimentacao")
        )
    )

    curiosidade = ave.get("curiosidade")

    if curiosidade:
        subtitulo("Curiosidade")
        print(curiosidade)

    midia = ave.get("midia", {})

    if not isinstance(midia, dict):
        midia = {}

    subtitulo("Mídia")

    print(
        "Página no guia: "
        + valor_ou_indisponivel(
            midia.get("pagina_guia")
        )
    )

    print(
        "Fotógrafo: "
        + valor_ou_indisponivel(
            midia.get("fotografo")
        )
    )

    print(
        "WikiAves: "
        + valor_ou_indisponivel(
            midia.get("wikiaves_url")
        )
    )

    print(
        "Som: "
        + valor_ou_indisponivel(
            midia.get("som_url")
        )
    )

    print(
        "Imagem: "
        + valor_ou_indisponivel(
            midia.get("imagem_url")
        )
    )


def tela_detalhes(aves):
    """Permite escolher uma ave e abrir seus detalhes."""

    ave = escolher_ave(
        aves,
        "Escolha uma ave para ver os detalhes"
    )

    if ave is not None:
        mostrar_detalhes(ave)


def criar_texto_busca(ave):
    """Monta o texto pesquisável de uma ave."""

    valores = [
        str(ave.get(campo, ""))
        for campo in CAMPOS_BUSCA
    ]

    return normalizar_texto(" ".join(valores))


def buscar_lista_aves(aves, termo_busca):
    """Devolve as aves que contêm o termo em algum campo pesquisável."""

    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in aves:
        if termo in criar_texto_busca(ave):
            resultados.append(ave)

    return resultados


def buscar_aves(aves):
    """Executa a busca textual e permite abrir um resultado."""

    titulo("BUSCAR AVE")

    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        mensagem_aviso(
            "Digite algum texto para realizar a busca."
        )
        return

    resultados = buscar_lista_aves(
        aves,
        termo
    )

    if not resultados:
        mensagem_aviso("Nenhuma ave encontrada.")
        return

    ave = paginar_aves(
        resultados,
        "RESULTADOS DA BUSCA"
    )

    if ave is not None:
        mostrar_detalhes(ave)