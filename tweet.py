import json
import twitter
import ConfigParser
from datetime import date

"""
Pushes a tweet with today's thing
"""

config = ConfigParser.RawConfigParser()
config.read('config.ini')

# Today's date
d = date.today()
month_path = d.strftime("_entries/%Y/%m")
current = d.strftime("_entries/%Y/%m/%d.json")

with open(current, "r") as f:
    data = f.read()

thing = json.loads(data)

api = twitter.Twitter(auth=twitter.OAuth(
    config.get('twitter', 'access_token_key'),
    config.get('twitter', 'access_token_secret'),
    config.get('twitter', 'consumer_key'),
    config.get('twitter', 'consumer_secret')))

status = api.statuses.update("%s: %s - %s" % (
    thing["verb"].capitalize(), thing["title"], thing["url"]))
