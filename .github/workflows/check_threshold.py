import mlflow

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

client = mlflow.tracking.MlflowClient()

run = client.get_run(run_id)
accuracy = run.data.metrics["accuracy"]

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    raise Exception("a3333333 Model accuracy below threshold")
else:
    print(" yes yes Model passed threshold")
