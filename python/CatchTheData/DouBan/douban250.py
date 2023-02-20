import requests
import re
import csv
start = 0
while start<250:
    
    url = "https://movie.douban.com/top250?start=" + str(start)
    start = start+25
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text # all the resourse from the website


    # anaylze data
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
                r'</span>.*?<p class="">.*?导演:(?P<direct_name>.*?)'
                r'&nbsp.*?<br>(?P<year>.*?)'
                r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                r'<span>.*?(?P<num>.*?)人评价</span>',re.S)
    # Start to find smt in page_content
    result = obj.finditer(page_content)
    if start ==0:   
        f = open("/Users/monaguo/Desktop/data/data.csv",mode = "w",encoding='utf-8-sig')
        csv_writer = csv.writer(f)
    else:
        f = open("/Users/monaguo/Desktop/data/data.csv",mode = "a",encoding='utf-8-sig')
        csv_writer = csv.writer(f)
    for i in result:
    # print(i.group("name"),end=" ")
    # direct_name =i.group("direct_name").replace('导演:','')
    # print(i.group("direct_name").strip(),end=" ")
    # print(i.group("year").strip(),end=" ")
    # print(i.group("score").strip(),end=" ")
    # print(i.group("num").strip())
        dic = i.groupdict()
        dic['direct_name'] =  dic['direct_name'].strip()
        dic['year'] =  dic['year'].strip()
        csv_writer.writerow(dic.values())

f.close()
print('over!')