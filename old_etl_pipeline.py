''' REFRACTORED INTO STRUCTURED /etl_pipeline PROJECT
import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine,Column, Integer, String, MetaData, Table, Boolean
from unidecode import unidecode



api_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?order_by=is_returning%2Cis_renting%2Cis_installed&limit=100"
# EXTRACT
def get_api_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data.get('results', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# TRANSFORM
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

# LOAD
def load_into_database(df):
    # Replace with your MySQL database credentials
    db_username = 'quantify'
    db_password = 'quantify'
    db_name = 'quantify'

    # Create a database connection string
    db_connection_str = f'mysql+mysqlconnector://{db_username}:{db_password}@localhost:3306/{db_name}?charset=utf8mb4'

    # Create a database engine
    engine = create_engine(db_connection_str)
    connection = engine.connect()
    metadata = MetaData()

    station_table = Table(
        'Station',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('stationcode', Integer),
        Column('capacity', Integer),
        Column('numdocksavailable', Integer),
        Column('numbikesavailable', Integer),
        Column('mechanical', Integer),
        Column('ebike', Integer),
        Column('is_installed', Boolean),
        Column('is_renting', Boolean),
        Column('is_returning', Boolean),
        Column('nom_arrondissement_communes', String(255)),
    )
    metadata.create_all(engine)

    # Insert data into Station table
    station_data = df[[
        'stationcode',  'capacity', 'numdocksavailable',
        'numbikesavailable', 'mechanical', 'ebike','is_installed', 'is_renting', 'is_returning','nom_arrondissement_communes'
    ]].to_dict(orient='records')
    print(station_data[0])
    connection.execute(station_table.insert().values(station_data))
    connection.commit()


api_records = get_api_data(api_url)
df = get_transformed_data(api_records)
load_into_database(df)

'''