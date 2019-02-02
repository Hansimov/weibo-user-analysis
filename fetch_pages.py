import requests
import time

# https://weibo.cn/u/2219124641?page=1
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
    print(req.status_code)

    with open(filename, encoding='utf8', mode='w') as wf:
        wf.write(req.text)

if __name__ == '__main__':
    uid = 2219124641
    for pagenum in [1462]:
        fetchPage(uid, pagenum)
