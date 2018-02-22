import urllib.request
import json
import html

def getInfo(id):
    return json.loads(urllib.request.urlopen("http://api.pouet.net/v1/prod/?id=" + str(id)).read())["prod"]

def getDemos():
    def isDemo(id):
        return getInfo(id)["type"] == "demo"

    prods = json.loads(urllib.request.urlopen("http://api.pouet.net/adhoc/prods-from-year?year=2017").read())["prods"]
    prods_ids = map(lambda prod: int(prod["id"]), prods)
    return list(filter(isDemo, prods_ids))

# print(json.dumps(getDemos()))


# ranked = json.load(open('ranked.json'))
# ranked = map(lambda prod: prod["id"], ranked)
# print(list(ranked))

ranked = [
    69648, 71414, 69701, 71996, 71976, 68878, 71742, 69705, 69688, 68783, 71543,
    69719, 70596, 71881, 69702, 72279, 69730, 70460, 68795, 71774, 71413, 71406,
    69302, 70013, 68869, 68891, 70418, 69700, 72716, 68903, 68868, 71415, 71978,
    71430, 72278, 68986, 70961, 72573, 68906, 71544, 71416, 71003, 68893, 70415,
    70075, 70788, 71989, 71135, 69738, 70003, 71719, 70410, 71558, 71134, 71701,
    73026, 72746, 68676, 71971, 68794, 71777, 70217, 69212, 71398, 71412, 69649,
    69034, 72741, 68774, 72273, 69693, 71810, 69803, 69323, 71729, 68705, 70450,
    69665, 72210, 71870, 71711, 69685, 70134, 72025, 68884, 71786, 69728, 71560,
    69393, 69110, 70628, 68758, 69727, 70409, 69655, 70466, 69656, 71632, 72004,
    71835, 70627, 72490, 70025, 71124, 71713, 69138, 69686, 70987, 71825, 71402,
    70132, 70986, 71588, 71793, 68775, 69692, 71637, 69735, 71915, 71585, 72019,
    69804, 71738, 69706, 70468, 70465, 71634, 71409, 70828, 72956, 69784, 70827,
    70136, 72968, 71580, 71422, 70629, 70467, 71788, 70445, 69722, 68916, 69944,
    68862, 69740, 70220, 72407, 70637, 70084, 70608, 72717, 71704, 69731, 68716,
    69271, 69137, 68978, 70400, 71843, 71429, 71631, 72000, 71724, 69016, 70390,
    73059, 72722, 71432, 69736, 71914, 72740, 71709, 73098, 71547, 71705, 71498,
    68724, 71411, 71126, 69133, 72005, 71748, 72657, 71115, 71642, 70760, 73148,
    69344, 73162, 71349, 73027, 72718, 70023, 68709, 72002, 71981, 71735, 71417,
    72384, 68728, 70392, 72451, 69805, 70770, 72570, 71281, 72807, 68837, 72481,
    68874, 71721, 70810, 72288, 73219, 70047, 71916, 72466, 71917, 68836, 71499,
    71831, 71796, 70630, 71606, 72285, 70652, 71995, 70206, 71577, 73138, 72477,
    69158, 72282, 68729, 69769, 70396, 71209, 72965, 68730, 69964, 71233, 71589,
    70642, 70448, 71818, 70607, 69355, 71874, 71546, 70978, 71408, 73105, 72951,
    68840, 72345, 71421, 69149, 69848, 71664, 68976, 69319, 72470, 71116, 71424,
    68777, 70289, 68822, 69709, 68977, 71614, 71436, 70617, 70305, 69014, 72828,
    72768, 68870, 72453, 72270, 69931, 70303, 71503, 71526, 71291, 73165, 71635,
    71502, 69782, 71696, 70699, 68725, 71676, 72480, 72572, 70563, 71745, 71433,
    72478, 71789, 71435, 73104, 70205, 71689, 68876, 71549, 71751, 71925, 68877,
    71468, 72274, 71442, 70397, 71650, 73160, 71734, 72121, 69830, 70656, 68838,
    72452, 69689, 71454, 69781, 70417, 68779, 70509, 70240, 70614, 69947, 72456,
    71821, 72473, 72474, 71431, 71509, 72756, 71268, 70616, 68710, 68802, 69737,
    69758, 73109, 72289, 71926, 71909, 71834, 71584, 70063, 70391, 70196, 68896,
    72387, 70012, 72929, 70643, 68798, 72376, 71494, 68839, 71824, 69753, 71039,
    71651, 68955, 73168, 70970, 69768, 72479, 70036, 70389, 73151, 71504, 70531,
    71507, 68974, 73094, 72475, 70606, 68712, 71697, 71732, 71927, 71120, 69772,
    70419, 69283, 71833, 70151, 71243, 69757, 69993, 70693, 70989, 70076, 71450,
    68871, 70422, 71903, 72290, 71571, 69806, 70615, 72545, 72003, 71922, 71452,
    71896, 69756, 70399, 71924, 69961, 69754, 71747, 68801, 69783, 70590, 70593,
    71451, 70162, 69517, 70207, 71980, 73113, 69824, 70612, 71923, 71662, 70288,
    71808, 68846, 69822, 70421, 70352, 71535, 70402, 69747, 70348, 70613, 71743,
    71746, 72865, 69759, 70562, 71894, 70611, 71744, 71895, 71891
]

# def getRank(id):
#     return int(getInfo(id)["rank"])

# print("demos: " + str(len(demos)))
# demos = demos[:5] # just use a tiny selection for testing

# ranked = map(lambda id: (id, getRank(id)), demos)
# ranked = sorted(ranked, key=lambda prod: prod[1])
# ranked = map(lambda prod: {"id" : prod[0], "rank" : prod[1]}, ranked)
# print(json.dumps(list(ranked), indent=4, sort_keys=True))

# for id in demos:
#    info = getInfo(id)
#    info = json.loads(urllib.request.urlopen("http://api.pouet.net/v1/prod/?id=" + str(id)).read())["prod"]
#    print(json.dumps(info, indent=4, sort_keys=True))

def encode(unicode_data, encoding='ascii'):
    return unicode_data.encode(encoding, 'xmlcharrefreplace').decode("utf-8") 

# ranked = ranked[:2] # just use a tiny selection for testing

data = map(lambda id: getInfo(id), ranked)
print(json.dumps(list(data), indent=4, sort_keys=True))

# for id in ranked:
    #info = getInfo(id)
    # print(json.dumps(info, indent=4, sort_keys=True))
    #groups = ", ".join(map(lambda group: encode(group["name"]), info["groups"]))
    #print("<p>")
    #print("<h1>" + encode(info["name"]) + "</h1>")
    #print("<h2>" + groups + "</h2>")
    #print("<a href=\"http://www.pouet.net/prod.php?which=" + str(id) + "\">")
    #if hasattr(info, 'screenshot'):
#        print("<img src=\"" + info["screenshot"] + "\">")
#    else:
#        print("No screenshot :(")
#    print("</a>")
#    print("</p>")
#    print("<hr>")
