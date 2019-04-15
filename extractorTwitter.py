import tweepy

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
public_tweets = api.search(q='telemedicina', count=100)
public_tweets

cont = 0
lastId = 0
i = 0
while i <= 10: 
    if i >= 1:
        public_tweets = api.search(q='telemedicina', count=100, max_id=lastId)
    for tweet in public_tweets:
        
        # atw.append(tweet.id)
        # atw.append(tweet.created_at)
        # atw.append(tweet.user.id)
        # atw.append(tweet.text)
        print('--------------------')
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.user.id)
        print(tweet.user.screen_name)
        print(tweet.text)
        print(cont)
        lastId = tweet.id

        cont += 1
        if cont >= 1000:
            break
        
    
    i += 1
