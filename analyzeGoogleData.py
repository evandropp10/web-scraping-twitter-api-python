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

# Colocando todas as palavras em um único dataframe em uma única coluna
cont = 1
while cont < len(df):
    dfAux = pd.DataFrame(df['content'].iloc[cont], columns=['words'])
    frames = [dfNew, dfAux]
    dfNew = pd.concat(frames)
    cont += 1

## Início da limpeza dos dados
# Eliminando todas as palavras com menos de 4 letras
cont = 0
while cont < len(dfNew):
    if len(dfNew['words'].iloc[cont]) <= 3:
        dfNew = dfNew.drop(cont)
    cont += 1
    if cont == len(dfNew):
        break

print(dfNew)

print('ok1')


