import requests
from bs4 import BeautifulSoup
import pymongo
import re


def insertMongoDB(values):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['telemedicina']
    coll = db['google_rank']

    x = coll.insert_many(values)
    print(x.inserted_ids)

def scrapSite(urlSite):
    try:
        responseSite = requests.get(urlSite)
    except requests.exceptions.RequestException as e:
        return str(e)
    
    encoding = responseSite.encoding if 'charset' in responseSite.headers.get('content-type', '').lower() else None
    soupSite = BeautifulSoup(responseSite.content, from_encoding=encoding)

    cont = soupSite.find('body')
    if cont:
        words = cont.get_text().replace('\n', ' ')
        words = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', words)
        words = words.split(' ')
        while '' in words:
            words.remove('')
            
        return ','.join(words)
    else:
        return 'NaN'

def scrapGoogle():
    search = 'telemedicina'
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
            print(rank)
            print(link)
            print(content)
            print(len(content))
            obj = {'rank': rank,
                    'title': title.get_text(),
                    'link': link,
                    'content': content }
            values.append(obj) 

    insertMongoDB(values)
    print('FIM')
    
    
def main():
    scrapGoogle()

if __name__ == '__main__':
    main()