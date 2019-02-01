import requests

url = 'https://weibo.cn/u/2219124641?page=1'

with open('cookie.txt', 'r') as rf:
    cookie = rf.readline().strip()
    user_agent = rf.readline().strip()

headers = {
    'Cookie': cookie,
    'User-Agent': user_agent,
}

sess = requests.Session()
req = sess.get(url, headers=headers)
# req.encoding = None
print(req.text)

with open('xmls/ellie.xml', encoding='utf8', mode='w') as wf:
    wf.write(req.text)


# print(req.content)