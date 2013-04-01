import pystache
import json
import sys
import hashlib
import re
from datetime import datetime as dt

# Do some datetime fiddling
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

# Grab the first argument raw
data_location = sys.argv[1]
template_location = "template.mustache"
index_location = "public/index.html"
css_location = "public/css/onething.css"

# Build version hash(es)
css_hash = hashlib.md5(open(css_location,'rb').read()).hexdigest()

# Pull in the JSON file
with open(data_location) as f:
   data = f.read()

m = re.search('\d+/\d+/\d+', data_location)
filename_date = m.group(0)
time_from_file = dt.strptime(filename_date, "%Y/%m/%d")
string_from_time = custom_strftime("%B {S}, %Y", time_from_file)

# Convert to object
entry = json.loads(data)

# Pull in the template
with open(template_location) as f:
   template = f.read()

if entry['contributor']:
   contributor = '%s' % entry['contributor']
elif entry['url'] and entry['contributor']:
   contributor = '<a href="%s">%s</a>' % (entry['url'], entry['contributor'])
else:
   contributor = 'anonymous'

generated = pystache.render(template, {
   'verb':entry['verb'],
   'url': entry['url'],
   'title':entry['title'],
   'time':string_from_time,
   'contributor':contributor,
   'css_hash':css_hash
})

with open(index_location, "wb+") as f:
   f.write(generated)

print "done."
