# ETL SCRIPT #
## introduction ##
This is a small Flask web application for data analysis using Plotly and Pandas. The app provides the following features:

### File Structure ###
~~~ bash
dashboard/
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── database.py -> database connection
│   ├── routes.py -> app routes
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── favicon.png
│   └── templates
│       ├── base.html -> base extended template
│       ├── components
│       │   └── navbar.html -> navbar component
│       ├── index.html -> index template
│       └── plot.html -> template for visualization
├── app.py
├── gunicorn_config.py -> gUnicorn configuration file
└── requirements.txt
~~~

## 1. Home Page
- Nothing Here.

## 2. Correlation Analysis
- Visit `/correlation` to perform correlation analysis on the dataset.
- The page displays a correlation matrix heatmap for numerical columns in the dataset.

## 3. X-Y Analysis
- Access `/x-y-analysis` to conduct X-Y analysis with an interactive scatter plot.
- Choose X and Y axes dynamically and visualize the relationship between them.

## 4. Capacity Analysis
- Explore `/capacity` to analyze *"total capacity / Arrondissement"*
- The page includes a bar chart showing the total capacity grouped by the arrondissement_communes.

