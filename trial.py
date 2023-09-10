import json

# Load the JSON data from the file
with open('/home/baymax/Github_Repos/Pointnet_Pointnet2_pytorch/data/taxonomy.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the data and print "synsetId" and "name" side by side
for item in data:
    synsetId = item["synsetId"]
    name = item["name"]
    print(f"Synset ID: {synsetId}, Class Name(s): {name}")