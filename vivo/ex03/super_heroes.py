import pandas as pd


def orchestrator(file_path):
    df = df_all_columns(file_path)

    bonus_best_hero_lap, mean_vel = bonus_info(df)

    total_laps, total_time = total_time_laps(df)
    names = remove_duplicated_name(df)

    final = get_exercise_result_info(
        bonus_best_hero_lap, mean_vel, names, total_laps, total_time
    )
    return final.to_json(orient='records', force_ascii=False)


def df_all_columns(file_path):
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
    total_time = pd.DataFrame(df.groupby('Codigo')['Tempo Volta'].sum())
    total_laps = pd.DataFrame(df.groupby('Codigo').count()['Nº Volta'])
    return total_laps, total_time


def bonus_info(df):
    mean_vel = pd.DataFrame(df.groupby(['Codigo']).mean()['Velocidade média da volta'])
    bonus_best_hero_lap = pd.DataFrame(df.groupby('Codigo').min()['Tempo Volta'])
    bonus_best_hero_lap.rename(columns={'Tempo Volta': 'Melhor Volta'}, inplace=True)
    return bonus_best_hero_lap, mean_vel


def remove_duplicated_name(df):
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
    time = str(time)
    time = time.split(' ')
    return f'{time[2]}'


if __name__ == '__main__':
    file = '/Users/Wblech/Desktop/vivo/tests/ex03/example/log_bug.csv'
    teste = orchestrator(file)
    print(teste)
