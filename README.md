Name: Edara Bharath Kalyan Reddy
Date: 11-11-2025
Project Description:
DockerFile execution process:
# Hello Python Docker
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
