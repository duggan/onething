import argparse
import pickle
import json
import sys

from datetime import date
import os

queue_path = "_queue"

d = date.today()
month_path = d.strftime("_entries/%Y/%m")
current = d.strftime("_entries/%Y/%m/%d.json")

# Pull the queue
with open(queue_path) as f:
   data = pickle.load(f)

if len(data):
   entry = data.pop()
else:
   print "Error: empty queue"
   sys.exit(1)

try:
   if not os.path.exists(month_path):
      os.makedirs(month_path)

   with open(current, "wb+") as f:
      f.write(json.dumps(entry))

   with open(queue_path, "wb+") as f:
      pickle.dump(data, f)
except Exception as e:
   print "Error:", e
   sys.exit(1)

print current
   
