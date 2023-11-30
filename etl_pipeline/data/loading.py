from sqlalchemy import create_engine
from database.models import station_table
from database.connection import connection


def load_into_database(df):
    station_data = df[[
        'stationcode',  'capacity', 'numdocksavailable',
        'numbikesavailable', 'mechanical', 'ebike','is_installed', 'is_renting', 'is_returning','nom_arrondissement_communes'
    ]].to_dict(orient='records')
    print(station_data[0])
    connection.execute(station_table.insert().values(station_data))
    connection.commit()
