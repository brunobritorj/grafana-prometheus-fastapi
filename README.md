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
