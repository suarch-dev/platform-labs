import os

file_path = "/app/data/counter.txt"

os.makedirs("/app/data", exist_ok=True)

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        count = int(f.read())
else:
    count = 0

count += 1
with open(file_path, "w") as f:
    f.write(str(count))

print(f"This script has been executed {count} times.")
