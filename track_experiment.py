import mlflow

# Set the tracking URI (can be local file storage)
mlflow.set_tracking_uri("file:./mlruns")

# Start an experiment
mlflow.set_experiment("hello_docker_experiment")

with mlflow.start_run():
    mlflow.log_param("greeting", "Hello, Docker + MLflow")
    mlflow.log_metric("run_count", 1)
    print("MLflow experiment logged successfully!")
