import re
import time, datetime
import os

re_text     = re.compile(r'id=".*?"><div><span class="c[m|t]t">(.*?)<a', re.S)
re_pubtime  = re.compile(r'<span class="ct">(.*?)&nbsp;', re.S)
re_pagesize = re.compile(r'/(\d*?)页</div>', re.S)
re_idx      = re.compile(r'</div><div class="c" id="(.*?)"><div>', re.S)

def calcFilename(uid, pagenum):
    filename = './xmls/{}-{:0>6}.xml'.format(uid, pagenum)
    return filename

def parseXML(uid, pagenum):
    filename = calcFilename(uid, pagenum)
    with open(filename, encoding='utf8', mode='r') as rf:
        doc = rf.read()

    # text = re_text.findall(doc)
    pagesize = int(re_pagesize.findall(doc)[0])
    idx = re_idx.findall(doc)
    pubtime_original = re_pubtime.findall(doc)
    pubtime = [''] * len(pubtime_original)
    for i in range(len(pubtime_original)):
        pubtime[i] = convertTime(getFileTime(filename)[0], pubtime_original[i])

    created_time = getFileTime(filename)[0]
    # print(type(created_time))
    # for i in range(len(pubtime)):
        # print(idx[i], convertTime(created_time, pubtime[i]), pubtime[i])

    return pagesize, idx, pubtime

def convertTime(created_time, time_string=''):
    # '刚刚', '20分钟前', '今天 18:43', '01月31日 22:57', '2017-10-22 07:49:32'
    created_time_string = created_time.strftime("%Y-%m-%d %H:%M:%S")
    ttypes = [r'刚刚', r'(\d+)分钟前', r'今天 (.*)', r'(\d+月\d+日.*)', r'(\d+-\d+-\d+.*)']

    dynamic_time_string = '1970-01-01 00:00:00'

    tn = 0
    for ttype in ttypes:
        if bool(re.match(ttype, time_string)):
            break
        else:
            tn += 1

    re_result = re.search(ttypes[tn], time_string).group(1)

    if   tn == 0:
        dynamic_time_string = created_time_string
    elif tn == 1:
        mins = int(re_result)
        dynamic_time_string = (created_time - datetime.timedelta(minutes=mins)).strftime("%Y-%m-%d %H:%M:%S")
    elif tn == 2:
        hr_min = re_result
        dynamic_time_string = created_time_string[0:10] + ' ' + hr_min + ':00'
    elif tn == 3:
        mon, day, hr, mins = list(map(lambda s,e: re_result[s:e], [0,3,7,10], [2,5,9,12]))
        dynamic_time_string = created_time_string[0:4] + '-' + mon + '-' + day + ' ' + hr +  ':' + mins + ':00'
    elif tn == 4:
        dynamic_time_string = re_result
    else:
        pass

    return dynamic_time_string

def getFileTime(filename):
    # filename = './xmls/{}-{:0>6}.xml'.format(uid, pagenum)
    created_time = datetime.datetime.fromtimestamp(os.path.getctime(filename))#.strftime("%Y-%m-%d %H:%M:%S")
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))#.strftime("%Y-%m-%d %H:%M:%S")
    return created_time, modified_time

def updatePagesize(uid, pagesize_old):
    pagesize_new = parseXML(uid, pagesize_old)[0]
    return pagesize_new

if __name__ == '__main__':
    uid = 2219124641
    # for pagenum in [1,2,3,50,1000,1500]:
    #     parseXML(uid, pagenum)
    # normTime(uid, 1)

