class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://quantify:quantify@mysql-db:3306/quantify?charset=utf8mb4'
    API_URL = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?order_by=is_returning%2Cis_renting%2Cis_installed&limit=100'
