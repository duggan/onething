import argparse
import pickle
import os
from datetime import date

# Argument parsing
parser = argparse.ArgumentParser(description='one thing / create')
parser.add_argument('-v','--verb', help='read|watch|see', required=True)
parser.add_argument('-t','--title', help='Title for the URL', required=True)
parser.add_argument('-u','--url', help='The URL', required=True)
parser.add_argument('-c','--contributor', help='Contributed this entry', required=False)
parser.add_argument('-a','--contributor-url', help='Contributor URL', required=False)
args = vars(parser.parse_args())

queue_path = "_queue"

if os.path.exists(queue_path):
   with open(queue_path) as f:
      queue = pickle.load(f)

if 'queue' not in locals():
   queue = []

queue.append(args)

with open(queue_path, "wb+") as f:
   pickle.dump(queue, f)

print "entry added to queue."
