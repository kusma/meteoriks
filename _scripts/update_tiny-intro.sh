#!/bin/sh
python3 _scripts/type-filter-prod-list.py _data/prods.json 8k,4k,1k,512b,256b,128b,64b,32b _data/tiny-intro.json
python3 _scripts/platform-filter-in-prod-list.py _data/tiny-intro.json "Windows,JavaScript,MS-Dos,MacOSX Intel,Linux,FreeBSD,BeOS" _data/tiny-intro.json
