import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str,
                    help="Input filename")
parser.add_argument("platforms", type=str,
                    help="Platforms to filter out (comma separated string)")
parser.add_argument("output", type=str,
                    help="Output filename")
args = parser.parse_args()

with open(args.input, encoding='utf8') as infile:
    data = json.load(infile)

platforms = args.platforms.split(',')

data = filter(lambda prod: not all(x in platforms for x in map(lambda p: p["name"], prod["platforms"].values())), data)

with open(args.output, 'w', encoding='utf8') as outfile:
    json.dump(list(data), outfile, ensure_ascii=False, indent=4, sort_keys=True)
