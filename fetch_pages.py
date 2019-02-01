import requests

# 2219124641
url_body = 'https://weibo.cn/u/{}?page={}'

with open('cookie.txt', 'r') as rf:
    cookie = rf.readline().strip()
    user_agent = rf.readline().strip()

headers = {
    'Cookie': cookie,
    'User-Agent': user_agent,
}

sess = requests.Session()

def fetchPage(uid, pagenum):
    url = url_body.format(uid, pagenum)
    filename = 'xmls/{}-{:0>6}.xml'.format(uid, pagenum)
    req = sess.get(url, headers=headers)

    with open(filename, encoding='utf8', mode='w') as wf:
        wf.write(req.text)

if __name__ == '__main__':
    fetchPage(2219124641, 1)