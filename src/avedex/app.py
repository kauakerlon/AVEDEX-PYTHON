from src.avedex.catalogo import listar_aves, buscar_aves, tela_detalhes
from src.avedex.comparacao import comparar_aves
from src.avedex.creditos import mostrar_creditos
from src.avedex.dados import carregar_aves
from src.avedex.interface import abertura, exibir_menu_principal
from src.avedex.utils import pausar, mensagem_aviso
from src.avedex.dados import carregar_aves, validar_dataset


def executar():
    # Carrega a lista de aves a partir do JSON.
    aves = carregar_aves()

    # Se a lista estiver vazia, não há o que exibir.
    if not aves:
        mensagem_aviso(
            "Nenhuma ave foi carregada. "
            "Verifique o arquivo do dataset."
        )
        return

    # Valida o conteúdo do dataset.
    problemas = validar_dataset(aves)

    # Se existirem problemas, mostramos todos e encerramos.
    if len(problemas) > 0:
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

    # Se chegou até aqui, os dados passaram pela validação.
    abertura(aves)

    # Depois disso, continua o while do menu principal.
    while True:
        exibir_menu_principal()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_aves(aves)
            pausar()

        elif opcao == "2":
            buscar_aves(aves)
            pausar()

        elif opcao == "3":
            tela_detalhes(aves)
            pausar()

        elif opcao == "4":
            comparar_aves(aves)
            pausar()

        elif opcao == "5":
            mostrar_creditos()
            pausar()

        elif opcao == "0":
            print("Encerrando a AveDex. Até logo!")
            break

        else:
            mensagem_aviso("Opção inválida.")
            pausar()