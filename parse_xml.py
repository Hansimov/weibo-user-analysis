import re

with open('./xmls/ellie.xml', encoding='utf8', mode='r') as rf:
    doc = rf.read()
# print(doc)

re_text = re.compile(r'id=".*?"><div><span class="c[m|t]t">(.*?)<a', re.S)
re_pubtime = re.compile(r'.*?<span class="ct">(.*?)&nbsp;', re.S)
re_pagesize = re.compile(r'.*/(\d*?)页</div>', re.S)
re_idx = re.compile(r'</div><div class="c" id="(.*?)"><div>', re.S)

text = re_text.findall(doc)
pubtime = re_pubtime.findall(doc)
pagesize = re_pagesize.findall(doc)[0]
idx = re_idx.findall(doc)

for item in text:
    print(item)
# for item in pubtime:
#     print(item)

# print(len(text), len(pubtime), len(idx))
# print(pagesize)
