import json
from pathlib import Path

from src.avedex.utils import mensagem_erro

# __file__ representa o caminho deste arquivo dados.py..
#
# Como dados.py está em src/avedex/dados.py, usamos parents[2]
# para chegar à raiz do projeto.

CAMINHO_PROJETO = Path(__file__).resolve().parents[2]


# Caminho do arquivo JSON usado pela AveDex.

CAMINHO_DATASET = (
    CAMINHO_PROJETO
    / "data"
    / "avedex_dataset_midias.json"
)

CAMPOS_OBRIGATORIOS = [
    "id",
    "slug",
    "nome_popular",
    "nome_cientifico",
    "ordem",
    "familia",
    "dieta_tipo",
    "comprimento_cm",
    "peso_g",
    "status_conservacao",
    "indice_conservacao",
    "descricao",
    "habitat",
    "alimentacao",
    "midia",
]

CAMPOS_MIDIA = [
    "pagina_guia",
    "fotografo",
    "wikiaves_url",
    "som_url",
    "imagem_url",
]

def carregar_dataset(caminho=CAMINHO_DATASET):
    # Tenta abrir e ler o arquivo JSON.
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    # Este erro acontece quando o arquivo não existe.
    except FileNotFoundError:
        mensagem_erro(
            f"Arquivo de dataset não encontrado: {caminho}"
        )
        return {
            "nome_dataset": "AveDex",
            "aves": []
        }

    # Este erro acontece quando o JSON está mal formatado.
    except json.JSONDecodeError:
        mensagem_erro("Erro ao ler o JSON do dataset.")
        mensagem_erro(
            "Verifique vírgulas, aspas, chaves e colchetes."
        )
        return {
            "nome_dataset": "AveDex",
            "aves": []
        }


def carregar_aves():
    # Carrega o dataset completo.

    dataset = carregar_dataset()

    # Retorna apenas a lista de aves.
    # Se a chave "aves" não existir, retorna lista vazia.

    return dataset.get("aves", [])


def obter_fontes_globais():
    # Carrega o dataset completo.

    dataset = carregar_dataset()

    # Retorna as fontes gerais cadastradas no JSON.

    return dataset.get("fontes_globais", {})


if __name__ == "__main__":
    aves = carregar_aves()

    print(f"Total de aves carregadas: {len(aves)}")

    for ave in aves:
        print(ave["nome_popular"])

def validar_dataset(aves):
    # Lista que guardará todos os problemas encontrados.
    problemas = []

    # Conjunto usado para identificar IDs repetidos.
    ids_encontrados = set()

    # Percorre cada ave da lista.
    for posicao, ave in enumerate(aves, start=1):

        # Tenta usar o nome popular para identificar a ave.
        # Se não houver nome, usa a posição na lista.
        identificacao = ave.get(
            "nome_popular",
            f"ave na posição {posicao}"
        )

        # Verifica se todos os campos obrigatórios existem.
        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in ave:
                problemas.append(
                    f"{identificacao}: campo ausente '{campo}'"
                )

        # Verifica se o ID já apareceu antes.
        id_ave = ave.get("id")

        if id_ave in ids_encontrados:
            problemas.append(
                f"{identificacao}: ID duplicado '{id_ave}'"
            )
        else:
            ids_encontrados.add(id_ave)

        # Verifica se o campo midia é um dicionário.
        midia = ave.get("midia")

        if not isinstance(midia, dict):
            problemas.append(
                f"{identificacao}: campo 'midia' deveria ser um dicionário"
            )
        else:
            # Verifica se as chaves esperadas existem dentro de midia.
            for campo_midia in CAMPOS_MIDIA:
                if campo_midia not in midia:
                    problemas.append(
                        f"{identificacao}: campo de mídia ausente "
                        f"'{campo_midia}'"
                    )

        # Valida campos numéricos importantes.
        if "comprimento_cm" in ave and not isinstance(
            ave.get("comprimento_cm"),
            (int, float)
        ):
            problemas.append(
                f"{identificacao}: comprimento_cm deveria ser número"
            )

        if "peso_g" in ave and not isinstance(
            ave.get("peso_g"),
            (int, float)
        ):
            problemas.append(
                f"{identificacao}: peso_g deveria ser número"
            )

        if "indice_conservacao" in ave and not isinstance(
            ave.get("indice_conservacao"),
            int
        ):
            problemas.append(
                f"{identificacao}: indice_conservacao deveria ser inteiro"
            )

        # Valida nome popular vazio.
        if str(ave.get("nome_popular", "")).strip() == "":
            problemas.append(
                f"{identificacao}: nome_popular não pode estar vazio"
            )

    return problemas