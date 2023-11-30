from sqlalchemy import Column, Integer, String, Boolean,Table
from database.connection import metadata

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
