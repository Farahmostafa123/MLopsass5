import mlflow
import random
import os

mlflow.set_experiment("mlops-assignment")

with mlflow.start_run() as run:
    accuracy = random.uniform(0.7, 0.95)  # simulate accuracy

    mlflow.log_metric("accuracy", accuracy)

    print(f"Accuracy: {accuracy}")
    print(f"Run ID: {run.info.run_id}")

    # Save run_id for GitHub Actions
    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)
