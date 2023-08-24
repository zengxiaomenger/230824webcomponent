
import json
import os
res = dict()

path = "./src/categories.json"
f = open(path, "r")
cat = json.load(f)
f.close()

res["categories"] = cat
res["technologies"] = {}

paths = os.listdir("./src/technologies")

root = "./src/technologies"
for jsonfile in os.listdir("./src/technologies"):
    path = root + "/" + jsonfile
    f = open(path, "r", encoding="utf-8")
    dat = json.load(f)
    f.close()
    for key, value in dat.items():
        res["technologies"][key] = value

data = res

for key, value in data["technologies"].items():
    try:
        if "url" in value and value["url"] is not list:
            data["technologies"][key]["url"] = [value["url"]]
    except:
        pass
    try:
        if "implies" in value and value["implies"] is not list:
            data["technologies"][key]["implies"] = [value["implies"]]
    except:
        pass
    try:
        if "scriptSrc" in value and value["scriptSrc"] is not list:
            data["technologies"][key]["scriptSrc"] = [value["scriptSrc"]]
    except:
        pass
    try:
        if "html" in value and not value["html"] is not list:
            data["technologies"][key]["html"] = [value["html"]]
            print(data["technologies"][key]["html"])
    except:
        pass
    try:
        a = value["headers"]
    except KeyError:
        data["technologies"][key]["headers"] = {}
    try:
        a = value["meta"]
    except KeyError:
        data["technologies"][key]["meta"] = {}

    for k in ['headers', 'meta']:
        obj = data["technologies"][key][k]

f = open("technologies_2.json", "w", encoding="utf-8")
json.dump(data, f, indent=2)
f.close()







