# webComponent

检测网站使用的组件

## 目录&文件说明

- wappalyzer文件夹：包含指纹源文件，没事儿别乱动
- technologies.json：整理过后能做匹配的指纹文件，没事儿别乱动（截至今日，是最新的）
- webComponent.py：用于整理指纹的文件，没事儿别乱动
- componentServer：linux可执行文件，用法看后面
- componentClient：用法看后面
- componentDetect.py：检测程序，可以随便改

该工具有两种使用方式，具体如下

## 第一种使用方式（推荐）

将该工具部署在服务器上，这样任何人都可以向服务端发请求使用

服务器环境：
1. python3环境，不需要安装任何依赖
2. 必须确保能正常访问github，因为要访问github自动更新指纹库

部署步骤如下：
1. 首先将该项目上传至服务器
2. 进入目录文件夹执行命令chmod 777 componentServer
3. 开启服务端，执行./componentServer

客户端请求方法：
1. 将componentClient.py下载到你电脑上，运行即可，里面代码看下面实例
```
import requests

domainlist = ["csdn.net", "youku.com", "wappalyzer.com"]
for domain in domainlist:
    # 这边填你的内网服务器地址，端口8000，参数只传域名，别加协议
    req = requests.get("http://192.168.231.129:8000", params={"domain": domain})
    print(req.text, type(req.text))
```
返回值如下（返回一个字典，key是组件名，value是组件类别）：
```
{"Element UI":"JavaScript frameworks","OpenResty":"Web servers","Vue.js":"JavaScript frameworks","jQuery":"JavaScript libraries"}
 <class 'str'>
{"Ant Design":"UI frameworks","React":"JavaScript frameworks","Tengine":"Web servers"}
 <class 'str'>
{"Amazon S3":"Miscellaneous","Google Tag Manager":"Tag managers","Nuxt.js":"JavaScript frameworks","Vue.js":"JavaScript frameworks"}
 <class 'str'>
```

## 第二种使用方式（不推荐）

直接将项目中的componentDetect.py和technologies.json下载到本地，用法写在componentDetect.py里了
本地环境：
- python3，记得安装componentDetect的依赖，一共没几个，自己看看手动按一下即可

## 自动更新

如果按照第一种方式部署在服务器上，则服务端运行开始会进行自动更新，记得确保服务器能正常访问github

wappalyzer的指纹库更新频率不大，遂设置两个月更新一次

第二种方式的指纹不会自动更新，所以，你要去你的服务器上下载最新的指纹库，直接下载technologies.json就行

