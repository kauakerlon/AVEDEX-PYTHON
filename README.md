# AveDex
Catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Funcionalidades atuais
- menu em repetição;
- mensagem personalizada;
- apresentação inicial de uma ave;
- tratamento de opção inválida.
## Testes manuais realizados
- [x] Listagem de aves
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Opção inválida no menu
- [x] Encerramento do programa
## Testes manuais realizados
- [x] Busca por parte do nome popular
- [x] Busca ignorando acentos
- [x] Busca por família
- [x] Busca por ordem
- [x] Busca por dieta
- [x] Busca sem resultados
- [x] Busca com entrada vazia
- [x] Tentativa de abrir ID fora dos resultados
## Testes manuais realizados
- [x] Comparação entre duas aves existentes
- [x] Comparação exibindo família, dieta e habitat
- [x] Comparação exibindo peso e comprimento
- [x] Comparação exibindo status e índice de conservação
- [x] Tratamento de ID inexistente na comparação
- [x] Comparação da mesma ave com ela mesma
- [x] Opção inválida no menu
## Testes de regressão
- [ ] Listar aves
- [ ] Buscar por parte do nome
- [ ] Buscar por família
- [ ] Buscar por ordem
- [ ] Buscar por dieta
- [ ] Ver detalhes por ID
- [ ] Comparar duas aves
- [ ] Tratar ID inexistente
- [ ] Tratar opção inválida no menu
- [ ] Encerrar o programa
## Testes de regressão
- [x] Listar aves
- [x] Buscar por parte do nome
- [x] Buscar por família
- [x] Buscar por ordem
- [x] Buscar por dieta
- [x] Ver detalhes por ID
- [x] Comparar duas aves
- [x] Tratar ID inexistente
- [x] Tratar opção inválida no menu
- [x] Encerrar o programa
# AveDex
A AveDex é um catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Como executar
```bash
python main.py
```
## Estrutura do projeto
- `main.py`: inicia o programa.
- `src/avedex/app.py`: controla o fluxo principal.
- `src/avedex/interface.py`: mostra abertura e menu.
- `src/avedex/dados.py`: carrega o dataset JSON.
- `src/avedex/catalogo.py`: lista, busca e mostra detalhes.
- `src/avedex/comparacao.py`: compara duas aves.
- `src/avedex/creditos.py`: mostra informações e fontes.
- `src/avedex/utils.py`: reúne funções auxiliares.
- `data/avedex_dataset_midias.json`: dados das aves.
## Testes manuais realizados em 03/08
- [x] Execução com `python main.py`
- [x] Carregamento das aves pelo JSON
- [x] Listagem das aves
- [x] Busca textual
- [x] Detalhes por ID
- [x] Comparação entre aves
- [x] Créditos e fontes
- [x] Encerramento do programa
## Como executar
```bash
python avedex.py
```
# AveDex
A AveDex é um catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Funcionalidades
- Listagem de aves
- Busca por nome, família, ordem ou dieta
- Exibição de detalhes por ID
- Comparação entre duas aves
- Dados carregados de arquivo JSON
- Validação defensiva do dataset
- Verificação de ambiente
## Como executar
```bash
python main.py
```
## Instalação das dependências opcionais
```bash
pip install -r requirements.txt
```
## Estrutura do projeto
- `main.py`: ponto de entrada.
- `src/avedex/app.py`: menu e fluxo principal.
- `src/avedex/interface.py`: abertura e menu.
- `src/avedex/catalogo.py`: listagem, busca e detalhes.
- `src/avedex/comparacao.py`: comparação entre aves.
- `src/avedex/dados.py`: carregamento e validação do JSON.
- `src/avedex/ambiente.py`: verificação de dependências.
- `src/avedex/creditos.py`: informações e fontes.
- `src/avedex/utils.py`: funções auxiliares.
- `data/avedex_dataset_midias.json`: dados das aves.
## Testes
Os testes manuais estão documentados em:
`docs/testes_manuais.md`
## Testes defensivos realizados
- [x] JSON carregado corretamente
- [x] Arquivo JSON ausente
- [x] JSON mal formatado
- [x] Campo obrigatório ausente
- [x] ID duplicado
- [x] Campo numérico inválido
- [x] Entrada inválida no ID
- [x] Verificação de ambiente
## Autor
kauã kerlon pinto de paula.
