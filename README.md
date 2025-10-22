# Repositório de aulas — Fundamentos de Programação e Introdução à I.A.

Este repositório reúne exemplos e exercícios das aulas de:

- Fundamentos de Programação (Python)
- Introdução à Inteligência Artificial

Estrutura principal
-------------------

- `FP/` — Exercícios e scripts de Fundamentos de Programação (laços, condicionais, listas, etc.).
- `IIA/` — Material de Introdução à I.A. e exercícios com NumPy. Dentro de `IIA/numpy aula/` há demos e notebooks.


Como usar (rápido)
------------------

1. Criar e ativar um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux (zsh)
```

2. Instalar dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Rodar o demo NumPy:

```bash
python "IIA/numpy aula/hello_world.py"
```

4. Rodar o teste rápido:

```bash
python "IIA/numpy aula/test_numpy.py"
```

Dicas para VS Code
------------------

- Se o editor mostrar "Import could not be resolved" para `numpy`, selecione o interpretador do projeto (Command Palette → Python: Select Interpreter) e escolha o Python em `.venv/bin/python`.
- Reinicie o servidor de linguagem (Command Palette → Python: Restart Language Server) ou recarregue a janela.
- O repositório contém uma configuração de workspace (`.vscode/settings.json`) apontando para a virtualenv criada em `.venv/`.

Contribuições
-------------

Pull requests são bem-vindos. Para novos notebooks ou exercícios, crie uma pasta com um nome descritivo dentro de `IIA/` ou `FP/`.

Licença
-------

Use conforme as regras da sua instituição. Se quiser, posso adicionar um cabeçalho de licença padrão (MIT, Apache-2.0, etc.).

