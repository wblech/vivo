import logging

from vivo.config import settings


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)


def get_an(num_list):
    """Algoritmo que receba como entrada um Vetor A[N] em que An ∈ { 0, 1, 2,..., 15 }.
        Devolve uma String indicando a quantidade de vezes que cada An foi encontrado na matriz de bitmap. No caso em que algum elemento não tenha sido encontrado, o algoritmo deve retornar que a quantidade é zero para aquele elemento.
    Args:
        num_list (list): Lista de inteiros do 0 ao 15

    Returns:
        retorna uma string em formato de dicionário com a indicação de quantas vezes cada número aparece na lista
    """
    try:
        record = {expected_num: 0 for expected_num in range(16)}
        for num in num_list:
            if num < 0 or num > 15:
                raise Exception('Number should be between 0 and 15')
            record[num] += 1
        return str(record)
    except Exception as e:
        logger.error(e, exc_info=True)
