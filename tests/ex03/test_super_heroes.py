from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

from vivo.ex03.super_heroes import bonus_info
from vivo.ex03.super_heroes import df_all_columns
from vivo.ex03.super_heroes import get_exercise_result_info
from vivo.ex03.super_heroes import orchestrator
from vivo.ex03.super_heroes import parse_time_to_str
from vivo.ex03.super_heroes import remove_duplicated_name
from vivo.ex03.super_heroes import total_time_laps


@pytest.fixture
def file_path():
    parent_path = Path(__file__).parents[0]
    return f'{parent_path}/example/log_bug.csv'


@pytest.fixture
def expected_final_dataframe():
    return pd.DataFrame(
        [
            {
                'Codigo': '033',
                'Tempo Volta': '04:33:00',
                'Nº Volta': 4,
                'Nome': 'Flash',
                'Velocidade média da volta': 43.468,
                'Melhor Volta': '01:04:02',
                'Posição': 1,
                'Melhor volta da corrida': '00:19:37',
            },
            {
                'Codigo': '023',
                'Tempo Volta': '04:44:42',
                'Nº Volta': 4,
                'Nome': 'Sonic',
                'Velocidade média da volta': 43.19125,
                'Melhor Volta': '01:07:36',
                'Posição': 2,
                'Melhor volta da corrida': '00:19:37',
            },
            {
                'Codigo': '002',
                'Tempo Volta': '04:48:53',
                'Nº Volta': 4,
                'Nome': 'Mercúrio',
                'Velocidade média da volta': 43.62725,
                'Melhor Volta': '01:04:16',
                'Posição': 3,
                'Melhor volta da corrida': '00:19:37',
            },
            {
                'Codigo': '038',
                'Tempo Volta': '04:51:58',
                'Nº Volta': 4,
                'Nome': 'Superman',
                'Velocidade média da volta': 44.24575,
                'Melhor Volta': '01:05:50',
                'Posição': 4,
                'Melhor volta da corrida': '00:19:37',
            },
            {
                'Codigo': '015',
                'Tempo Volta': '05:13:21',
                'Nº Volta': 4,
                'Nome': 'PAPALÉGUA',
                'Velocidade média da volta': 38.06625,
                'Melhor Volta': '01:07:11',
                'Posição': 5,
                'Melhor volta da corrida': '00:19:37',
            },
            {
                'Codigo': '011',
                'Tempo Volta': '01:47:16',
                'Nº Volta': 3,
                'Nome': 'GATOAJATO',
                'Velocidade média da volta': 25.7456666667,
                'Melhor Volta': '00:19:37',
                'Posição': 6,
                'Melhor volta da corrida': '00:19:37',
            },
        ]
    )


@pytest.fixture
def expected_orchestrator_json(expected_final_dataframe):
    return expected_final_dataframe.to_json(orient='records', force_ascii=False)


