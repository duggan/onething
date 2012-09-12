# one thing
Your time is valuable.

## Creating an entry
Today's entry is created as a JSON formatted file @ `verb/year/month/day.json`

The file takes the following format (example):

```
{
    "verb":"read",
    "title":"After 35 years, Voyager nears edge of solar system.",
    "url": "http://www.npr.org/templates/transcript/transcript.php?storyId=160609488",
    "contributor": "anonymous"
}
```

### Create

`create.py` takes several flags, some optional:

```
--verb				read|watch|see
--title				"A string encapsulated by double quotes"
--url				"A url encapsulated by double quotes"
--contributor		"A string encapsulated by double quotes" (optional)
--contributor-url	"A url encapsulated by double quotes" (optional)
```
This generates the JSON formatted file described above, and returns the path to this file
as the only output, eg:

```
ross-air:~$ create.py --verb read --title "After 35 years, Voyager nears edge of solar system." \
--url "http://www.npr.org/templates/transcript/transcript.php?storyId=160609488"
/home/ross/onething/_entries/read/2012/09/08.json
ross-air:~$
```

If no `contributor` information is passed, the entry will be attributed to *anonymous*.

### Build

`build.py` accepts the output of `create.py` as its only input (file location), and builds the HTML for that date, replacing whatever the currently build page is.

### Publish

To publish, all changes are committed, then pushed to the "published" branch of the repo.

`git commit -am "Thing for 2012/09/08 - After 35 years, Voyager nears edge of solar system."`

`git push origin published`

### Queue

Queue something up to be published.

`queue-push.py` takes the same parameters as `create.py`

`queue-pop.py` takes an entry off the bottom of the queue and writes it as today's entry JSON.

For now, historical "things" will not be public, to keep the focus narrow.
