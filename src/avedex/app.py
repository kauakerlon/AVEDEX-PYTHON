"""Fluxo principal da aplicação AveDex."""

from src.avedex.ambiente import verificar_ambiente
from src.avedex.batalha import batalha_avedex
from src.avedex.catalogo import (
    buscar_aves,
    escolher_ave,
    listar_aves,
    mostrar_ave_aleatoria,
    tela_detalhes,
)
from src.avedex.comparacao import comparar_aves
from src.avedex.creditos import mostrar_creditos
from src.avedex.dados import carregar_aves, validar_dataset
from src.avedex.interface import abertura, exibir_menu_principal
from src.avedex.multimidia import tocar_som, visualizar_imagem
from src.avedex.utils import (
    Cor,
    colorir,
    limpar_tela,
    mensagem_aviso,
    pausar,
)


def selecionar_e_visualizar_imagem(aves):
    """Permite escolher uma ave e chama a visualização de imagem."""
    ave = escolher_ave(
        aves,
        "Escolha uma ave para visualizar a imagem",
    )

    if ave is not None:
        visualizar_imagem(ave)


def selecionar_e_tocar_som(aves):
    """Permite escolher uma ave e chama a reprodução de som."""
    ave = escolher_ave(
        aves,
        "Escolha uma ave para ouvir o som",
    )

    if ave is not None:
        tocar_som(ave)


def executar():
    """Carrega os dados, valida o dataset e mantém o menu em execução."""
    aves = carregar_aves()

    if not aves:
        mensagem_aviso(
            "Nenhuma ave foi carregada. "
            "Verifique o arquivo do dataset."
        )
        return

    problemas = validar_dataset(aves)

    if problemas:
        mensagem_aviso(
            "Foram encontrados problemas no dataset:"
        )

        for problema in problemas:
            print(f"- {problema}")

        print()

        mensagem_aviso(
            "Corrija o arquivo JSON antes de continuar."
        )
        return

    abertura(aves)
    pausar()

    while True:
        limpar_tela()
        exibir_menu_principal()

        opcao = input(
            colorir(
                "Escolha uma opção: ",
                Cor.CIANO,
            )
        ).strip()

        if opcao == "1":
            listar_aves(aves)
            pausar()

        elif opcao == "2":
            buscar_aves(aves)
            pausar()

        elif opcao == "3":
            mostrar_ave_aleatoria(aves)
            pausar()

        elif opcao == "4":
            tela_detalhes(aves)
            pausar()

        elif opcao == "5":
            comparar_aves(aves)
            pausar()

        elif opcao == "6":
            batalha_avedex(aves)
            pausar()

        elif opcao == "7":
            selecionar_e_visualizar_imagem(aves)
            pausar()

        elif opcao == "8":
            selecionar_e_tocar_som(aves)
            pausar()

        elif opcao == "9":
            verificar_ambiente()
            pausar()

        elif opcao == "10":
            mostrar_creditos()
            pausar()

        elif opcao == "0":
            limpar_tela()
            print(
                colorir(
                    "Obrigado por usar a AveDex!",
                    Cor.VERDE,
                )
            )
            break

        else:
            mensagem_aviso("Opção inválida.")
            pausar()