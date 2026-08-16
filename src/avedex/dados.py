
import json
from pathlib import Path

from src.avedex.utils import mensagem_erro

# __file__ representa o caminho deste arquivo dados.py.
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