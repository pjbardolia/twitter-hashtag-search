from Twython import Twython

TWITTER_APP_KEY = 'uIK8z7sG1ogwzmIBjGyP9mST8' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'NbP7hVFTY0QFkOqAV4w6No3F9RNfPphuyaqXHKLSIFpsx39tbU' 
TWITTER_ACCESS_TOKEN = '85787905-NNL57uu34LQV0F5n2SO8SQ0zYFfbbDDBYODwLYNFx'
TWITTER_ACCESS_TOKEN_SECRET = 'y9sGKomATulARLf3lFYJXCvBSxeT1UEqjHiz4zXUAOoaB'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#thisisatesttweet',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
