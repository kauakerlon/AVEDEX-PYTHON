import importlib.util

from src.avedex.utils import (
    titulo,
    mensagem_sucesso,
    mensagem_aviso,
)

BIBLIOTECAS = {
    "requests": "baixar imagens e sons da internet",
    "pygame": "reproduzir sons de aves",
    "term_image": "exibir imagens no terminal",
}


def biblioteca_instalada(nome):
    # find_spec retorna informação da biblioteca se ela estiver instalada.
    return importlib.util.find_spec(nome) is not None


def verificar_ambiente():
    titulo("VERIFICAÇÃO DO AMBIENTE")

    for biblioteca, finalidade in BIBLIOTECAS.items():
        if biblioteca_instalada(biblioteca):
            mensagem_sucesso(
                f"{biblioteca}: instalada - {finalidade}"
            )
        else:
            mensagem_aviso(
                f"{biblioteca}: não instalada - {finalidade}"
            )

    print()
    print("Para instalar todas as dependências opcionais:")
    print("pip install -r requirements.txt")