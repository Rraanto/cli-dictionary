"""
dictionary url : https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=your-api-key
thesaurus url : https://www.dictionaryapi.com/api/v3/references/thesaurus/json/umpire?key=your-api-key
"""

import requests 
import json 
import argparse

description = '''
dico is a command line tool that connects to Meriam Webster's api and gives definition of a word or related words.
'''
parser = argparse.ArgumentParser()
parser.add_argument('word', help='word to be defined')
parser.add_argument('-t', '--thesaurus', action='store_true', help='search in the thesaurus')

args = vars(parser.parse_args())


# loading my api key from a file)
keys_str = "" 
with open('apikey.json', mode='r') as key_file:
    key_str = key_file.read()
keys = json.loads(key_str)

# for your own keys 
# keys = {
#     'thesaurus': 'your thesaurus key',
#     'dictionary': 'your dictionary key'
# }

key = keys['thesaurus'] if args['thesaurus'] else keys['dictionary']
url = 'https://www.dictionaryapi.com/api/v3/references/' + ('thesaurus' if args['thesaurus'] else 'collegiate') + '/json/' + args['word'] + '?key=' + key

response = json.loads(requests.get(url).text)

print("\n", args['word'])
for definition in response[0]['shortdef']:
    print("->", definition, "\n")
