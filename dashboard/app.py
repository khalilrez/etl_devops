from flask import Flask, render_template,request
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

app = Flask(__name__)

# Replace with your MySQL database credentials
db_username = 'quantify'
db_password = 'quantify'
db_name = 'quantify'
db_connection_str = f'mysql+mysqlconnector://{db_username}:{db_password}@localhost:3306/{db_name}'
global engine
engine = create_engine(db_connection_str)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correlation')
def correlation():
    # Load the data from MySQL database
    query = 'SELECT * FROM Station'
    df = pd.read_sql(query, engine)
    # Extract numerical columns
    numerical_columns = ['capacity', 'numdocksavailable', 'numbikesavailable', 'mechanical', 'ebike']
    # Calculate correlation matrix
    correlation_matrix = df[numerical_columns].corr()
    fig = px.imshow(correlation_matrix)
    return render_template('plot.html', plot=fig.to_html())

@app.route('/capacity', methods=['GET', 'POST'])
def capacity():
    if request.method == 'POST':
        order_by = request.form.get('order_by')
        filter_by = request.form.get('filter_by')

        query = f'SELECT nom_arrondissement_communes, SUM(capacity) AS total_capacity FROM Station '

        if filter_by:
            query+= f' WHERE nom_arrondissement_communes LIKE "%{filter_by}%" '
        
        query += 'GROUP BY nom_arrondissement_communes '
        if order_by:
            query += f'ORDER BY total_capacity {order_by}'
        df_sorted = pd.read_sql(query, engine)
    else:
        # Load the data from MySQL database
        query = 'SELECT nom_arrondissement_communes, SUM(capacity) AS total_capacity FROM Station GROUP BY nom_arrondissement_communes '
        df_sorted = pd.read_sql(query, engine)

    fig = px.bar(df_sorted, x='nom_arrondissement_communes', y='total_capacity', labels={'nom_arrondissement_communes':'Arrondissement','total_capacity': 'Total Capacity'})

    return render_template('plot.html', plot=fig.to_html())


if __name__ == '__main__':
    app.run(debug=True)
