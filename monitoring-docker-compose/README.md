# Monitoring Stack with Docker Compose

This Docker Compose configuration sets up a simple monitoring stack with the following services:

1. **cAdvisor:**
   - Container for collecting, aggregating, and exporting resource usage information for containers.
   - Exposes metrics at [http://localhost:8080](http://localhost:8080).

2. **Prometheus:**
   - Monitoring and alerting tool
   - Reads metrics from cAdvisor.
   - Configuration file: `prometheus.yml`.

3. **Grafana:**
   - Platform for analytics and monitoring with an integrated dashboard.
   - Connects to Prometheus as a data source.
   - Exposed at [http://localhost:3000](http://localhost:3000) (default credentials: admin/admin).

## How to Use

1. Keep the *(config files)* `prometheus.yml`, `datasources.yml`, `dashboard.json`, and `default.yaml` files to the same directory as your `docker-compose.yml`.
2. Run the monitoring stack:

    ```bash
    docker-compose up -d
    ```

3. Access Grafana at [http://localhost:3000](http://localhost:3000) and log in with the credentials `admin/admin`.
