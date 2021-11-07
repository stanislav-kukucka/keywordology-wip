import requests
import json
lib1 = input("Enter Base Keyword to Suggest: ")
lib2 = input("Enter Letter, Number or Word to Suggest: ")
url = "http://suggestqueries.google.com/complete/search?client=firefox&q=" +(str(lib1)) +"%20" +(str(lib2))

headers = {'USER_AGENT':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
research = json.loads(response.content.decode('cp1252'))

serializeddata = json.dumps(research, indent=4, sort_keys=True) # make json output pretty

print(serializeddata)
