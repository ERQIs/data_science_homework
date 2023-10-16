import csv, lxml, requests
from lxml import etree

filePath = "C:\\Users\\ERQI\\Desktop\\homework.csv"
header ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}

fp = open(filePath, "w", encoding = 'utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('name', 'actor', 'date', 'star', 'introduction'))

result = []

urls = ["https://movie.douban.com/top250?start={}&filter=".format(str(i)) for i in range(0,500,25)]

cnt = 1

for url in urls:  #循环分析每25条电影条目
    html = requests.get(url, headers = header)
    selector = etree.HTML(html.text)
    infos = selector.xpath("//ol[@class='grid_view']/li")
    subPages = []
    
    for info in infos:   #获取每个电影的主页
        subPage = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a")[0].attrib['href']
        subPages.append(subPage)


    for subPage in subPages:    #循环每个电影的主页

        print("pursing entry {}".format(cnt))
        cnt += 1
        
        movieInfo = {}   #用来存储一个电影的相关信息
        html = requests.get(subPage, headers = header)
        selector = lxml.etree.HTML(html.text)
        
        actors = []    # 获取演员信息
        for a in selector.xpath(".//div[@id='info']//span[@class='actor']//span[@class='attrs']//a"):
            actors.append(a.text)
        movieInfo["actors"] = ' '.join(actors)
 
        date = []      # 获取上映日期
        for s in selector.xpath(".//div[@id='info']//span[@property='v:initialReleaseDate']"):
            date.append(s.text)
        movieInfo["date"] = ' '.join(date)
        
        movieInfo["intro"] = selector.xpath(".//span[@property='v:summary']")[0].text

        movieInfo["name"] = selector.xpath(".//h1/span[1]")[0].text

        movieInfo["star"] = selector.xpath(".//strong[@class='ll rating_num']")[0].text

        result.append(movieInfo)

for info in result:
    writer.writerow((info["name"], info["actors"], info["date"], info["star"], info["intro"]))

fp.close()
