import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str,
                    help="Input filename")
parser.add_argument("categories", type=str,
                    help="Category (comma separated string)")
parser.add_argument("output", type=str,
                    help="Output filename")
args = parser.parse_args()

with open(args.input, encoding='utf8') as infile:
    data = json.load(infile)

categories = args.categories.split(',')

data = filter(lambda prod: any(x in categories for x in prod["types"]), data)

with open(args.output, 'w', encoding='utf8') as outfile:
    json.dump(list(data), outfile, ensure_ascii=False, indent=4, sort_keys=True)
