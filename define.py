import requests
import json
import config_local
import argparse

app_id = config_local.APP_ID
app_key = config_local.APP_KEY

parser = argparse.ArgumentParser(description='Example with long option names')
parser.add_argument('-w', action="store", dest="WORD_ID")

language = 'en'
word_id = vars(parser.parse_args())['WORD_ID']
output = ':::::::::::::::::::\n::::Definitions::::\n:::::::::::::::::::\n'
head = "::::"
tail = ":::"

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/definitions'

r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
parsed_json = json.loads(json.dumps(r.json()))

for r in parsed_json['results'][0]['lexicalEntries']:
    body = r['entries'][0]['senses'][0]['definitions'][0]
    output += '\n' + head + body + tail

print(output)
