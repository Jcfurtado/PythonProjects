import .firebase.ufirebase as firebase

URL = 'lucid-lychee'  # see note on URLs at the bottom of documentation
print
firebase.get(URL)  # this is an empty Firebase
None

firebase.put(URL, 'tell me everything')  # can take a string
print
firebase.get(URL)
tell
me
everything

firebase.put(URL, {'lucidity': 9001})  # or a dictionary
print
firebase.get(URL)
{u'lucidity': 9001}

firebase.put(URL, {'color': 'red'})  # replaces old value
print
firebase.get(URL)
{u'color': u'red'}

print
firebase.get(URL + '/color')
red
