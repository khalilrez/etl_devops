# ETL and Monitoring Automated Script

This script automates the setup of an Extract, Transform, Load pipeline and monitoring stack using Docker Compose.

1. **Image Building Phase:**
   - Builds Docker images for ETL script and dashboard.
   - Image names:
     - ETL Script: `khalilrez/etl-script:1.0.0`
     - Dashboard: `khalilrez/gunicorn-etl-dashboard:1.0.0`

2. **Docker-Compose and Scripts Execution:**
   - Runs Docker Compose for the ETL pipeline (`etl-docker-compose/docker-compose.yml`).
   - Executes a bash script (`../index_bash_script.sh`) for indexing.
   - Attempts multiple times with a delay between attempts in case of failure.

3. **Monitoring Stack Setup:**
   - Runs Docker Compose for the monitoring stack (`monitoring-docker-compose/docker-compose.yml`).
   - Utilizes cAdvisor, Prometheus, and Grafana for monitoring.

4. **Periodic Execution:**
   - Contains commented-out code for periodic execution every 24 hours (uncomment if needed).

## Logs:
The script logs errors to `error_log.txt`.

