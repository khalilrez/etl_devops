# ETL SCRIPT #
## introduction ##
This directory contains a python script divided into three main components : 
- Retrieving data from API (data/api.py)
- Transform retrieved data (data/transformations.py)
- Load data into MySQL database (data/loading.py)

### File Structure ###
~~~ bash
etl_pipeline/ 
├── Dockerfile
├── README.md
├── config
│   └── config.py -> Configuration Variables
├── data
│   ├── __init__.py
│   ├── api.py -> retrieve data from API
│   ├── loading.py -> Load data into MySQL
│   └── transformations.py -> Transformations on data
├── data_2023-12-03.csv
├── database
│   ├── __init__.py
│   ├── connection.py -> Connection to database
│   └── models.py -> Defining the SQL table
├── main.py
└── requirements.txt -> dependencies
~~~

