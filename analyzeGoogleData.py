import pandas as pd
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['telemedicina']
coll = db['google_rank']

cursor = coll.find()

df = pd.DataFrame(list(cursor))

df['content'] = df['content'].str.lower()
df['content'] = df['content'].str.split(',')

dfNew = pd.DataFrame(df['content'].iloc[0], columns=['words'])
dfNew
cont = 1
while cont < len(df):
    dfAux = pd.DataFrame(df['content'].iloc[cont], columns=['words'])
    frames = [dfNew, dfAux]
    dfNew = pd.concat(frames)
    cont += 1

dfNew