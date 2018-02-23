import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str,
                    help="File to sort")
args = parser.parse_args()

with open(args.filename, encoding='utf8') as infile:
    data = json.load(infile)

data = sorted(data, key=lambda prod: int(prod["rank"]))

with open(args.filename, 'w', encoding='utf8') as outfile:
    json.dump(list(data), outfile, ensure_ascii=False, indent=4, sort_keys=True)
