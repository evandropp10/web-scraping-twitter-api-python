import pandas as pd
import pymongo

def analyzeGoogle():
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['google_rank']

    cursor = coll.find()

    df = pd.DataFrame(list(cursor))

    # 1.1
    df['domain'] = df['link'].apply(lambda x: x.split('/')[2])
    dfDomains = pd.DataFrame(df['domain'].value_counts())
    dfDomains.to_csv('Google_domains.csv')

    ## 1.2
    df['content'] = df['content'].str.lower()
    df['content'] = df['content'].str.split(',')

    dfNew = pd.DataFrame(df['content'].iloc[0], columns=['words'])

    # Colocando todas as palavras em um único dataframe em uma única coluna
    cont = 1
    while cont < len(df):
        dfAux = pd.DataFrame(df['content'].iloc[cont], columns=['words'])
        frames = [dfNew, dfAux]
        dfNew = pd.concat(frames)
        cont += 1

    # Gerando os 100 primeiros termos com mais incidência
    df100 = pd.DataFrame(dfNew['words'].value_counts().head(100))
    df100.to_csv('Google_100.csv')


def analyzeTwitter():
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['twitter']

    cursor = coll.find()

    df = pd.DataFrame(list(cursor))

    #2.1
    dfUser = pd.DataFrame(df['user'].value_counts())
    dfUser.to_csv('Twitter_users.csv')

    #2.2
    df['weekday'] = df['datetime'].apply(lambda x: x.isoweekday())
    dias = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]
    df['weekday_name'] = df['weekday'].apply(lambda x: dias[x-1])
    dfDay = pd.DataFrame(df['weekday_name'].value_counts())
    dfDay.to_csv('Twitter_dayweek.csv')

    #2.3
    df['hour'] = df['datetime'].apply(lambda x: x.hour)
    dfHour = pd.DataFrame(df['hour'].value_counts())
    dfHour.to_csv('Twitter_hour.csv')



'''
TEST MONGO
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['telemedicina']
coll = db['google_rank']

cursor = coll.find()

df = pd.DataFrame(list(cursor))
df
'''