@pytest.fixture
def expected_df_all_columns():
    expected_result = pd.DataFrame(
        [
            {
                'Hora': '23:49:08.277',
                'Super-Heroi': '038–Superman',
                'Nº Volta': 1,
                'Tempo Volta': '01:16:12',
                'Velocidade média da volta': 44.275,
                'Codigo': '038',
                'Nome': 'Superman',
            },
            {
                'Hora': '23:49:10.858',
                'Super-Heroi': '033–Flash',
                'Nº Volta': 1,
                'Tempo Volta': '01:09:52',
                'Velocidade média da volta': 43.243,
                'Codigo': '033',
                'Nome': 'Flash',
            },
            {
                'Hora': '23:49:11.075',
                'Super-Heroi': '002–Mercúrio',
                'Nº Volta': 1,
                'Tempo Volta': '01:05:48',
                'Velocidade média da volta': 43.408,
                'Codigo': '002',
                'Nome': 'Mercúrio',
            },
            {
                'Hora': '23:49:12.667',
                'Super-Heroi': '023–Sonic',
                'Nº Volta': 1,
                'Tempo Volta': '01:10:54',
                'Velocidade média da volta': 43.202,
                'Codigo': '023',
                'Nome': 'Sonic',
            },
            {
                'Hora': '23:49:30.976',
                'Super-Heroi': '015–PAPALÉGUA',
                'Nº Volta': 1,
                'Tempo Volta': '01:25:36',
                'Velocidade média da volta': 35.47,
                'Codigo': '015',
                'Nome': 'PAPALÉGUA',
            },
            {
                'Hora': '23:50:11.447',
                'Super-Heroi': '038–Superman',
                'Nº Volta': 2,
                'Tempo Volta': '01:05:50',
                'Velocidade média da volta': 44.053,
                'Codigo': '038',
                'Nome': 'Superman',
            },
            {
                'Hora': '23:50:14.860',
                'Super-Heroi': '033–Flash',
                'Nº Volta': 2,
                'Tempo Volta': '01:04:02',
                'Velocidade média da volta': 43.48,
                'Codigo': '033',
                'Nome': 'Flash',
            },
            {
                'Hora': '23:50:15.057',
                'Super-Heroi': '002–Mercúrio',
                'Nº Volta': 2,
                'Tempo Volta': '01:19:22',
                'Velocidade média da volta': 43.493,
                'Codigo': '002',
                'Nome': 'Mercúrio',
            },
            {
                'Hora': '23:50:17.472',
                'Super-Heroi': '023–Sonic',
                'Nº Volta': 2,
                'Tempo Volta': '01:17:25',
                'Velocidade média da volta': 42.941,
                'Codigo': '023',
                'Nome': 'Sonic',
            },
            {
                'Hora': '23:50:37.987',
                'Super-Heroi': '015–PAPALÉGUA',
                'Nº Volta': 2,
                'Tempo Volta': '01:07:11',
                'Velocidade média da volta': 41.528,
                'Codigo': '015',
                'Nome': 'PAPALÉGUA',
            },
            {
                'Hora': '23:51:14.216',
                'Super-Heroi': '038–Superman',
                'Nº Volta': 3,
                'Tempo Volta': '01:14:49',
                'Velocidade média da volta': 44.334,
                'Codigo': '038',
                'Nome': 'Superman',
            },
            {
                'Hora': '23:51:18.576',
                'Super-Heroi': '033–Flash',
                'Nº Volta': 3,
                'Tempo Volta': '01:14:56',
                'Velocidade média da volta': 43.675,
                'Codigo': '033',
                'Nome': 'Flash',
            },
            {
                'Hora': '23:51:19.044',
                'Super-Heroi': '002–Mercúrio',
                'Nº Volta': 3,
                'Tempo Volta': '01:19:27',
                'Velocidade média da volta': 43.49,
                'Codigo': '002',
                'Nome': 'Mercúrio',
            },
            {
                'Hora': '23:51:21.759',
                'Super-Heroi': '023–Sonic',
                'Nº Volta': 3,
                'Tempo Volta': '01:08:47',
                'Velocidade média da volta': 43.287,
                'Codigo': '023',
                'Nome': 'Sonic',
            },
            {
                'Hora': '23:51:46.691',
                'Super-Heroi': '015–PAPALÉGU',
                'Nº Volta': 3,
                'Tempo Volta': '01:19:44',
                'Velocidade média da volta': 40.504,
                'Codigo': '015',
                'Nome': 'PAPALÉGU',
            },
            {
                'Hora': '23:52:01.796',
                'Super-Heroi': '011–GATOAJATO',
                'Nº Volta': 1,
                'Tempo Volta': '00:36:15',
                'Velocidade média da volta': 13.169,
                'Codigo': '011',
                'Nome': 'GATOAJATO',
            },
            {
                'Hora': '23:52:17.003',
                'Super-Heroi': '038–Superman',
                'Nº Volta': 4,
                'Tempo Volta': '01:15:07',
                'Velocidade média da volta': 44.321,
                'Codigo': '038',
                'Nome': 'Superman',
            },
            {
                'Hora': '23:52:22.586',
                'Super-Heroi': '033–Flash',
                'Nº Volta': 4,
                'Tempo Volta': '01:04:10',
                'Velocidade média da volta': 43.474,
                'Codigo': '033',
                'Nome': 'Flash',
            },
            {
                'Hora': '23:52:22.120',
                'Super-Heroi': '002–Mercúrio',
                'Nº Volta': 4,
                'Tempo Volta': '01:04:16',
                'Velocidade média da volta': 44.118,
                'Codigo': '002',
                'Nome': 'Mercúrio',
            },
            {
                'Hora': '23:52:25.975',
                'Super-Heroi': '023–Sonic',
                'Nº Volta': 4,
                'Tempo Volta': '01:07:36',
                'Velocidade média da volta': 43.335,
                'Codigo': '023',
                'Nome': 'Sonic',
            },
            {
                'Hora': '23:53:06.741',
                'Super-Heroi': '015–PAPALÉGUA',
                'Nº Volta': 4,
                'Tempo Volta': '01:20:50',
                'Velocidade média da volta': 34.763,
                'Codigo': '015',
                'Nome': 'PAPALÉGUA',
            },
            {
                'Hora': '23:53:39.660',
                'Super-Heroi': '011–GATOAJATO',
                'Nº Volta': 2,
                'Tempo Volta': '00:51:24',
                'Velocidade média da volta': 28.435,
                'Codigo': '011',
                'Nome': 'GATOAJATO',
            },
            {
                'Hora': '23:54:57.757',
                'Super-Heroi': '011–GATOAJATO',
                'Nº Volta': 3,
                'Tempo Volta': '00:19:37',
                'Velocidade média da volta': 35.633,
                'Codigo': '011',
                'Nome': 'GATOAJATO',
            },
        ]
    )
    expected_result['Tempo Volta'] = pd.to_timedelta(expected_result['Tempo Volta'])
    return expected_result


@pytest.fixture
def expected_df_time(expected_df_all_columns):
    df = pd.DataFrame(
        {
            'Tempo Volta': {
                '002': '04:48:53',
                '011': '01:47:16',
                '015': '05:13:21',
                '023': '04:44:42',
                '033': '04:33:00',
                '038': '04:51:58',
            }
        }
    )
    df.index.name = 'Codigo'
    df['Tempo Volta'] = pd.to_timedelta(df['Tempo Volta'])
    return df


