# grafana-prometheus-fastapi

It has a docker-compose example to show how to use Prometheus and Grafana to monitor a FastAPI app.

```
├── fastapi                     # FastAPI sample app
|       ├── app
|       ├── requirements.txt
|       └── Dockerfile
├── prometheus                  # Prometheus startup config
|       └── prometheus.yml
├── grafana                     # Grafana startup config
|       ├── password.env
|       ├── datasources.yml
|       ├── dashboards.yml
|       └── dashboard1.json
└── docker-compose.yml          # Docker-compose playbook
```

After running it (```docker-compose up```):
  - FastAPI app (OpenAPI): ```http://localhost/docs```
  - FastAPI exposed metrics: ```http://localhost/metrics```
  - Prometheus: ```http://localhost:9090```
  - Grafana: ```http://localhost:3000```
