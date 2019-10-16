import json

#Read dummy json to work in this module
with open('C:\dev\python-getting-started\json\\test.json') as f:
    data = f.read()
request = json.loads(data) # {'request-id': 5846615, 'color': {'dominantColorBackground': 'white', 'dominantColorForeground': 'white'}, 'description': {'tags': ['bear', 'polar', 'animal'], 'captions': [{'text': 'a large bear'}]}}

#print the value of the request-id
print(request['request-id'])
# read key-subkey value
print(request['color']['dominantColorBackground'])
# print out the first tag in the description
print(request['description']['tags'][0])
# or print out all tags
for item in request['description']['tags']:
    print(item)