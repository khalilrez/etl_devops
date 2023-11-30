#!/bin/bash

MYSQL_CONTAINER_NAME="quantify-mysql"
MYSQL_USERNAME="quantify"
MYSQL_PASSWORD="quantify"

SQL_SCRIPT_PATH="index_creation.sql"

docker exec -i $MYSQL_CONTAINER_NAME mysql -u $MYSQL_USERNAME -p$MYSQL_PASSWORD < $SQL_SCRIPT_PATH
