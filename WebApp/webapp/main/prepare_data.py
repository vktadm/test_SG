import pandas as pd

def prepare_data():
    df = pd.read_csv('receptions.csv')

    # Преобразование в datetime
    columns_date = ['add_time', 'start_time', 'end_time', 'cancel_time']
    for column in columns_date:
        df[column] = pd.to_datetime(df[column], dayfirst=True, format='mixed')

    # Преобразование в int и str
    colums_str = ['phone', 'personal_account', 'family_account']
    df[colums_str] = df[colums_str].fillna(0.0).astype('int')
    df[colums_str] = df[colums_str].astype('str')

    # Замена отсутствующих значений на ''
    for i in colums_str:
        df.replace('0', '', inplace=True)

    # Удаление комментариев
    del df['card_comment']
    del df['reception_comment']

    # Добавление столбца, считающий для будущих приёмов количество дней до приёма,
    # а для завершенных приёмов – количество дней, прошедших после приёма
    df = df.assign(count_day=(df['start_time'] - pd.Timestamp.now()).dt.days)

    return df

def get_user_receptions(username):
    df = prepare_data()

    receptions = df[df['phone'] == str(username)].sort_values('start_time')
    receptions['num'] = range(len(receptions))

    receptions_list = receptions.to_dict('records')
    return receptions_list
