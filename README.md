# VIVO
[![VIVO](https://circleci.com/gh/wblech/vivo.svg?style=svg)](https://app.circleci.com/pipelines/github/wblech/vivo)

Resolução de exercicios referente ao processo seletivo da vivo
O exercício encontra-se na pasta *exercicio*
## Pré-requisitos
- Python3.8 ou maior (Utilize o [Pyenv](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation) para gerenciar multiplas versões)
- [Poetry](https://python-poetry.org/docs/)
## Instalação
Execute os comandos abaixo para configurar o ambiente virtual e instalar as dependências:
```bash
$ python -m venv .venv
$ poetry install
$ poetry shell
$ cp local.env .env
$ pre-commit install
```
## Testes e cobertura
Para rodar os testes, execute:
```bash
$ make test
```
Para rodar os testes e visualizar o relatório de cobertura, execute:
```bash
$ make test-cov
```
