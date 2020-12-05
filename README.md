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

Você pode instalar também utilizando o pip, contudo, indicamos o poetry como mostrado acima
````bash
$ python -m venv .venv
$ pip install -r requirements.txt  
$ source .venv/bin/activate
$ cp local.env .env
$ pre-commit install
````

## Testes e cobertura
Para rodar os testes, execute:
```bash
$ make test
```
Para rodar os testes e visualizar o relatório de cobertura, execute:
```bash
$ make test-cov
```
## Exercício 01
Para testar o exercício 01
Digite no terminal
```bash
python
```
Em seguida digite no REPL do python
```python
>>> from vivo.ex01.get_an import get_an
>>> get_an([1,2,3,5,5,5,5])
```
Você receberá um json como resposta
```json
'{0: 0, 1: 1, 2: 1, 3: 1, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}'
```
## Exercício 02
Você pode subir a API com este comando no terminal
```bash
make ex02
```
ou
````python
python vivo/ex02/app.py
````
Em seguida basta enviar uma chamada GET para o localhost port 5000
Com uma lista de números como parâmetro
```
http://localhost:5000/?lista=1,5,5,5,5
```
Você receberá um json na resposta
```json
{
  0: 0,
  1: 1,
  2: 0,
  3: 0,
  4: 0,
  5: 4,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0,
  11: 0,
  12: 0,
  13: 0,
  14: 0,
  15: 0
}
```
O nome do parâmetro não importa, bem como é
possível enviar mais de um parâmetro, neste caso as listas serão juntadas
```
http://localhost:5000/?wincenty=1,5,5,5,5&lech=1,1,1,1,0,0,0,0
```
Neste caso o retorno será este
````json
{
  0: 4,
  1: 5,
  2: 0,
  3: 0,
  4: 0,
  5: 4,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0,
  11: 0,
  12: 0,
  13: 0,
  14: 0,
  15: 0
}
````
## Exercício 03
Para executar o exercício 02
Digite no terminal
```bash
python
```
Em seguida no REPL do python digite
```python
>>> from vivo.ex03.super_heroes import orchestrator
>>> orchestrator('./tests/ex03/example/log.csv')
```
Você receberá esta resposta
```json
'[{"Codigo":"033","Tempo Volta":"04:33:00","Nº Volta":4,"Nome":"Flash","Velocidade média da volta":43.468,"Melhor Volta":"01:04:02","Posição":1,"Melhor volta da corrida":"00:19:37"},{"Codigo":"023","Tempo Volta":"04:44:42","Nº Volta":4,"Nome":"Sonic","Velocidade média da volta":43.19125,"Melhor Volta":"01:07:36","Posição":2,"Melhor volta da corrida":"00:19:37"},{"Codigo":"002","Tempo Volta":"04:48:53","Nº Volta":4,"Nome":"Mercúrio","Velocidade média da volta":43.62725,"Melhor Volta":"01:04:16","Posição":3,"Melhor volta da corrida":"00:19:37"},{"Codigo":"038","Tempo Volta":"04:51:58","Nº Volta":4,"Nome":"Superman","Velocidade média da volta":44.24575,"Melhor Volta":"01:05:50","Posição":4,"Melhor volta da corrida":"00:19:37"},{"Codigo":"015","Tempo Volta":"05:13:21","Nº Volta":4,"Nome":"PAPALÉGUA","Velocidade média da volta":38.06625,"Melhor Volta":"01:07:11","Posição":5,"Melhor volta da corrida":"00:19:37"},{"Codigo":"011","Tempo Volta":"01:47:16","Nº Volta":3,"Nome":"GATOAJATO","Velocidade média da volta":25.7456666667,"Melhor Volta":"00:19:37","Posição":6,"Melhor volta da corrida":"00:19:37"}]'
```
