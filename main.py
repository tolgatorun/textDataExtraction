import json

inputfile = "steamsystems.AxiomCht2"

with open(inputfile, "r") as fi:
    stringfile = fi.read()

jsonObj = json.loads(stringfile)
arrayOfJson = jsonObj["TrendGraph"]["ControlChildren"]
for x in arrayOfJson:
    print(x["ControlProperties"]["DisplayName"])
    print(x["ControlProperties"]["SourceTag"])