import requests
import sys
import json


def padtext(text=None):
  text = ''
  for i in range(1, len(sys.argv)):
    text+= sys.argv[i] + '+'
  return text[ :(len(text) - 1 )]

text = padtext()
url = 'https://api.textgears.com/check.php'
key = 'zHOhWHCGjaqGed7M'
PARAMS = { 'text': text, 'key': key }
r = requests.get(url = url, params= PARAMS)
binary = r.content
res = json.loads(binary)

errors = res['errors']

if(len(errors) == 0):
  print('No error')
else:
  for error in errors:
    bad = error['bad']
    print('Error in: '+ bad)
    print('Better alternative: ')
    for better in error['better']:
      print(better)
