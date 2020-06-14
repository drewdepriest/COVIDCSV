import glob, os
import json

result = []
for file in glob.glob("*.json"):
    #print(file)
	with open(file, "r", encoding="utf8") as infile:
			result.append(json.load(infile))

with open("covid-full-history.json", "w") as outfile:
	json.dump(result, outfile)
