Name: Edara Bharath Kalyan Reddy
Date: 11-11-2025
Project Description:
DockerFile execution process:
# Hello Python Docker
![Python CI](https://github.com/bharathkalyanreddyedara/devops/actions/workflows/ci.yml/badge.svg)
## Description
A simple Dockerized Python application that prints "Hello, Docker!" on startup.
## Build the Docker image
```bash
docker build -t hello-python .
```
## Run the container
```bash
docker run --rm hello-python
```
### Expected Output:
```
Hello, Docker!
```
## Run with Nomad
1. Ensure Docker and Nomad are installed.
2. Build the Docker image locally:
   ```bash
   docker build -t hello-python .
3. Run the Nomad job:
   ```bash
   nomad job run nomad/hello.nomad

## Monitoring with Loki
1. Start Loki locally using Docker:
   ```bash
   docker run -d --name=loki -p 3100:3100 grafana/loki:2.9.0
2. Forward container logs to Loki:
   ```bash
   docker run --log-driver=loki \
   --log-opt loki-url="http://localhost:3100/loki/api/v1/push" \
   hello-python
   ```
3. View logs:
   Using Docker:
   ```bash
    docker logs hello-python

  Using Loki API:
  ```bash
curl -G "http://localhost:3100/loki/api/v1/query" \
  --data-urlencode 'query={job="docker"}'
```
Or visualize logs in Grafana by adding Loki as a data source.
