import argparse
import html
import json
import urllib.request

def getInfo(id):
    return json.loads(urllib.request.urlopen("http://api.pouet.net/v1/prod/?id=" + str(id)).read())["prod"]

def getProdIdsForYear(year):
    prods = json.loads(urllib.request.urlopen("http://api.pouet.net/adhoc/prods-from-year?year=" + str(year)).read())["prods"]
    return map(lambda prod: int(prod["id"]), prods)

parser = argparse.ArgumentParser()
parser.add_argument("year", type=int,
                    help="Which year to extract prods for")
parser.add_argument("filename", type=str,
                    help="File to write to")
args = parser.parse_args()

prodIds = getProdIdsForYear(args.year)
data = map(lambda id: getInfo(id), prodIds)

with open(args.filename, 'w', encoding='utf8') as outfile:
    json.dump(list(data), outfile, ensure_ascii=False, indent=4, sort_keys=True)
