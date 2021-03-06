import requests
from bs4 import BeautifulSoup
import pymongo
import re

def deleteMongoDB():
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['google_rank']
    coll.drop()

def insertMongoDB(values):
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['google_rank']

    x = coll.insert_many(values)

def scrapSite(urlSite):
    try:
        responseSite = requests.get(urlSite)
    except requests.exceptions.RequestException as e:
        return ''
        #str(e)
    
    encoding = responseSite.encoding if 'charset' in responseSite.headers.get('content-type', '').lower() else None
    soupSite = BeautifulSoup(responseSite.content, "html.parser", from_encoding=encoding)

    cont = soupSite.find('body')
    if cont:
        words = cont.get_text().replace('\n', ' ')
        words = re.sub(u'[^a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', words)
        words = words.split(' ')
        while '' in words:
            words.remove('')
        for x in words:
            if len(x.strip()) <= 4:
                while x in words:
                    words.remove(x)
            if 'class' in x.lower() or 'click' in x.lower() or 'idtab' in x.lower() or 'style' in x.lower() or 'div' in x.lower() or 'http' in x.lower() or 'false' in x.lower() or 'return' in x.lower() or 'function' in x.lower() or 'none' in x.lower() or 'share' in x.lower():
                while x in words:
                    words.remove(x)
            
            
        return ','.join(words)
    else:
        return 'NaN'

def scrapGoogle(search):
    url = 'https://www.google.com/search?q=' + search + '&num=100'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    values = []
    rank = 0
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            rank += 1
            link = link['href']
            link = link.split('=')[1]
            link = link.split('&')[0]
            content = scrapSite(link)

            obj = {'rank': rank,
                    'title': title.get_text(),
                    'link': link,
                    'content': content }
            values.append(obj) 

    insertMongoDB(values)

    