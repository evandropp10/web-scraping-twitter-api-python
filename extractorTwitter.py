import tweepy
import pymongo

def insertMongoDB(values):
    #client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb://datastore:27017/')
    db = client['database']
    coll = db['twitter']

    x = coll.insert_many(values)
    print(x.inserted_ids)


def queryTwitter(search):

    ## TWEETER KEYS
    consumer_key = 'rYffQfwjwOlDjFNNuauV2R46w'
    consumer_secret = 'CjTcQanzKiGNra75MbF3vLT9zhdHUuilhgfxnGJiN35uA7RQ6a'
    access_token = '1091274790332190720-QLYCMs2IYsIkXEV3qnDLbDgk0BTsSP'
    access_token_secret = 'n7fnnQe71joWSlkYKbZ9XkuiNKxOqUz09pcDKMBTfFEAz'

    ## TWEETER AUTH ACESS
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #public_tweets = api.search('bitcoin since:2012-01-01 until:2014-01-30') #, lang='en', rpp=100)
    public_tweets = api.search(q=search, count=100)

    values = []
    cont = 0
    lastId = 0
    i = 0
    while i <= 10: 
        if i >= 1:
            public_tweets = api.search(q=search, count=100, max_id=lastId)
        for tweet in public_tweets:
           
            lastId = tweet.id

            obj = {'user': tweet.user.screen_name,
                    'datetime': tweet.created_at,
                    'text': tweet.text,
                    'id': tweet.id }
            values.append(obj) 

            cont += 1
            if cont >= 1000:
                break
        
        i += 1

    insertMongoDB(values)