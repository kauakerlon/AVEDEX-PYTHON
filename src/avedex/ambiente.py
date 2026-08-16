"""Verificação das dependências opcionais usadas pela AveDex."""

import importlib.util

from src.avedex.utils import (
    mensagem_aviso,
    mensagem_sucesso,
    titulo,
)


BIBLIOTECAS = {
    "requests": "baixar imagens e sons da internet",
    "pygame": "reproduzir sons de aves",
    "term_image": "exibir imagens no terminal",
}


def biblioteca_instalada(nome):
    """Informa se um módulo pode ser encontrado no ambiente Python."""
    return importlib.util.find_spec(nome) is not None


def verificar_ambiente():
    """Exibe a situação das bibliotecas usadas pelos recursos de mídia."""
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
    print("O núcleo da AveDex funciona sem essas bibliotecas.")
    print("Imagem, som e download dependem delas.")
    print("Para instalar: pip install -r requirements.txt")