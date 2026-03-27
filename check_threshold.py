# Read accuracy from file
with open("accuracy.txt", "r") as f:
    accuracy = float(f.read())

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    raise Exception("a3333333333333Model accuracy below threshold!")
else:
    print("yes yes Model passed threshold")
