import os

for filename in os.listdir("task_3"):
    with open(os.path.join("task_3", filename), 'r') as file:
        text = file.read()
        print(text)