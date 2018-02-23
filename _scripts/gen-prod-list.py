import urllib.request
import json
import html

def getInfo(id):
    return json.loads(urllib.request.urlopen("http://api.pouet.net/v1/prod/?id=" + str(id)).read())["prod"]

def getProdIdsForYear(year):
    prods = json.loads(urllib.request.urlopen("http://api.pouet.net/adhoc/prods-from-year?year=" + str(year)).read())["prods"]
    return map(lambda prod: int(prod["id"]), prods)

prodIds = getProdIdsForYear(2017)
data = map(lambda id: getInfo(id), prodIds)
print(json.dumps(list(data), indent=4, sort_keys=True))
