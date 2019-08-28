from parse_xmls import *
import re
import os
import sys
import pyecharts as pe

uid = 2219124641

xmls = [f for f in os.listdir('./xmls') if re.match(r'{}-.*\d+.xml'.format(uid), f)]

redundant_size = 0
for i in range(0,3):
    redundant_size += len(parseXML(uid, len(xmls)-i)[1])

dynamic_size = 10 * (len(xmls)-3) + redundant_size

idxs = [''] * dynamic_size
pubtimes = [''] * dynamic_size


def extractXML(pagenum):
    global idxs, pubtimes
    # sys.stdout.write("\rParsing page {:0>6}".format(pagenum))
    _, idxs_part, pubtimes_part = parseXML(uid, pagenum)
    j = (pagenum-1)*10
    for idx, pubtime in zip(idxs_part, pubtimes_part):
        pubtimes[j] = pubtime
        idxs[j] = idx
        j += 1
    # return idxs_part, pubtimes_part

for i in range(1, len(xmls)+1):
    extractXML(i)

# with open('records.txt',encoding='utf8',mode='w') as wf:
#     for idx, pubtime in zip(idxs, pubtimes):
#         print(idx, pubtime,file=wf)

idxs = [x for x in idxs if x != '']
pubtimes = [x for x in pubtimes if x != '']
print(len(idxs), len(pubtimes))

pubtime_x = [i for i in range(0,24)]
pubtime_y = [0] * 24

def calcTimeDistribution():
    global pubtime_y
    # '1970-01-01 00:00:00'
    for pubtime in pubtimes:
        seg = int(pubtime[11:13])
        pubtime_y[seg] += 1

calcTimeDistribution()

print(pubtime_y)

bar = pe.Bar('Pubtime Distribution',  '# of Dynamics: {}'.format(len(idxs)))
bar.add('Pubtime', pubtime_x, pubtime_y)
bar.render(path='pubtime.html')