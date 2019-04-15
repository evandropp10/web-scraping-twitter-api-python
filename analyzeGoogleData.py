import pandas as pd
import pymongo

def analyze():
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['google_rank']

    cursor = coll.find()

    df = pd.DataFrame(list(cursor))

    # 1.1
    df['domain'] = df['link'].apply(lambda x: x.split('/')[2])
    dfDomains = pd.DataFrame(df['domain'].value_counts())
    dfDomains.to_csv('domains.csv')

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
    df100.to_csv('100.csv')


'''
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['telemedicina']
coll = db['google_rank']

cursor = coll.find()

df = pd.DataFrame(list(cursor))
df
'''