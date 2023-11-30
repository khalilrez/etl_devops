# database/connection.py
from sqlalchemy import create_engine,Column, Integer, String, MetaData, Table, Boolean

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

metadata.create_all(engine)