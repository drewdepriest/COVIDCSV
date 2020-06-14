import glob
import json

output = []
# chug through directory of daily JSON files
for f in glob.glob("*.json"):
    #print(file)
	# stitch them all together
	with open(f, "r", encoding="utf8") as infile:
			output.append(json.load(infile))

#push the large file to new JSON in same directory
with open("covid-full-history.json", "w") as outfile:
	json.dump(output, outfile)
