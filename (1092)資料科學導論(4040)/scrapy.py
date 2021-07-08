#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import sys
import json
import time
import base64
import loguru
import ntpath
import random
import pymysql
import requests
import configparser
import concurrent.futures

from PIL import Image

from bs4 import BeautifulSoup

from lxml import etree
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.schema
import sqlalchemy.ext.automap


# In[2]:


def main():
    global pageLinks
    global articles
    global images
    #登入
    login()
    
    #檢查下一頁
    hasNext = search(keyword)
    #print(hasNext)
    while hasNext == True:
        time.sleep(random.randint(2000, 3000)/1000)
        hasNext = fetch_list()
        
    #排序連結
    pageLinks = sorted(pageLinks, key=lambda k: k['link'])
    
    #去除重複的連結
    pageLinks = [dict(t) for t in {tuple(d.items()) for d in pageLinks}]
    
    #排序連結
    pageLinks = sorted(pageLinks, key=lambda k: k['link'])
    
    #顯示{標題,網址}
    #showPage(pageLinks)
    
    #取得內容
    fetch_detail()
    
    try:
        #寫入資料庫
        create_db_scrapy()
    except:
        # 建立連線引擎
        connect_string = connect_string = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset={}'.format(username, password, host, port, database, chartset)
        connect_args = {'connect_timeout': 10}
        engine = sqlalchemy.create_engine(connect_string, connect_args=connect_args, echo=True)


        # 取得資料庫元資料
        metadata = sqlalchemy.schema.MetaData(engine)
        # 產生自動對應參照
        automap = sqlalchemy.ext.automap.automap_base()
        automap.prepare(engine, reflect=True)
        # 準備 ORM 連線
        session = sqlalchemy.orm.Session(engine)
        
        #寫入資料庫
        create_db_scrapy()
    

    sys.exit('爬蟲結束')


# In[4]:


def showPage(pageLinks):
    print(len(pageLinks))
    for pageLink in pageLinks:
        print(pageLink)


# In[5]:


#登入
def login():
    #進入 pixiv 登入頁面
    driver.get(config['pixiv']['Login'])
    time.sleep(random.randint(2000, 3000)/1000)
    login_username = driver.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input')
    login_password = driver.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input')
    login_button = driver.find_element_by_xpath('//*[@id="LoginComponent"]/form/button')

    #填入帳密並送出
    login_username.send_keys(config['pixiv']['Username'])
    login_password.send_keys(config['pixiv']['Password'])
    login_button.click()
    time.sleep(random.randint(2000, 3000)/1000)


# In[6]:


#搜尋(關鍵字:)
def search(keyword):
    search_input = driver.find_element_by_xpath('//input[@class="sc-5ki62n-4 fOlftl"]')
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)
    return True


# In[7]:


#取得列表
def fetch_list():
    #print('fetch_list()')
    time.sleep(random.randint(2000, 3000)/1000)
    results = driver.find_element_by_xpath('//ul[@class="l7cibp-1 iTgRcY"]').get_attribute('innerHTML')
    if results == None:
        sys.exit('程式中止：無回應指定內容元素')

    dom = etree.HTML(results)
    links = dom.xpath('//div[@class="rp5asc-0 bscYTy"]/a/@href')
    titles = dom.xpath('//div[@class="iasfms-0 iubowd"]/a/text()')
    composeItems(links, titles)

    #利用下一頁按鈕，判讀有無下一頁
    try:
        nextPage = driver.find_element_by_xpath('//nav[@class="xhhh7v-0 iNnSIH"]').get_attribute('innerHTML')
        nextPageUrl = etree.HTML(nextPage)
        if nextPageUrl.xpath('//a[@class="xhhh7v-1-filterProps-undefined bpzyvR"]/@aria-disabled')[1] == 'false':
            driver.get(config['pixiv']['Url'] + nextPageUrl.xpath('//a[@class="xhhh7v-1-filterProps-undefined bpzyvR"]/@href')[1])
            time.sleep(random.randint(2000, 3000)/1000)
        else:
            return
    except NoSuchElementException as e:
        print('無下一頁')
        return False

    return True


# In[8]:


#取得內容
def fetch_detail():
    for pageLink in pageLinks:
        try:
            print('讀取 >>> ' + pageLink['link'])
            driver.get(pageLink['link'])
            time.sleep(random.randint(2000, 3000)/1000)
            results = driver.find_element_by_xpath('//section').get_attribute('innerHTML')
            if results == None:
                print('忽略本頁：無回應指定內容元素')
                return
            dom = etree.HTML(results)
            parseDetail(pageLink, dom)
        except:
            print('內容頁面錯誤。')


# In[9]:


