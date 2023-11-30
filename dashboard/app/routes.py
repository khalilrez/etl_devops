
from flask import render_template, request, g
from app import app
import pandas as pd
import plotly.express as px
from app.database import engine

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correlation')
def correlation():
    query = 'SELECT * FROM Station'
    df = pd.read_sql(query, engine)
    numerical_columns = ['capacité', 'nombre_docks_disponibles', 'nombre_vélos_disponibles', 'mécanique', 'vélo_électrique']
    df.rename(columns={
    'capacity': 'capacité',
    'numdocksavailable': 'nombre_docks_disponibles',
    'numbikesavailable': 'nombre_vélos_disponibles',
    'mechanical': 'mécanique',
    'ebike': 'vélo_électrique'
    }, inplace=True)
    correlation_matrix = df[numerical_columns].corr()
    
    fig = px.imshow(correlation_matrix, labels=dict(color="Correlation"))

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
        query = 'SELECT nom_arrondissement_communes, SUM(capacity) AS total_capacity FROM Station GROUP BY nom_arrondissement_communes '
        df_sorted = pd.read_sql(query, engine)

    fig = px.bar(df_sorted, x='nom_arrondissement_communes', y='total_capacity', labels={'nom_arrondissement_communes':'Arrondissement','total_capacity': 'Total Capacity'})

    return render_template('plot.html', plot=fig.to_html())