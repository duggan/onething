import argparse
import pickle
import json

from datetime import date
import os

queue_path = "_queue"

d = date.today()
month_path = d.strftime("_entries/%Y/%m")
current = d.strftime("_entries/%Y/%m/%d.json")

with open(queue_path) as f:
   data = pickle.load(f)

entry = data.pop()

with open(queue_path, "wb+") as f:
   pickle.dump(data, f)

if not os.path.exists(month_path):
   os.makedirs(month_path)

with open(current, "wb+") as f:
   f.write(json.dumps(entry))

print current
   
