# ETL to Data visualization dashboard & Container Monitoring #
## Tech Stack  
**Dashboard:** Python, Flask, Plotly,SqlAlchemy, ...

**ETL Script:** Python, Pandas, numpy,SqlAlchemy, ...

**Others:** Bash, Docker, SQL


*Check requirements.txt in /dashboard and /etl_pipeline for more detailed dependencies*

## Requirement
- git
- docker
- bash
## Run Locally  
Clone the project  

~~~bash  
  git clone https://github.com/khalilrez/etl_devops.git
~~~

Go to the project directory  

~~~bash  
  cd etl_devops
~~~

OPTION 1 : Run full project (ETL + Dashboard + Monitoring System)  

~~~bash  
./automated-workflow/pipeline.sh
~~~
*(commented while loop for 24h re-extraction of data)*

OPTION 2 : Run Docker compose files and Bash script individually  

~~~bash  
cd etl-docker-compose
docker compose up -d
cd ..
./index_bash_script.sh
cd monitoring-docker-compose
docker compose up -d
~~~  

## Usage
DataViz Dashboard : localhost:8001

Monitoring Processes:
- cAdvisor : localhost:8080
- Prometheus: localhost:9090
- Grafana: localhost:3000

~~~
grafana credentials:
admin@admin
mysql credentials:
root@quantify
~~~  

## Features that could be added
- Testing For ETL script
- Map Visualization through Latitude and Longitude data