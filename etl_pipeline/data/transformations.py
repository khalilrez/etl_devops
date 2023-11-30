# data/transformations.py
import pandas as pd
from datetime import datetime
from unidecode import unidecode

def remove_accents(s):
    return unidecode(s)

def apply_transform(data_frame):
    df=data_frame
    # Convert 'duedate' to datetime
    df['duedate'] = pd.to_datetime(df['duedate'])

    # Extract coordinates from the 'fields.coordonnees_geo' column
    # Extract coordinates from the 'coordonnees_geo' column
    df['longitude'] = df['coordonnees_geo.lon']
    df['latitude'] = df['coordonnees_geo.lat']
    
    boolean_columns = ['is_installed', 'is_renting', 'is_returning']
    df[boolean_columns] = df[boolean_columns].replace({'OUI': True, 'NON': False})
    
    # Apply the function to the 'Name' column
    df['nom_arrondissement_communes'] = df['nom_arrondissement_communes'].apply(remove_accents)

    # Drop the original 'fields.coordonnees_geo' column
    df.drop(columns=['coordonnees_geo.lon'], inplace=True)
    df.drop(columns=['coordonnees_geo.lat'], inplace=True)
    return df

def get_transformed_data(api_records):
    if api_records:
        # Create a DataFrame from the API data
        df = pd.json_normalize(api_records)

        # Transformation phase
        df = apply_transform(df)

        # Extract numerical columns
        numerical_columns = ['capacity', 'numdocksavailable', 'numbikesavailable', 'mechanical', 'ebike']
        # Calculate correlation matrix
        correlation_matrix = df[numerical_columns].corr()

        # Display the transformed DataFrame
        print(df)
        # Display correlation matrix
        print(correlation_matrix)
        today_date = datetime.today().strftime('%Y-%m-%d')

        # Save DataFrame to CSV with today's date in the filename
        df.to_csv(f'data_{today_date}.csv', index=False)
        return df
