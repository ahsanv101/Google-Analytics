import tweepy as tw
import requests
import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

consumer_key= 'GJyd3G73WbqCNFQvUSwZ3M5PZ'
consumer_secret= 'Ph9YcMUZVduIjlb1o3lBLEtTSAtqdNxJpOrjZE5jqWTIhCoz33'
access_token= '1217865572-aZcjHlqlXaGyXXcb7D6xc02wIjQXJLtC4CXRB96'
access_token_secret= 'irgJlETZ7DYVNGozvzpr1OhfrKVKCjLfo22Obch4klF3p'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

a=input("Please enter phrase or hastag: ")
b=input("Please enter tweet limit per every 2 minute: ")

def tweetR():
    tweets = tw.Cursor(api.search,
                  q=a,
                  lang="en").items(int(b))

    for tweet in tweets:
        text=tweet.text
        params = {
            'v': '1',
            'tid': 'UA-141667083-1',
            't': 'event',
            'ec': 'tweet',
            'ea': text,
            'el': tweet.user.name,
            'ev': text.count('#'),
            'cid': tweet.user.screen_name,
        }
        endpoint = 'https://www.google-analytics.com/collect'
        r = requests.post(url = endpoint,verify=False, data = params
              , headers={'User-Agent': 'My User Agent 1.0'})
        print(r)
    threading.Timer(120, tweetR).start()

tweetR()



