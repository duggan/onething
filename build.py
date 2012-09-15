import pystache
import json
import sys
import hashlib

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
   'url': entry['url'],
   'title':entry['title'],
   'contributor':contributor,
   'css_hash':css_hash
})

with open(index_location, "wb+") as f:
   f.write(generated)

print "done."
