#!/bin/bash

LOG_FILE="error_log.txt"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INDEXING_FILE="${CURRENT_DIR}/../index_bash_script.sh"
ETL_COMPOSE_FILE="${CURRENT_DIR}/../etl-docker-compose/docker-compose.yml"
MONITORING_COMPOSE_FILE="${CURRENT_DIR}/../monitoring-docker-compose/docker-compose.yml"
SQL_SCRIPT_PATH="${CURRENT_DIR}/../index_creation.sql"




log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: $1" >> "$LOG_FILE"
}

run_docker_compose() {
    echo "Running docker-compose..."
    docker compose -f "${ETL_COMPOSE_FILE}" down
    docker compose -f "${ETL_COMPOSE_FILE}" up -d
    if [ $? -ne 0 ]; then
        log_error "Failed to run ETL docker-compose."
    fi
}

run_bash_script() {
    echo "Running bash script..."
    bash "${INDEXING_FILE}"
    return $?
}
run_monitoring_docker_compose() {
    echo "Running monitoring containers..."
    docker compose -f "${MONITORING_COMPOSE_FILE}" up -d
    if [ $? -ne 0 ]; then
        log_error "Failed to run monitoring docker-compose."
    fi
}
build_dashboard_image(){
    echo "Building Dashboard Image..."
    cd ${CURRENT_DIR}/..
    pwd
    cd dashboard
    docker build -t khalilrez/gunicorn-etl-dashboard:1.0.0 .
    if [ $? -ne 0 ]; then
        log_error "Fail to build dashboard image."
    fi
}
build_etl_script_image(){
    echo "Building Dashboard Image..."
    cd ${CURRENT_DIR}/..
    pwd
    cd etl_pipeline
    docker build -t khalilrez/etl-script:1.0.0 .
    if [ $? -ne 0 ]; then
        log_error "Fail to build ETL script image."
    fi
}

# Main
echo "Starting script..."

echo "********************************************************"
echo "************* Image Building Phase Started *************"
echo "********************************************************"
build_etl_script_image
build_dashboard_image
echo "********************************************************"
echo "************* Image Building Phase Ended *************"
echo "********************************************************"
echo "                                                         "
echo "********************************************************"
echo "******** Running Docker-Compose and Scripts ************"
echo "********************************************************"
run_docker_compose

MAX_ATTEMPTS=6
attempts=0

while [ $attempts -lt $MAX_ATTEMPTS ]; do
    ((attempts++))
    echo "Attempt $attempts ..."
    run_bash_script "$SQL_SCRIPT_PATH"
    if [ $? -eq 0 ]; then
        echo "Script executed successfully."
        break
    else
        log_error "Attempt $attempts failed."
        echo "10s before next attempt ..."
        sleep 5s
        echo "5s before next attempt ..."
        sleep 4s
        echo "1s before next attempt ..."
        sleep
    fi
done

run_monitoring_docker_compose

echo "Done."


<< EOF 

while true; do
    echo "Sleep for 24 hours..."
    sleep 24h
    echo "ETL every 24 hours..."
    run_docker_compose
done
EOF