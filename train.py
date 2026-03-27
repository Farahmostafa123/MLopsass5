import os
import random
accuracy = float(os.getenv("ACCURACY", "0.80"))

# Generate fake run_id
run_id = "run_" + str(random.randint(1000, 9999))

print(f"Accuracy: {accuracy}")
print(f"Run ID: {run_id}")
with open("model_info.txt", "w") as f:
    f.write(run_id)
with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))
