import logging

import pandas as pd

from vivo.config import settings

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)


def orchestrator(file_path):
    """API que lê o arquivo de log e retorna um json

    Args:
        file_path (str): caminho para o arquivo csv

    Returns:
        json com as informações solicitadas no pdf do exercicio
    """
    try:
        if not file_path.endswith('.csv'):
            raise Exception('Por favor, utilize apenas arquivos .CSV')
        df = df_all_columns(file_path)

        bonus_best_hero_lap, mean_vel = bonus_info(df)

        total_laps, total_time = total_time_laps(df)
        names = remove_duplicated_name(df)

        final = get_exercise_result_info(
            bonus_best_hero_lap, mean_vel, names, total_laps, total_time
        )
    except Exception as e:
        logger.error(e, exc_info=True)
    else:
        return final.to_json(orient='records', force_ascii=False)


def df_all_columns(file_path):
    """Faz a leitura do arquivo CSV e adiciona 2 novas colunas (Codigo e Nome)

    Args:
        file_path (str): recebe o caminho do arquivo csv

    Returns:
         DataFrame com as informações do CSV com mais 2 novas colunas (Codigo e Nome)
    """
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')
    df['Velocidade média da volta'] = df['Velocidade média da volta'].str.replace(
        ',', '.'
    )
    df['Velocidade média da volta'] = df['Velocidade média da volta'].astype(float)
    df['Tempo Volta'] = df['Tempo Volta'].str.replace('.', ':')
    df[['Codigo', 'Nome']] = df['Super-Heroi'].str.split('–', expand=True)
    df['Tempo Volta'] = pd.to_timedelta(df['Tempo Volta'])
    return df


def total_time_laps(df):
    """

    Args:
        df (DataFrame): DataFrame com as informações do CSV mais as colunas Codigo e Nome

    Returns:
       tuple com 2 Dataframe
    """
    total_time = pd.DataFrame(df.groupby('Codigo')['Tempo Volta'].sum())
    total_laps = pd.DataFrame(df.groupby('Codigo').count()['Nº Volta'])
    return total_laps, total_time


def bonus_info(df):
    """

    Args:
        df (DataFrame): DataFrame com as informações do CSV mais as colunas Codigo e Nome

    Returns:
       tuple com 2 Dataframe
    """
    mean_vel = pd.DataFrame(df.groupby(['Codigo']).mean()['Velocidade média da volta'])
    bonus_best_hero_lap = pd.DataFrame(df.groupby('Codigo').min()['Tempo Volta'])
    bonus_best_hero_lap.rename(columns={'Tempo Volta': 'Melhor Volta'}, inplace=True)
    return bonus_best_hero_lap, mean_vel


def remove_duplicated_name(df):
    """

    Args:
        df: DataFrame com as informações do CSV mais as colunas Codigo e Nome

    Returns:
        Dataframe com as colunas Codigo e Nome sem duplicidade
    """
    names = pd.DataFrame(df.drop_duplicates(subset=['Codigo']))
    names.drop(
        labels=[
            'Hora',
            'Super-Heroi',
            'Nº Volta',
            'Tempo Volta',
            'Velocidade média da volta',
        ],
        axis=1,
        inplace=True,
    )
    return names


def get_exercise_result_info(
    bonus_best_hero_lap, mean_vel, names, total_laps, total_time
):
    """

    Args:
        bonus_best_hero_lap (Dataframe):
        mean_vel (Dataframe):
        names (Dataframe):
        total_laps (Dataframe):
        total_time (Dataframe):

    Returns:
        DataFrame com as informações solicitadas pelo exercício Posição de Chegada, Código do Super-herói, Nome Super-herói, Quantidade de Voltas Completadas e Tempo Total de Prova. 1. Descobrir a melhor volta de cada super-herói. 2. Descobrir a melhor volta da corrida. 3. Calcular a velocidade média de cada super-herói durante toda a corrida.
    """
    final = total_time.merge(total_laps, on='Codigo')
    final = final.merge(names, on='Codigo', how='left')
    final = final.merge(mean_vel, on='Codigo', how='left')
    final = final.merge(bonus_best_hero_lap, on='Codigo', how='left')
    final = final.sort_values(['Nº Volta', 'Tempo Volta'], ascending=[False, True])
    final['Tempo Volta'] = final['Tempo Volta'].map(parse_time_to_str)
    final['Melhor Volta'] = final['Melhor Volta'].map(parse_time_to_str)
    final = final.reset_index(drop=True)
    final['Posição'] = final.index + 1
    final['Melhor volta da corrida'] = final['Melhor Volta'].min()
    return final


def parse_time_to_str(time):
    """Recebe uma string em formato timedelta '0 days 12:12:00'
    e retorna apenas o horário 12:12:00

    Args:
        time (string): Uma dtring em formato timedelta '0 days 12:12:00'

    Returns:
        string com apenas a informação do horário '00:00:00'
    """
    time = str(time)
    time = time.split(' ')
    return f'{time[2]}'
