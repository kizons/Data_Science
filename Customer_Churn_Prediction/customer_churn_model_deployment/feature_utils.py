def feature_engineering(X_df):
    X = X_df.copy()
    X[['international_plan', 'voice_mail_plan']] = X[['international_plan', 'voice_mail_plan']].replace({'yes': 1, 'no': 0})
    X['total_minutes'] = X['total_day_minutes'] + X['total_eve_minutes'] + X['total_night_minutes']
    X['total_charge'] = X['total_day_charge'] + X['total_eve_charge'] + X['total_night_charge']
    X['total_calls'] = X['total_day_calls'] + X['total_eve_calls'] + X['total_night_calls']

    X.drop(columns=[
        'total_day_minutes', 'total_eve_minutes', 'total_night_minutes',
        'total_day_charge', 'total_eve_charge', 'total_night_charge',
        'total_day_calls', 'total_eve_calls', 'total_night_calls'
    ], inplace=True)
    return X