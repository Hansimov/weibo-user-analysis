import requests

uid = 7275152514
url_fans = "https://weibo.cn/{}/fans?page={}"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.43"}

with open("cookies.txt","r") as rf:
    cookiesString = rf.read()

def parseCookies(cookiesString):
    cookies = {}
    items = cookiesString.split(";")
    for item in items:
        name,value=item.strip().split('=',1)
        cookies[name] = value
    # print(items)
    # print(cookies)
    return cookies

url = url_fans.format(uid,99)
cookies = parseCookies(cookiesString)
req = requests.get(url,cookies=cookies)

# def parseHTML():
#     pass
print(req.text)