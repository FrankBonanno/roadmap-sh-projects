import json
import os
from parser import create_parser

"""File Handling"""
# Load tasks from the JSON file
def load_tasks():
  if not os.path.exists("tasks.json"):
    with open('tasks.json', 'w') as f:
      json.dump([], f)
  with open("tasks.json", "r") as f:
    return json.load(f)
# Save tasks to the JSON file
def save_tasks(tasks):
  with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)

"""Set Up Arg Parser"""
parser = create_parser()
args = parser.parse_args()