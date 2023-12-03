from sqlalchemy import create_engine,Column, Integer, String, MetaData, Table, Boolean

db_password = 'quantify'
db_name = 'quantify'

db_connection_str = f'mysql+mysqlconnector://root:{db_password}@mysql-db:3306/{db_name}?charset=utf8mb4'

engine = create_engine(db_connection_str)
connection = engine.connect()
metadata = MetaData()

