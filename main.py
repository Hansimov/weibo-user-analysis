'''
面向社会工程学的SNS分析和挖掘
    http://cdmd.cnki.com.cn/Article/CDMD-10248-1013022142.htm

爬虫实战（一）：爬取微博用户信息
    https://blogof33.com/post/11/

爬虫实战（二）：Selenium 模拟登录并爬取信息
    https://blogof33.com/post/12/

爬虫实战（三）：微博用户信息分析
    https://blogof33.com/post/13/

'''

# url = 'https://weibo.cn/u/2219124641'
from fetch_pages import *
from parse_xmls import *

if __name__ == '__main__':
    uid = 2219124641
    # uid = 3761166897
    fetchPage(uid, 1)
    pagesize = parseXML(uid, 1)[0]
    i = 1
    while i <= pagesize:
        print('Fetching Page {}'.format(i))
        fetchPage(uid, i)
        i += 1
        if i == pagesize+1:
            pagesize = parseXML(uid, i-1)[0]
        time.sleep(0.5)
