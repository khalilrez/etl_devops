import pandas as pd
from datetime import datetime
from unidecode import unidecode

def remove_accents(s):
    return unidecode(s)

def apply_transform(data_frame):
    df=data_frame

    df['longitude'] = df['coordonnees_geo.lon']
    df['latitude'] = df['coordonnees_geo.lat']
    
    boolean_columns = ['is_installed', 'is_renting', 'is_returning']
    df[boolean_columns] = df[boolean_columns].replace({'OUI': True, 'NON': False})
    
    df['nom_arrondissement_communes'] = df['nom_arrondissement_communes'].apply(remove_accents)

    df.drop(columns=['coordonnees_geo.lon'], inplace=True)
    df.drop(columns=['coordonnees_geo.lat'], inplace=True)
    return df

def get_transformed_data(api_records):
    if api_records:
        df = pd.json_normalize(api_records)

        df = apply_transform(df)

        numerical_columns = ['capacity', 'numdocksavailable', 'numbikesavailable', 'mechanical', 'ebike']
        correlation_matrix = df[numerical_columns].corr()

        print(df)
        print(correlation_matrix)
        today_date = datetime.today().strftime('%Y-%m-%d')

        df.to_csv(f'data_{today_date}.csv', index=False)
        return df
