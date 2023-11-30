from sqlalchemy import create_engine,Column, Integer, String, MetaData, Table, Boolean

db_username = 'quantify'
db_password = 'quantify'
db_name = 'quantify'

db_connection_str = f'mysql+mysqlconnector://{db_username}:{db_password}@localhost:3306/{db_name}?charset=utf8mb4'

engine = create_engine(db_connection_str)
connection = engine.connect()
metadata = MetaData()

metadata.create_all(engine)