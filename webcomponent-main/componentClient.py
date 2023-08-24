
import requests

domainlist = ["csdn.net", "youku.com", "wappalyzer.com"]
for domain in domainlist:
    # 这边填你的内网服务器地址，端口8000
    req = requests.get("http://192.168.231.129:8000", params={"domain": domain})
    print(req.text, type(req.text))



