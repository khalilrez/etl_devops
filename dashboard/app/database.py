from sqlalchemy import create_engine

db_username = 'quantify'
db_password = 'quantify'
db_name = 'quantify'
db_connection_str = f'mysql+mysqlconnector://{db_username}:{db_password}@localhost:3306/{db_name}'
global engine
engine = create_engine(db_connection_str)