#解析內容頁
def parseDetail(pageLink, dom):
    global articles
    global images
    #作品ID
    ID = ''
    try:
        ID = pageLink['link'].split('/')[-1]
        print('作品ID:',ID)
    except:
        print('找不到：作品ID')
        
    #標題
    articleTitle = ''
    try:
        articleTitle = dom.xpath('//h1/text()')[0]
        print('標題:',articleTitle)
    except:
        print('找不到：標題')
        
    #內容
    description = ''
    try:
        description = dom.xpath('//div[@class="eyxzap-0 hVnlwp"]/p')[0]
        description = etree.tostring(description, encoding='unicode', pretty_print=True)
        description = remove_tags(description)
        print('內容:',description,end='')
    except:
        print('找不到：內容')
        
    #主題標籤
    hashtags = []
    try:
        hashtags = dom.xpath('//a[@class="gtm-new-work-tag-event-click"]/text()')
        print('主題標籤',hashtags)
    except:
        print('找不到：主題標籤')
        
    #讚!
    likes = 0
    try:
        likes = dom.xpath('//dd[@title="讚！"]/text()')[0].replace(',','')
        print('讚!',likes)
    except:
        print('找不到：讚!')
        
    #收藏
    collects = 0
    try:
        collects = dom.xpath('//dd[@title="收藏"]/text()')[0].replace(',','')
        print('收藏',collects)
    except:
        print('找不到：收藏')
        
    #瀏覽量
    views = 0
    try:
        views = dom.xpath('//dd[@title="浏览量"]/text()')[0].replace(',','')
        print('瀏覽量',views)
    except:
        print('找不到：瀏覽量')
        
    #投稿時間
    postDate = 0
    try:
        postDate = dom.xpath('//div[@title="投稿時間"]/text()')[0].replace('年','-').replace('月','-') .replace('日','')
        postDate = int(datetime.strptime(postDate, '%Y-%m-%d %H:%M').timestamp())
        print('投稿時間',postDate)
    except:
        print('無法解析：發文日期')
        
    #畫師
    artist = 'None'
    artistLink = ''
    try:
        artist = dom.xpath('//a[@class="sc-10gpz4q-6 gOiTBS"]/div/text()')[0]
        artistLink = config['pixiv']['Url'] + dom.xpath('//a[@class="sc-10gpz4q-6 gOiTBS"]/@href')[0]
        print('畫師',artist)
        print('畫師網頁',artistLink)
    except:
        print('找不到：畫師')
        
    #圖片
    images_Detail = []
    try:
        try:
            open_button = driver.find_element_by_xpath('//button[@class="emr523-0 cwSjFV"]')
            open_button.click()
            time.sleep(random.randint(3000, 5000)/1000)
            new_result = driver.find_element_by_xpath('//div[@class="sc-1qi8blb-0 jtqttS"]').get_attribute('innerHTML')
            new_dom = etree.HTML(new_result)
            urls = new_dom.xpath('//img[@class="sc-1qpw8k9-1 fvHoJ"]/@src')
            for url in urls:
                filename = 'images/' + path_leaf(url)
                images_Detail.append({'url':url,'filename':filename})
                download_file(url, filename)
                print('圖片連結:',url,'檔案名稱:',filename)
                images.append({
                    'filename':str(filename),
                    'image':image_base64(filename)
                })
            
        except:
            url = dom.xpath('//a[@class="sc-1qpw8k9-3 kIEHmb gtm-expand-full-size-illust"]/@href')[0]
            filename = 'images/' + path_leaf(url)
            images_Detail.append({'url':url,'filename':filename})
            download_file(url, filename)
            print('圖片連結:',url,'檔案名稱:',filename)
            images.append({
                'filename':str(filename),
                'image':image_base64(filename)
            })
    except:
        print('找不到：圖片')

    articles.append({
            'title':str(pageLink['title']), 
            'link':str(pageLink['link']), 
            'ID':str(ID), 
            'articleTitle':str(articleTitle),
            'description':str(description), 
            'hashtags':str(hashtags), 
            'likes':int(likes), 
            'collects':int(collects),
            'views':int(views),
            'postDate':int(postDate),
            'artist':str(artist)
        })


# In[10]:


#組合列表中的標題
def composeItems(links, titles):
    global pageLinks
    for idx, link in enumerate(links):
        #print(link)
        #print(titles[idx])
        pageLinks.append({'title':titles[idx], 'link':config['pixiv']['Url'] + link})


# In[11]:


#清空字串內全部的 html tag，只留下內文
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)


# In[12]:


#解析檔案路徑及檔名
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail #or ntpath.basename(head)


# In[13]:


