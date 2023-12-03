#!/bin/bash

MYSQL_CONTAINER_NAME="quantify-mysql"
MYSQL_PASSWORD="quantify"

SQL_FILE_NAME="index_creation.sql"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SQL_PATH="${CURRENT_DIR}/${SQL_FILE_NAME}"

docker exec -i $MYSQL_CONTAINER_NAME mysql -u root -p$MYSQL_PASSWORD < $SQL_PATH