@pytest.fixture
def expected_df_lap(expected_df_all_columns):
    df = pd.DataFrame(
        {'Nº Volta': {'002': 4, '011': 3, '015': 4, '023': 4, '033': 4, '038': 4}}
    )
    df.index.name = 'Codigo'
    return df


@pytest.fixture
def expected_df_hero_lap(expected_df_all_columns):
    df = pd.DataFrame(
        {
            'Melhor Volta': {
                '002': '01:04:16',
                '011': '00:19:37',
                '015': '01:07:11',
                '023': '01:07:36',
                '033': '01:04:02',
                '038': '01:05:50',
            }
        }
    )
    df['Melhor Volta'] = pd.to_timedelta(df['Melhor Volta'])
    df.index.name = 'Codigo'
    return df


@pytest.fixture
def expected_df_mean_velocity(expected_df_all_columns):
    df = pd.DataFrame(
        {
            'Velocidade média da volta': {
                '002': 43.627250000000004,
                '011': 25.745666666666665,
                '015': 38.06625,
                '023': 43.191250000000004,
                '033': 43.467999999999996,
                '038': 44.24575,
            }
        }
    )
    df.index.name = 'Codigo'
    return df


@pytest.fixture
def expected_df_names(expected_df_all_columns):
    return pd.DataFrame(
        {
            'Codigo': {0: '038', 1: '033', 2: '002', 3: '023', 4: '015', 15: '011'},
            'Nome': {
                0: 'Superman',
                1: 'Flash',
                2: 'Mercúrio',
                3: 'Sonic',
                4: 'PAPALÉGUA',
                15: 'GATOAJATO',
            },
        }
    )


@patch('vivo.ex03.super_heroes.get_exercise_result_info')
@patch('vivo.ex03.super_heroes.remove_duplicated_name')
@patch('vivo.ex03.super_heroes.total_time_laps')
@patch('vivo.ex03.super_heroes.bonus_info')
@patch('vivo.ex03.super_heroes.df_all_columns')
def test_orchestrator(
    mock_df_all_columns,
    mock_bonus_info,
    mock_total_time_laps,
    mock_remove_duplicated_name,
    mock_get_exercise_result_info,
    expected_final_dataframe,
    expected_orchestrator_json,
    file_path,
):
    df_all_columns_return = 'df return'

    mock_df_all_columns.return_value = 'first df'
    mock_bonus_info.return_value = ('df_bonus_best_hero_lap', 'df_mean_vel')
    mock_total_time_laps.return_value = ('df_total laps', 'df_total_time')
    mock_remove_duplicated_name.return_value = 'df_names'
    mock_df_all_columns.return_value = df_all_columns_return
    mock_get_exercise_result_info.return_value = expected_final_dataframe

    result = orchestrator(file_path)

    assert result == expected_orchestrator_json
    mock_df_all_columns.assert_called_once_with(file_path)
    mock_bonus_info.assert_called_once_with(df_all_columns_return)
    mock_total_time_laps.assert_called_once_with(df_all_columns_return)
    mock_remove_duplicated_name.assert_called_once_with(df_all_columns_return)
    mock_get_exercise_result_info.assert_called_once_with(
        'df_bonus_best_hero_lap',
        'df_mean_vel',
        'df_names',
        'df_total laps',
        'df_total_time',
    )


def test_df_all_columns(file_path, expected_df_all_columns):
    result = df_all_columns(file_path)
    pd.testing.assert_frame_equal(result, expected_df_all_columns)


def test_total_time_laps(expected_df_all_columns, expected_df_time, expected_df_lap):
    laps_result, time_result = total_time_laps(expected_df_all_columns)
    pd.testing.assert_frame_equal(time_result, expected_df_time)
    pd.testing.assert_frame_equal(laps_result, expected_df_lap)


def test_bonus_info(
    expected_df_all_columns, expected_df_hero_lap, expected_df_mean_velocity
):
    hero_lap_result, mean_vel_result = bonus_info(expected_df_all_columns)
    pd.testing.assert_frame_equal(hero_lap_result, expected_df_hero_lap)
    pd.testing.assert_frame_equal(mean_vel_result, expected_df_mean_velocity)


def test_remove_duplicated_name(expected_df_all_columns, expected_df_names):
    result = remove_duplicated_name(expected_df_all_columns)
    pd.testing.assert_frame_equal(result, expected_df_names)


def test_get_exercise_result_info(
    expected_final_dataframe,
    expected_df_hero_lap,
    expected_df_mean_velocity,
    expected_df_names,
    expected_df_lap,
    expected_df_time,
):
    result = get_exercise_result_info(
        expected_df_hero_lap,
        expected_df_mean_velocity,
        expected_df_names,
        expected_df_lap,
        expected_df_time,
    )
    pd.testing.assert_frame_equal(result, expected_final_dataframe)


def test_parse_time_to_str():
    time = '0 days 12:12:00'
    result = parse_time_to_str(time)
    assert result == '12:12:00'
