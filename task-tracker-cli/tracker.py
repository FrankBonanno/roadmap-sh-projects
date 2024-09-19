import json
import os

def load_tasks():
  if not os.path.exists("tasks.json"):
    with open('tasks.json', 'w') as f:
      json.dump([], f)
  with open("tasks.json", "r") as f:
    return json.load(f)
  
def save_tasks(tasks):
  with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)