# Monitoring
## Prerequisites
* There are [troubles with accessing docker logs](https://stackoverflow.com/questions/48180981/docker-container-log-file-not-found-on-mac/48183300#48183300) on MacOS , so I decided to configure Ubuntu20.04 based VM on [AWS](https://aws.amazon.com).
* [docker v20.10.8](https://docs.docker.com/engine/install/ubuntu/)
* [docker-compose v1.29.2](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)

## Screenshots
![Prometheus targets](images/prometheus-targets.png)

![Grafana Loki Dashboard](images/prometheus-loki.png)

![Grafana Prometheus Dashboard](images/prometheus-prometheus.png)

![App Metrics](images/app-metrics.png)

![App in Prometheus](images/app-prom.png)

![Prometheus in Prometheus](images/prom-prom.png)

![Grafana in Prometheus](images/grafana-prom.png)

![Loki in Prometheus](images/loki-prom.png)