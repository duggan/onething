import argparse
import json
from datetime import date
import os

"""
Creates our raw entry
"""

# Argument parsing
parser = argparse.ArgumentParser(description='one thing / create')
parser.add_argument('-v','--verb', help='read|watch|see', required=True)
parser.add_argument('-t','--title', help='Title for the URL', required=True)
parser.add_argument('-u','--url', help='The URL', required=True)
parser.add_argument('-c','--contributor', help='Contributed this entry', required=False)
parser.add_argument('-a','--contributor-url', help='Contributor URL', required=False)
args = vars(parser.parse_args())

# Build the JSON object
entry = json.dumps(args)

# Today's date
d = date.today()
month_path = d.strftime("_entries/%Y/%m")
current = d.strftime("_entries/%Y/%m/%d.json")

if not os.path.exists(month_path):
   os.makedirs(month_path)

with open(current, "wb+") as f:
   f.write(entry)

print current
