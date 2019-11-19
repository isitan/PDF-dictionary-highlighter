import json
import codecs
locations = set()

with open('world-cities_json.json') as json_file:
    data = json.load(json_file)
    for e in data:
        locations.add(e["country"])
        locations.add(e["name"])
        locations.add(e["subcountry"])

with codecs.open("locations.txt", "w", "utf-8") as f:
    for el in locations:
        print >> f, el