#以分包的方法下載檔案
def download_file(url, filename):
    # NOTE the stream=True parameter below
    my_headers = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.41'
    }
    try:
        with requests.get(url, headers = my_headers, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
        process_image(filename)
        return filename
    except:
        print("Error")
        return 0


# In[14]:


#讀取圖片
def image_base64(filename):
    with open(filename, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read())
    return base64_string


# In[15]:


#圖片壓縮
def process_image(filename):
    image = Image.open(filename)
    print (image.size)
    try:
        image.thumbnail((1000,1000))
        image.save(filename)
        print (image.size)
    except:
        print('Error')


# In[16]:


#發現重複的列表項目，若有不再予以新增
def find_duplicate_db_list(item):
    sqlalchemy.Table(__listtable__, metadata, autoload=True)
    Alist = automap.classes[__listtable__]

    aList = session.query(
        Alist
    ).filter(
        Alist.article_id == item['ID'], #item['source_id'],
        Alist.article_title == item['title'],
        Alist.article_url == item['link']
    ).first()

    if aList:
        loguru.logger.info('Find duplicate source article: ' + str(aList.id))
        return aList.id
    else:
        return False


# In[17]:


def create_db_list_item(item):
    loguru.logger.info(item['title'])

    itemDuplicateId = find_duplicate_db_list(item)
    if itemDuplicateId != False:
        return itemDuplicateId

    created = int(time.mktime(datetime.now().timetuple()))
    sqlalchemy.Table(__listtable__, metadata, autoload=True)
    Alist = automap.classes[__listtable__]

    alist = Alist()
    alist.article_id = item['ID']
    alist.article_topic = keyword
    alist.article_title = item['title']
    alist.article_url = item['link']
    alist.created = created
    session.add(alist)
    session.flush()

    return alist.id


# In[18]:


def create_db_article(item, listId):
    created = int(time.mktime(datetime.now().timetuple()))
    sqlalchemy.Table(__articletable__, metadata, autoload=True)
    Article = automap.classes[__articletable__]

    sourceContent = {
        'keyword': keyword, 
        'ID': item['ID'], 
        'articleTitle': item['articleTitle'],  
        'description': item['description'],
        'hashtags': item['hashtags'],
        'likes': item['likes'],
        'collects': item['collects'],
        'views': item['views'],
        'postDate': item['postDate'],
        'artist': item['artist']
    }
    
    sourceContent = json.dumps(sourceContent, ensure_ascii=False).encode('utf-8').decode('utf-8')
    print(sourceContent)
    
    article = Article()
    article.list_id = listId
    article.article_title = item['articleTitle']
    article.article_description = item['description']
    article.article_hashtags = item['hashtags']
    article.article_likes = item['likes']
    article.article_collects = item['collects']
    article.article_views = item['views']
    article.article_postdate = item['postDate']
    article.article_artist = item['artist']
    article.created = created
    session.add(article)
    return


# In[19]:


def create_db_image(item):
    created = int(time.mktime(datetime.now().timetuple()))
    sqlalchemy.Table(__imagetable__, metadata, autoload=True)
    Article = automap.classes[__imagetable__]
    
    article = Article()
    article.article_filename = item['filename']
    article.article_image = item['image']
    article.created = created
    session.add(article)
    return


# In[20]:


def create_db_scrapy():
    for item in articles:
        listId = create_db_list_item(item)
        create_db_article(item, listId)
        try:
            session.commit()
        except Exception as e:
            loguru.logger.error('新增資料失敗')
            loguru.logger.error(e)
            session.rollback()
    for image_item in images:
        create_db_image(image_item)
        try:
            session.commit()
        except Exception as e:
            loguru.logger.error('新增圖片失敗')
            loguru.logger.error(e)
            session.rollback()
            
    
    #session.close()
    loguru.logger.info('完成爬蟲及寫入資料.')
    return


# In[21]:


if __name__ == '__main__':
    loguru.logger.add(
        f'{datetime.today().strftime("%Y%m%d")}.log',
        rotation='1 day',
        retention='7 days',
        level='DEBUG'
    )
    
    config = configparser.ConfigParser()
    config.read("config.ini")

    #Selenium with webdriver
    from selenium.webdriver import Edge
    driver = Edge(executable_path='C:\\Users\\wumin\\Documents\\Python\\EdgeDriver.exe')
    driver.maximize_window()
    
    #資料庫定義
    __articletable__ = 'crawler_article'
    __listtable__ = 'crawler_list'
    __imagetable__ = 'crawler_image'
    #取得資料庫連線設定
    host = config['mysql']['Host']
    port = int(config['mysql']['Port'])
    username = config['mysql']['User']
    password = config['mysql']['Password']
    database = config['mysql']['Database']
    chartset = config['mysql']['Charset']

    # 建立連線引擎
    connect_string = connect_string = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset={}'.format(username, password, host, port, database, chartset)
    connect_args = {'connect_timeout': 10}
    engine = sqlalchemy.create_engine(connect_string, connect_args=connect_args, echo=True)
    
    
    # 取得資料庫元資料
    metadata = sqlalchemy.schema.MetaData(engine)
    # 產生自動對應參照
    automap = sqlalchemy.ext.automap.automap_base()
    automap.prepare(engine, reflect=True)
    # 準備 ORM 連線
    session = sqlalchemy.orm.Session(engine)
    
    #全域變數
    pageLinks = []
    articles = []
    images = []
    
    #keyword
    keyword = '風景10000users入り 空 背景 '
    
    main()

